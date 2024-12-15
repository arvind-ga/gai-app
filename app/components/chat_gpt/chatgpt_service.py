import logging
import os
import requests
import httpx
from dotenv import load_dotenv
from app.db.mongoClient import async_database
from app.components.logger import logger
from uuid import uuid4

chat_collection = async_database.chatgpt  # Get the collection from the database

load_dotenv()
# API_KEY = os.getenv("open_ai_secret_key")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ask_chatgpt_with_context(gpt_question: str, username: str, model: str = "gpt-4"):
    content = """
      # YOUR ROLE #
      You are an expert career counsellor. Your responsibility is to understand student's query 
      for career or academic help for K12 student in indian context. Below is the query from the 
      student {gpt_question}
      """.format(gpt_question=gpt_question)

    ###################

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    # Payload for the request
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": content
                        # "text": "You are an AI assistant that helps people find information."
                    }
                ]
            }
        ],
        "temperature": 0.5,
        "top_p": 0.15,
        "max_tokens": 800
    }

    ### Model Out
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if 'choices' not in data:
            raise ValueError("Unexpected API response format")
        processed_response = ''.join(choice['message']['content'] for choice in data['choices'] if
                       'message' in choice and 'content' in choice['message'])
        chat_dict = {"id": f"{username}_{uuid4()}", "model": model, "payload": payload, "model_response": processed_response}
        logger.info(f"Returning query response in chatgpt_service {chat_dict}")
        chat_collection.insert_one(chat_dict)
        return processed_response
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")


# Example usage
if __name__ == "__main__":
    question = "I am in class 10th, what should I do?"
    print(ask_chatgpt_with_context(question))
