import os
import secrets
from datetime import timedelta
from bson import ObjectId
from fastapi import status, Request, HTTPException, APIRouter
from fastapi import APIRouter, HTTPException, Depends, Query
from app.components.auth.jwt_token_handler import get_jwt_username
from app.components.auth.check_permissions import check_permissions

from app.classes.User import User, Role, UserRegistration
from app.classes.Quiz import Quiz, QuizResponse
from app.components.hash_password import hash_password
from app.components.logger import logger
from app.components.message_dispatcher.mail import send_email_and_save
from app.db.mongoClient import async_database
from app.db.downloadReport import generate_report_download_url, check_blob_exist
from app.db.uploadReport import upload_report
from app.routers.users import user_exists
from fastapi.encoders import jsonable_encoder
from gai_report.main_eng_db_v1 import generate_report
from app.db.stream_mapping import stream_mapping

router = APIRouter()  # router instance
user_collection = async_database.users  # Get the collection from the database
quiz_collection = async_database.quizes  # Get the collection from the database
quiz_response_collection = async_database.quiz_response  # Get the collection from the database


@router.get("/quiz/", dependencies=[Depends(check_permissions)])
async def get_quiz(quiz_id: str, user_id: str):
    print(f"Fetching quiz with ID: {quiz_id}")
    print(f"Received request for user_id: {quiz_id}")
    user = await user_collection.find_one({"username": user_id})
    if not user:
        logger.error(f"User with id {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    if (quiz_id=="3"):
        quiz_id_final = f"{quiz_id}_{user.get('standard')}_{stream_mapping.get(user.get('stream'), 'allsubj')}"
    else:
        quiz_id_final = quiz_id
    logger.info(f"Quiz_final_id::", quiz_id_final)
    quiz = await quiz_collection.find_one({"id": quiz_id_final})
    logger.info(f"Quiz fetched, detail:", quiz)
    logger.info(f"Quiz has been fetched successfully", jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]}))
    if not quiz_id or not user_id:
        raise HTTPException(status_code=422, detail="Invalid query parameters")
    print("Quiz Details:::", jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]}))
    return jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]})

@router.get("/check-quiz-response-exist/", dependencies=[Depends(check_permissions)])
async def check_quiz_response_exist(quiz_id: str, user_id: str):
    try:
        # Debugging: Log the incoming response
        print("Check quiz response for user_id", user_id)
        # Save user response in the database
        user = await user_collection.find_one({"username": user_id})
        if (quiz_id=="3"):
            quiz_id_final = f"{quiz_id}_{user.get('standard')}_{stream_mapping.get(user.get('stream'), 'allsubj')}"
        else:
            quiz_id_final = quiz_id
        result = await quiz_response_collection.find_one({"username": user_id, "quizId": quiz_id_final})
        if result:
            return {"message": "You have already submitted the quiz", "message_code": "already_submitted"}
        else:
            return {"message": "You have not submitted the quiz", "message_code": "not_submitted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/save-quiz-response/", dependencies=[Depends(check_permissions)])
async def save_quiz_response(response: QuizResponse):
    try:
        # Debugging: Log the incoming response
        print("Received response payload:", response.dict())
        # Save user response in the database
        result = await quiz_response_collection.insert_one(response.dict())
        return {"message": "Responses saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/check-report-exist/", dependencies=[Depends(check_permissions)])
async def check_report_exist(user_id: str):
    try:
        # Fetch user from the database
        logger.info(f"Entered in generate report function")
        logger.info(f"Received request for user_id: {user_id}")
        # logger.info(f"Headers: {request.headers}")
        report_name = user_id + ".pdf"
        flg = check_blob_exist(blob_name=report_name)
        if flg:
            return {"message": "Report already generate", "message_code": "already_generated"}
        else:
            return {"message": "Report has not generated", "message_code": "not_generated"}

    except HTTPException as http_exc:
        raise http_exc  # Propagate HTTP exceptions as-is
    except Exception as e:
        logger.exception("Unexpected error occurred while processing the request")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@router.post("/generate-report/", dependencies=[Depends(check_permissions)])
async def generate_student_report(user_id: str):
    try:
        # Fetch user from the database
        logger.info(f"Entered in generate report function")
        logger.info(f"Received request for user_id: {user_id}")
        # logger.info(f"Headers: {request.headers}")
        user = await user_collection.find_one({"username": user_id})
        if not user:
            logger.error(f"User with id {user_id} not found")
            raise HTTPException(status_code=404, detail="User not found")

        # Prepare user details
        logger.info(f"Fetched user in generate-report function for {user_id}, {user}")
        user_detail_dict = {
            "username": str(user.get("username")),
            "email": str(user.get("email")),
            "full_name": str(user.get("full_name")),
            "standard": str(user.get("standard")),
            "school_name": str(user.get("school_name")),
            "stream": str(user.get("stream")),
        }
        logger.info(f"Report being generated with details: {user_detail_dict}")

        # Generate the report
        pdf_report_url = await generate_report(user_detail_dict)
        if not pdf_report_url:
            logger.error("Failed to generate PDF report URL")
            raise HTTPException(status_code=500, detail="Report generation failed")

        # Construct the report URL
        # report_url = os.path.join("gai_report", pdf_report_url)
        logger.info(f"Report download link generated successfully for user: {user_detail_dict}")

        # Upload the report
        result = await upload_report(pdf_report_url)
        if not result:
            logger.error("Failed to upload report")
            raise HTTPException(status_code=500, detail="Report upload failed")

        return {"message": "Responses saved successfully", "id": str(user_id)}

    except HTTPException as http_exc:
        raise http_exc  # Propagate HTTP exceptions as-is
    except Exception as e:
        logger.exception("Unexpected error occurred while processing the request")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@router.get("/report-download-link/", dependencies=[Depends(check_permissions)])
async def get_report_download_link(user_id: str):
    try:
        report_name = user_id + ".pdf"
        if check_blob_exist(report_name):
            print(f"Downloading report for user_id: {user_id}")
            report_download_link = generate_report_download_url(blob_name=report_name)
            logger.info(f"Report download link generated successfully")
            return report_download_link
        else:
            print(f"report for {user_id} does not exist")
            raise HTTPException(status_code=404, detail=f"Report for user_id {user_id} not exist. Either you have not completed tests or your report not generated yet")
    except Exception as e:
        logger.error(f"Error generating report download link for {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

