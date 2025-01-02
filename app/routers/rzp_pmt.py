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


# mongo connection
all_txn_collection = async_database.all_txn  # Get the collection from the database
user_txn_collection = async_database.user_payment  # Get the collection from the database
booking_collection = async_database.session_booking

RZP_ID = os.getenv("RZP_ID")
RZP_PASS = os.getenv("RZP_KEY")

feature_amt_mapping = {"report": 200, "chat": 300, "session": 500}
offer_id = "offer_PegUdktBeVOe7X"

class CreateOrderRequest(BaseModel):
    username: str
    feature: str = "chat"
    # amount: int = 5
    # offer_id: str = "offer_PeGBYGqWZX2ocG"

# class UpdatePmtStatus(BaseModel):
#     username: str
#     report_pmt_status: bool = False
#     chat_pmt_status: bool = False
#     session_pmt_status: List[Dict[str, Bool]]

class UpdateTxnStatus(BaseModel):
    username: str
    feature: str = "chat"
    session_id: str = ""
    act_amount: int = 500
    disc_amount: int = 200
    razorpay_order_id: str = "order_PeY83Ow8BHK34C"
    razorpay_payment_id: str = "pay_PeY8FteUwlwwfI"
    razorpay_signature: str = "4cf3104a1fca632af366fb2b0ec85633bc58ea77a2dac6e4b5e988976cd337af"

@router.post("/create-order/", dependencies=[Depends(check_permissions)])
async def create_order(order: CreateOrderRequest):
    try:
        client = razorpay.Client(auth=(RZP_ID, RZP_PASS))
        DATA = {
            "amount": feature_amt_mapping.get(order.feature),
            "currency": "INR",
            "receipt": "receipt#1",
            "partial_payment": False,
            "offer_id": offer_id,
            "notes": {
                "username": order.username
            }
        }
        logger.info(f"Error while uploading report: {str(DATA)}")
        response = client.order.create(data=DATA)
        response = client.order.create(data=DATA)
        response1 = {"username": order.username, "rzp_id": RZP_ID, "order_id": response.get("id"), "amount": response.get("amount"), "amount_due": response.get("amount_due")}
        return response1
    except Exception as e:
        logger.error(f"Error while uploading report: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/post-rzp-pmt/", dependencies=[Depends(check_permissions)])
async def update_pmt_status(order_details: UpdateTxnStatus):
    try:
        username = order_details.username
        txn_uid = f"{username}_{order_details.razorpay_order_id}"
        txn_uid_dict = {"id": txn_uid, "order_details": order_details.dict()}
        all_txn_collection.insert_one(txn_uid_dict)
        ###
        result1 = await user_txn_collection.find_one({"id": username})
        feature = order_details.feature
        # Update based on the feature
        if result1:
            filter = {"id": username}
            if feature == "report":
                update = {"$set": {"report_pmt_status": True}}
            elif feature == "chat":
                update = {"$set": {"chat_pmt_status": True}}
            elif feature == "session":
                update = {"$set": {"session_pmt_status": [{order_details.session_id: True}]}}
            else:
                raise ValueError("Invalid feature type")

            result2 = await user_txn_collection.update_one(filter, update)
        else:
            if feature == "report":
                user_dict = {
                    "id": username,
                    "report_pmt_status": True,
                    "chat_pmt_status": False,
                    "session_pmt_status": [],
                }
            elif feature == "chat":
                user_dict = {
                    "id": username,
                    "report_pmt_status": False,
                    "chat_pmt_status": True,
                    "session_pmt_status": [],
                }
            elif feature == "session":
                user_dict = {
                    "id": username,
                    "report_pmt_status": False,
                    "chat_pmt_status": False,
                    "session_pmt_status": [{order_details.session_id: True}],
                }
            else:
                raise ValueError("Invalid feature type")

            result2 = await user_txn_collection.insert_one(user_dict)
        if feature == "session":
            filter = {"id": order_details.session_id}
            update = {"$set": {"status": "Confirmed"}}
            result3 = await booking_collection.update_one(filter, update)
        return {"message": "Transaction updated successfully"}
    except ValueError as ve:
        logger.error(f"Validation Error: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Error while uploading report: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")