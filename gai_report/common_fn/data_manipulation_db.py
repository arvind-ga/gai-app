import pandas as pd
import os
import matplotlib.pyplot as plt
import asyncio

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

from gai_report.common_fn.parameter_mapping import *
from gai_report.eng_fn.eng_report_generate_fn import *
from app.db.stream_mapping import stream_mapping
from app.components.logger import logger


# from app.components.logger import logger

###
img_path = "/Users/arvindyadav/Documents/1_GakudoAI_work/3_School_Stream_Selector/06_report_generation_data/images/rocket-in-space.webp"
gakudoai_logo_path = "/Users/arvindyadav/Documents/1_GakudoAI_work/3_School_Stream_Selector/06_report_generation_data/images/gakudoai_logo.jpeg"
# data_path1 = "/content/drive/MyDrive/1_GakudoAI_data/1_gakudoAI_school/0_gakudoai_report_generation_v1/1_gpt4_data_sample_v1.csv"
# df1 = pd.read_csv(data_path1)
#########

##################################
MONGODB_CONNECTION_STRING = f"mongodb://gakudoai-app-db:U6m0miKzJ7sCCHQkZCymYOYAKo63Imkz0h91DXPNh4vA4islkNRPtDXHjB1T6D0aT1XnXfNF6jXDACDbyj0l2Q==@gakudoai-app-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@gakudoai-app-db@"

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Asynchronous MongoDB connection
async_connection_string = f'{MONGODB_CONNECTION_STRING}'  # Replace with your connection string
async_mdb_client = AsyncIOMotorClient(async_connection_string)  # Setting MongoDB client for asynchronous operations
async_database = async_mdb_client['fastapi_db']  # Database name in MongoDB for asynchronous operations


# Function to validate connection
async def fetch_quiz_resp(user_email, quiz_id="1"):
    try:
        # Attempt to count documents in a specific collection, e.g., 'test_collection'
        count = await async_database['test_collection'].count_documents({})
        print(f"Connection Successful! Found {count} documents in 'test_collection'.")

        # Fetching data from the quiz response collection
        quiz_resp = await async_database['quiz_response'].find_one({"quizId": str(quiz_id), "email":str(user_email)})
        return quiz_resp
    except Exception as e:
        print(f"Connection to MongoDB failed: {e}")
        return None

# Function to validate connection
async def fetch_quiz(quiz_id="1"):
    try:
        # Attempt to count documents in a specific collection, e.g., 'test_collection'
        count = await async_database['test_collection'].count_documents({})
        print(f"Connection Successful! Found {count} documents in 'test_collection'.")

        # Fetching data from the quiz response collection
        quiz = await async_database['quizzes'].find_one({"id": str(quiz_id)})
        print("quiz::", quiz)
        return quiz
    except Exception as e:
        print(f"Connection to MongoDB failed: {e}")
        return None

# async def main(user_email):
async def get_dfs(user_email): #, standard, stream):

    # user_email = "mangalsikarwar@gmail.com"
    user_collection = async_database['users']

    # Check if user exists
    user = await user_collection.find_one({"email": user_email})  # Await the find_one call
    if user:
        print("User with email {} exist".format(user_email))
        quiz_idd = "3_" + str(user.get("standard")) + "_" + str(stream_mapping.get(user.get("stream")))
        logger.info(f"quiz_idd:::", quiz_idd)
        # Fetch quiz responses
        q1_resp1 = await fetch_quiz_resp(user_email, quiz_id="1")  # Await the fetch
        q1_resp2 = await fetch_quiz_resp(user_email, quiz_id="2")
        q1_resp3 = await fetch_quiz_resp(user_email, quiz_id=quiz_idd)
        q1_resp4 = await fetch_quiz_resp(user_email, quiz_id="1")

        # Fetch quiz for correct Answers
        quiz2 = await fetch_quiz(quiz_id="2")
        quiz3 = await fetch_quiz(quiz_id=quiz_idd)
        print("quiz2:::", quiz2)
        print("quiz3:::", quiz3)
        quiz2q = quiz2.get("questions")
        quiz3q = quiz3.get("questions")
        quiz2a = [{"id": i["id"], "answer": i["answer"], "segment": i["segment"]} for i in quiz2q]
        quiz3a = [{"id": i["id"], "answer": i["answer"], "segment": i["segment"]} for i in quiz3q]
        print("quiz2a:", quiz2a)
        print("quiz3a:", quiz3a)
        # Safely access and print data
        if q1_resp1:
            print("q1_resp1:", {"id": q1_resp1.get("quizId"), "email": q1_resp1.get("email"), "questions": q1_resp1.get("responses")})
            print("q1_resp1:", {"id": q1_resp2.get("quizId"), "email": q1_resp2.get("email"), "questions": q1_resp2.get("responses")})
            # print("q1_resp1:", {"id": q1_resp3.get("quizId"), "email": q1_resp3.get("email"), "questions": q1_resp3.get("responses")})
            # print("q1_resp1:", {"id": q1_resp4.get("quizId"), "email": q1_resp4.get("email"), "questions": q1_resp4.get("responses")})
            dict1 = q1_resp1.get("responses")
            dict2 = q1_resp2.get("responses")
            dict3 = q1_resp3.get("responses")
            dict4 = q1_resp4.get("responses")
            # user_detail = {}
            # user_detail["email_add"] = user_email
            # user_detail["username"] = q1_resp1.get("username")
            dfr1 = pd.DataFrame(dict1.items(), columns=["question_id", "response"])
            dfr2 = pd.DataFrame(dict2.items(), columns=["question_id", "response"])
            dfr3 = pd.DataFrame(dict3.items(), columns=["question_id", "response"])
            dfr4 = pd.DataFrame(dict4.items(), columns=["question_id", "response"])
            dfa2 = pd.DataFrame(quiz2a)
            dfa2.columns = ["question_id", "answer", "segment"]
            dfa3 = pd.DataFrame(quiz3a) #.items(), columns=["question", "answer"])
            dfa3.columns = ["question_id", "answer", "segment"]
            dfa3["question_id"] = dfa3["question_id"].astype(str)
            # print("user_detail", user_detail)
            # print("dfr1", dfr1)
            # print("dfr2", dfr2)
            # print("dfr3", dfr3)
            # print("dfr4", dfr4)
            print("dfa2 columns:", dfa2.columns)
            print("dfa3 columns", dfa3.columns)
            return dfr1, dfr2, dfr3, dfr4, dfa2, dfa3
            # print(dff.shape)
            # print(dff.tail())
            # print("dict1", type(dict1))
            # print("dict2", dict2)
            # final_dict = {}
            # final_dict["email_add"] = user_email
            # final_dict["username"] = q1_resp1.get("username")
            # for k,v in dict1.items():
            #     k1 = "t1_q" + str(k)
            #     final_dict[k1] = v
            # for k,v in dict2.items():
            #     k1 = "t2_q" + str(k)
            #     final_dict[k1] = v
            # print("final_dict:", final_dict)


        else:
            print("q1_resp1 not found")
    else:
        print("User with email {} does not exist".format(user_email))

    # quest_range = [str(i) for i in range(1,145)]
