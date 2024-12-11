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
from app.db.downloadReport import generate_report_download_url, check_blob_exists
from app.db.uploadReport import upload_report
from app.routers.users import user_exists
from fastapi.encoders import jsonable_encoder
from gai_report.main_eng_db_v1 import generate_report





router = APIRouter()  # router instance
user_collection = async_database.users  # Get the collection from the database
quiz_collection = async_database.quizes  # Get the collection from the database
quiz_response_collection = async_database.quiz_response  # Get the collection from the database


@router.get("/quiz/{quiz_id}")
async def get_quiz(quiz_id: str):
    print(f"Fetching quiz with ID: {quiz_id}")
    print(f"Received request for quiz_id: {quiz_id}")
    quiz = await quiz_collection.find_one({"id": quiz_id})
    logger.info(f"Quiz has been fetched successfully", jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]}))
    if not quiz:
        raise HTTPException(status_code=404, detail=f"Quiz with ID {quiz_id} not found")
    print("Quiz Details:::", jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]}))
    return jsonable_encoder({"id": quiz["id"], "questions": quiz["questions"]})

@router.post("/save-quiz-response")
async def save_quiz_response(response: QuizResponse):
    try:
        # Debugging: Log the incoming response
        print("Received response payload:", response.dict())
        # Save user response in the database
        result = await quiz_response_collection.insert_one(response.dict())
        return {"message": "Responses saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/report-generate/{user_id}")
async def save_quiz_response(user_id: str):
    try:
        # Generate Report
        user_detail = user_collection.find_one({"id": user_id})
        pdf_report_url = await generate_report(user_detail)
        # report_url = os.path.join("gai_report", pdf_report_url)
        result = await upload_report(report_url)
        return {"message": "Responses saved successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/report-download-link/{user_id}")
async def get_report_download_link(user_id: str):
    try:
        report_name = user_id + ".pdf"
        if check_blob_exists(report_name):
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

