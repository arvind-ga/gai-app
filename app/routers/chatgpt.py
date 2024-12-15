from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.classes.Chatgpt import ChatGptModelEnum
from app.components.auth.check_permissions import check_permissions
from app.components.chat_gpt.chatgpt_service import ask_chatgpt_with_context
from app.db.mongoClient import async_database
from app.components.logger import logger

router = APIRouter()  # loading the FastAPI app
chat_collection = async_database.chatgpt  # Get the collection from the database

@router.get("/chat/", dependencies=[Depends(check_permissions)])
async def chat_with_gpt(question: str, model: ChatGptModelEnum, username: str):
    """
    Chat with ChatGPT
    """
    answer = ask_chatgpt_with_context(question, model)
    chat_dict = {"username": username, "model": model, "query": question, "model_response": answer}
    logger.info(f"Returning query response {chat_dict}")
    new_chat = await chat_collection.insert_one(chat_dict)
    return JSONResponse(content={"message": answer})
