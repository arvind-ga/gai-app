from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.classes.Chatgpt import ChatGptModelEnum
from app.components.auth.check_permissions import check_permissions
from app.components.chat_gpt.chatgpt_service import ask_chatgpt_with_context
from app.db.mongoClient import async_database
from app.components.logger import logger
import yaml


with open("./config/gai_config.yml", "r") as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

router = APIRouter()  # loading the FastAPI app
chat_collection = async_database.chatgpt  # Get the collection from the database
chat_query_cnt_collection = async_database.chat_query_count # Get the collection from the database
user_payment_collection = async_database.user_payment # Get the collection from the database

user_query_count_limit = config.get("free_limit").get("chat_query_count") #500
chat_query_free_flg = config.get("payment").get("chat") #500


async def update_chat_query_count(username: str):
    logger.info(f"Inside chat_query_count router::: {username}")
    result = await chat_query_cnt_collection.find_one({"id": username})  # Fix `usename`
    if not result:
        count = 1  # Initialize count
        await chat_query_cnt_collection.insert_one({"id": username, "total_query_count": count})  # Use `insert_one`
        logger.info(f"Query count initialized for user::: {username}")
    else:
        count = result["total_query_count"]
        count += 1
        filter = {"id": username}
        update = {"$set": {"total_query_count": count}}
        await chat_query_cnt_collection.update_one(filter, update)
        logger.info(f"Query count updated for user::: {username}")

async def get_chat_query_count1(username: str):
    logger.info(f"Inside chat_query_count router::: {username}")
    result = await chat_query_cnt_collection.find_one({"id": username})  # Fix `usename`
    if not result:
        count = 0
    else:
        count = result.get("total_query_count", 0)
    return {"user_query_count": count, "user_query_count_limit": user_query_count_limit}


@router.get("/chat/", dependencies=[Depends(check_permissions)])
async def chat_with_gpt(question: str, model: ChatGptModelEnum, username: str):
    logger.info(f"Chat request received: question={question}, username={username}, model={model}")
    try:
        if chat_query_free_flg == "disable":
            logger.info("Chat query flag is set to 'disable'.")
            try:
                answer = ask_chatgpt_with_context(question, username, model)
                await update_chat_query_count(username)
                logger.info("Chat query successfully processed and count updated.")
                return JSONResponse(content={"message": answer})
                
            except Exception as e:
                logger.error(f"Error in processing chat query with flag 'disable': {e}")
                return JSONResponse(content={"error": "An error occurred while processing your request."}, status_code=500)

        elif chat_query_free_flg == "enable":
            logger.info("Chat query flag is set to 'enable'.")
            try:
                chat_query_cnt_dict = await get_chat_query_count1(username)
                chat_query_cnt = chat_query_cnt_dict["user_query_count"]
                chat_query_cnt_limit = chat_query_cnt_dict["user_query_count_limit"]
                logger.info(f"Retrieved query count: {chat_query_cnt}/{chat_query_cnt_limit} for user {username}")

                if chat_query_cnt < chat_query_cnt_limit:
                    logger.info("User is within the query limit.")
                    answer = ask_chatgpt_with_context(question, username, model)
                    await update_chat_query_count(username)
                    logger.info("Chat query successfully processed and count updated.")
                    return JSONResponse(content={"message": answer, "isLimitExceeded": False})

                logger.info("User has exceeded the query limit. Checking payment status.")
                result = await user_payment_collection.find_one({"id": username})
                if result:
                    chat_pmt_status = result.get("chat_pmt_status")
                    if chat_pmt_status == True:
                        answer = ask_chatgpt_with_context(question, username, model)
                        await update_chat_query_count(username)
                        logger.info("Chat query processed successfully after payment validation.")
                        return JSONResponse(content={"message": answer})
                logger.info("User has not made a payment. Returning free limit exceeded message.")
                return JSONResponse(
                    content={
                        "message": "YOUR FREE LIMIT EXCEEDED, PLEASE PAY TO ASK MORE QUESTIONS",
                        "isLimitExceeded": True,
                        "error": "Free limit exceeded, please make payment"
                    }
                )
            except Exception as e:
                logger.error(f"Error in processing chat query with flag 'enable': {e}")
                return JSONResponse(content={"error": "An error occurred while processing your request."}, status_code=500)

        else:
            logger.error(f"Invalid chat_query_free_flg value: {chat_query_free_flg}")
            return JSONResponse(content={"error": "Invalid configuration."}, status_code=500)

    except Exception as e:
        logger.error(f"Unexpected error in chat_with_gpt: {e}")
        return JSONResponse(content={"error": "An unexpected error occurred."}, status_code=500)



@router.get("/chat_query_count/", dependencies=[Depends(check_permissions)])
async def get_chat_query_count(username: str):
    logger.info(f"Inside chat_query_count router::: {username}")
    result = await chat_query_cnt_collection.find_one({"id": username})  # Fix `usename`
    count = result.get("total_query_count", 0) if result else 0
    return JSONResponse(content={"user_query_count": count, "user_query_count_limit": user_query_count_limit})


