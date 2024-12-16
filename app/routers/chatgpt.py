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
async def chat_with_gpt(question: str, model: str, username: str ):
    logger.info(f"Inside chat router::: {question} {username} {model}")
    """
    Chat with ChatGPT
    """
    answer = ask_chatgpt_with_context(question, username, model)
    return JSONResponse(content={"message": answer})
