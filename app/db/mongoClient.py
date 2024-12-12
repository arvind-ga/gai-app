import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from app.components.logger import logger

load_dotenv()  # loading environment variables

# MONGODB_USER = os.getenv("mongodb_username")
# MONGODB_PASS = os.getenv("mongodb_password")
# MONGODB_SERVER = os.getenv("mongodb_server")
# MONGODB_PORT = os.getenv("mongodb_port")

MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
# Asynchronous MongoDB connection
async_mdb_client = AsyncIOMotorClient(MONGODB_CONNECTION_STRING)  # setting mongodb client for asynchronous operations
async_database = async_mdb_client['fastapi_db']  # database name in mongodb for asynchronous operations

# Function to validate connection
async def validate_mongodb_connection():
    try:
        # Attempt to count documents in a specific collection, e.g., 'test_collection'
        count = await async_database['test_collection'].count_documents({})
        print(f"Connection Successful! Found {count} documents in 'test_collection'.")
        logger.info(f"Connection Successful! Found {count} documents in 'test_collection'.")
    except Exception as e:
        logger.info(f"Connection to MongoDB failed: {e}")

# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())