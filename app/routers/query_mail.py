import os
import secrets
from datetime import timedelta
from pydantic import EmailStr

from bson import ObjectId
from fastapi import status, Request, HTTPException, APIRouter

from app.components.hash_password import hash_password
from app.components.logger import logger
from app.components.message_dispatcher.mail import send_email_and_save
from app.db.mongoClient import async_database
from app.routers.users import user_exists
from azure.communication.email import EmailClient
from azure.core.exceptions import HttpResponseError

from dotenv import load_dotenv
load_dotenv() 

router = APIRouter()  # router instance

@router.post("/query/")
async def send_query(name: str, email: EmailStr, mobile: str, subject: str, body: str):

    # Look for the user in the database using the provided email address.
    logger.info(f"Entered email for query: {email}")

    # request = Request()
    # redis_client = request.app.state.redis

    # Email the user with the reset token
    host_ip = os.getenv("host_server_ip")
    az_comm_connection_string = os.getenv("AZURE_COMM_STRING")
    print("Query to be sent")
    try:
        client = EmailClient.from_connection_string(az_comm_connection_string)

        message = {
            "senderAddress": "DoNotReply@82c05fc9-8a5d-48a5-a90b-cf40e56d015d.azurecomm.net",
            "recipients": {
                "to": [{"address": "info@gakudoai.onmicrosoft.com"}]
            },
            "content": {
                "subject": "Query from website",
                "plainText": name,
                "html": f"""
                <html>
                    <body>
                        <p>Name: {name}</p>
                        <p>Email: {email}</p>
                        <p>Mob No.: {mobile}</p>
                        <p>Subject: {subject}</p>
                        <p>Body: {body}</p>
                    </body>
                </html>""".format(name=name, email=email, subject=subject, body=body)
            },
        }


        poller = client.begin_send(message)
        result = poller.result()
        if result:
            print(f"Query email sent successfully! Message ID: {result}")
        else:
            print("Failed to send email.")
        return {"message": "You query has been sent successfully!"}

    except HttpResponseError as e:
        print(f"Error sending email: {e}")
