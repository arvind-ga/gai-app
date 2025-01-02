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

import asyncio
import os
from aiosmtplib import SMTP, SMTPException
from bson import ObjectId
from fastapi import UploadFile, HTTPException

from app.db.mongoClient import async_mdb_client, async_database

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from app.components.logger import logger
from pydantic import BaseModel

import razorpay

load_dotenv()  # loading environment variables

router = APIRouter()  # router instance
# booking_collection = async_database.session_booking  # Get the collection from the database

# mongo connection
# config_collection = async_database.settings
# emails_collection = async_mdb_client.messages.emails_sent
RZP_ID = os.getenv("RZP_ID")
RZP_PASS = os.getenv("RZP_KEY")

class CreateOrderRequest(BaseModel):
    username: str
    feature: str = "chat"
    amount: int = 599
    offer_id: str = "offer_PeGBYGqWZX2ocG"

@router.post("/create-order/", dependencies=[Depends(check_permissions)])
async def create_order(order: CreateOrderRequest):
    try:
        client = razorpay.Client(auth=(RZP_ID, RZP_PASS))
        DATA = {
            "amount": order.amount,
            "currency": "INR",
            "receipt": "receipt#1",
            "partial_payment": False,
            "offer_id": order.offer_id,
            "notes": {
                "username": order.username
            }
        }
        response = client.order.create(data=DATA)
        response1 = {"rzp_id": RZP_ID, "order_id": response.get("id"), "username": order.username}
        return response1
    except Exception as e:
        logger.error(f"Error while uploading report: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.get("/create-order/", dependencies=[Depends(check_permissions)])
# async def create_order(username: str, amount: int):
#     try:
#         client = razorpay.Client(auth=(RZP_ID, RZP_PASS))
#         DATA = {
#             "amount": 2497,
#             "currency": "INR",
#             "receipt": "receipt#1",
#             "partial_payment": false,
#             "notes": {
#                 "username": username,
#                 "key2": "value2"
#             }
#         }
#         response = client.order.create(data=DATA)
#     except Exception as e:
#         logger.error(f"Error while uploading report: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
