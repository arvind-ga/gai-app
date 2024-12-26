from typing import List

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends, Query
from starlette import status

from app.classes.Booking import BookingRequest
from app.components.auth.check_permissions import check_permissions
from app.components.auth.jwt_token_handler import get_jwt_username
from app.components.hash_password import hash_password
from app.components.logger import logger
from app.db.mongoClient import async_database
import uuid


router = APIRouter()  # router instance
booking_collection = async_database.session_booking  # Get the collection from the database

@router.get("/fetch-booking/", dependencies=[Depends(check_permissions)])
async def book_session(username: str):  # noqa
    try:
        booking_dict = {"username":username}
        logger.info(f"User {username} fetching booking.")
        bookings = await booking_collection.find({"username": username}).to_list(length=None)
        # bookings = [del booking["_id"] for booking in bookings if "_id" in booking]
        for booking in bookings:
            if "_id" in booking:
                del booking["_id"]
        logger.info(f"Bookings: {bookings}")  # Log bookings
        return {"message": "Booking fetched successfully", "booking_list": bookings}
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/booking/", dependencies=[Depends(check_permissions)])
async def book_session(request: BookingRequest):  # noqa
    logger.info(f"Received booking request: {request}")
    try:
        uuid1 = str(uuid.uuid4())
        id1 = f"{request.username}_{uuid1}"
        booking_dict = {
            "id": id1,
            "username": request.username,
            "date_time": request.dateTime,
            "remark": request.remark,
            "status": "In Progress",
        }
        logger.info(f"User {request.username} making booking for date: {request.dateTime} successfully.")
        result = await booking_collection.insert_one(booking_dict)
        return {"message": "Booking done successfully", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))



