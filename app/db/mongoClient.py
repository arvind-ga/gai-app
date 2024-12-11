import asyncio
import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from app.components.logger import logger

load_dotenv()  # loading environment variables

MONGODB_USER = os.getenv("mongodb_username")
MONGODB_PASS = os.getenv("mongodb_password")
MONGODB_SERVER = os.getenv("mongodb_server")
MONGODB_PORT = os.getenv("mongodb_port")

MONGODB_CONNECTION_STRING1 = f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_SERVER}:{MONGODB_PORT}/fastapi_db?authSource=admin&authMechanism=SCRAM-SHA-256"
print("MONGODB_CONNECTION_STRING::", MONGODB_CONNECTION_STRING1)
MONGODB_CONNECTION_STRING = f"mongodb://gakudoai-app-db:U6m0miKzJ7sCCHQkZCymYOYAKo63Imkz0h91DXPNh4vA4islkNRPtDXHjB1T6D0aT1XnXfNF6jXDACDbyj0l2Q==@gakudoai-app-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@gakudoai-app-db@"

# Asynchronous MongoDB connection
async_connection_string = f'{MONGODB_CONNECTION_STRING}'  # This can be the same as the synchronous connection string
async_mdb_client = AsyncIOMotorClient(async_connection_string)  # setting mongodb client for asynchronous operations
async_database = async_mdb_client['fastapi_db']  # database name in mongodb for asynchronous operations

# Function to validate connection
async def validate_mongodb_connection():
    try:
        # Attempt to count documents in a specific collection, e.g., 'test_collection'
        count = await async_database['test_collection'].count_documents({})
        print(f"Connection Successful! Found {count} documents in 'test_collection'.")
    except Exception as e:
        logger.info(f"Connection to MongoDB failed: {e}")

# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())