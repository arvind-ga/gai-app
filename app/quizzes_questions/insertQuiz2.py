import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

# from dotenv import load_dotenv
# load_dotenv()  # loading environment variables
#
# MONGODB_USER = os.getenv("mongodb_username")
# MONGODB_PASS = os.getenv("mongodb_password")
# MONGODB_SERVER = os.getenv("mongodb_server")
# MONGODB_PORT = os.getenv("mongodb_port")
# MONGODB_CONNECTION_STRING1 = f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_SERVER}:{MONGODB_PORT}/fastapi_db?authSource=admin&authMechanism=SCRAM-SHA-256"
# print("MONGODB_CONNECTION_STRING::", MONGODB_CONNECTION_STRING1)
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
        print("Connection to MongoDB failed")

####################### Update quiz_data here ##################
quiz_data = {
    "id": "2",
    "questions": [
      {
        "id": "1",
        "question": "1. Select the word which is opposite in meaning to the given word: Optimistic.",
        "options": ["Hopeful", "Pessimistic", "Positive", "Confident"],
        "answer": "Pessimistic",
        "segment": "verbal"
      },
      {
        "id": "2",
        "question": "2. Find the missing term in the series: A, D, G, J, ?",
        "options": ["K", "M", "N", "P"],
        "answer": "M",
        "segment": "verbal"
      },
      {
        "id": "3",
        "question": "3. Identify the relationship between the given pair and choose the pair with the same relationship: Pen: Write :: Knife : ?",
        "options": ["Sharp", "Cut", "Point", "Break"],
        "answer": "Cut",
        "segment": "verbal"
      },
      {
        "id": "4",
        "question": "4. Choose the correct synonym for the word in capital letters: OBSTINATE.",
        "options": ["Flexible", "Stubborn", "Humble", "Friendly"],
        "answer": "Stubborn",
        "segment": "verbal"
      },
      {
        "id": "5",
        "question": "5. Complete the analogy: Lion: Roar :: Snake : ?",
        "options": ["Hiss", "Buzz", "Bark", "Chirp"],
        "answer": "Hiss",
        "segment": "verbal"
      },
      {
        "id": "6",
        "question": "6. Choose the option that best completes the sentence: If I were rich, I __________ travel the world.",
        "options": ["will", "would", "could", "should"],
        "answer": "would",
        "segment": "verbal"
      },
      {
        "id": "7",
        "question": "7. Find the odd one out: Horse, Cow, Dog, Whale.",
        "options": ["Horse", "Cow", "Dog", "Whale"],
        "answer": "Whale",
        "segment": "verbal"
      },
      {
        "id": "8",
        "question": "8. Identify the grammatically correct sentence.",
        "options": [
          "She don’t likes pizza.",
          "She doesn’t like pizza.",
          "She didn’t liked pizza.",
          "She don’t like pizza."
        ],
        "answer": "She doesn’t like pizza.",
        "segment": "verbal"
      },
      {
        "id": "9",
        "question": "9. Which of the following words is misspelled?",
        "options": ["Accommodate", "Embarrass", "Comitee", "Necessary"],
        "answer": "Comitee",
        "segment": "verbal"
      },
      {
        "id": "10",
        "question": "10. Rearrange the following words to form a meaningful sentence: given / a / was / the / prize / winner / the / to.",
        "options": [
          "The winner was given a prize.",
          "A prize was given to the winner.",
          "The winner to a prize was given.",
          "A and B both are correct."
        ],
        "answer": "A and B both are correct.",
        "segment": "verbal"
      },
      {
        "id": "11",
        "question": "11. Find the missing number in the sequence: 2, 6, 12, 20, ?",
        "options": ["30", "36", "28", "26"],
        "answer": "30",
        "segment": "logical"
      },
      {
        "id": "12",
        "question": "12. Complete the analogy: Book : Read :: Knife : ?",
        "options": ["Write", "Cut", "Cook", "Sharpen"],
        "answer": "Cut",
        "segment": "logical"
      },
      {
        "id": "13",
        "question": "13. Identify the odd one out: Apple, Orange, Banana, Carrot.",
        "options": ["Apple", "Orange", "Banana", "Carrot"],
        "answer": "Carrot",
        "segment": "logical"
      },
      {
        "id": "14",
        "question": "14. If the code for CAT is DBU, what is the code for DOG?",
        "options": ["DPH", "EPH", "FPH", "EPI"],
        "answer": "EPH",
        "segment": "logical"
      },
      {
        "id": "15",
        "question": "15. Which word does not belong to the group: Rectangle, Triangle, Circle, Pentagon?",
        "options": ["Rectangle", "Triangle", "Circle", "Pentagon"],
        "answer": "Circle",
        "segment": "logical"
      },
      {
        "id": "16",
        "question": "16. Select the option that continues the pattern: AB, CD, EF, GH, ?",
        "options": ["IJ", "HI", "JK", "LM"],
        "answer": "IJ",
        "segment": "logical"
      },
      {
        "id": "17",
        "question": "17. In a certain code language, if PAPER is coded as OBOFS, what is the code for PENCIL?",
        "options": ["ODMBJM", "QDMCPJ", "OEDNIM", "ODNBOJ"],
        "answer": "ODMBJM",
        "segment": "logical"
      },
      {
        "id": "18",
        "question": "18. Which of the following numbers is divisible by 3: 25, 33, 19, 22?",
        "options": ["25", "33", "19", "22"],
        "answer": "33",
        "segment": "logical"
      },
      {
        "id": "19",
        "question": "19. If all BLOOD is RED and all RED is COLOR, what can we infer?",
        "options": [
          "All COLOR is BLOOD",
          "All RED is BLOOD",
          "All BLOOD is COLOR",
          "None of the above"
        ],
        "answer": "All BLOOD is COLOR",
        "segment": "logical"
      },
      {
        "id": "20",
        "question": "20. Rearrange the letters to form a meaningful word: GOLRITHM.",
        "options": [
          "GIRLTHOM",
          "LITROGMH",
          "ALGORITHM",
          "GRILHTOM"
        ],
        "answer": "ALGORITHM",
        "segment": "logical"
      },
      {
        "id": "21",
        "question": "21. You notice a classmate is being bullied during lunch. What would you do?",
        "options": [
          "Ignore it and stay out of the situation.",
          "Join in with the bully.",
          "Stand up for the classmate and report the bully to a teacher.",
          "Film the incident and post it on social media."
        ],
        "answer": "Stand up for the classmate and report the bully to a teacher.",
        "segment": "situation"
      },
      {
        "id": "22",
        "question": "22. During a group project, one of your teammates is not contributing. What is the best way to handle the situation?",
        "options": [
          "Complain about the person to the teacher.",
          "Finish the work without them.",
          "Speak to them politely and encourage them to participate.",
          "Blame them in front of the group."
        ],
        "answer": "Speak to them politely and encourage them to participate.",
        "segment": "situation"
      },
      {
        "id": "23",
        "question": "23. You see someone accidentally drop money on the floor and walk away. What should you do?",
        "options": [
          "Keep the money for yourself.",
          "Leave it there and walk away.",
          "Pick it up and give it to the person.",
          "Show it to your friends and ask what to do."
        ],
        "answer": "Pick it up and give it to the person.",
        "segment": "situation"
      },
      {
        "id": "24",
        "question": "24. You are preparing for an important exam but your friends invite you to a party the night before. What is the best option?",
        "options": [
          "Go to the party and study after.",
          "Skip studying and go to the party.",
          "Politely decline the invitation and focus on studying.",
          "Go to the party and wake up early to study."
        ],
        "answer": "26. Politely decline the invitation and focus on studying.",
        "segment": "situation"
      },
      {
        "id": "25",
        "question": "25. You are working on a project and your friend copies your work without your permission. What would you do?",
        "options": [
          "Confront them angrily.",
          "Tell the teacher immediately.",
          "Calmly ask them why they copied and resolve the issue together.",
          "Do nothing and ignore it."
        ],
        "answer": "Calmly ask them why they copied and resolve the issue together.",
        "segment": "situation"
      },
      {
        "id": "26",
        "question": "26. If the opposite of 'Always' is 'Never', what is the opposite of 'Success'?",
        "options": ["Failure", "Loss", "Defeat", "Mistake"],
        "answer": "Failure",
        "segment": "situation"
      },
      {
        "id": "27",
        "question": "27. What comes next in the series: 5, 10, 20, 40, ?",
        "options": ["50", "60", "80", "100"],
        "answer": "80",
        "segment": "situation"
      },
      {
        "id": "28",
        "question": "28. Rearrange the following letters to form a country: A, I, N, D, A.",
        "options": ["India", "China", "Japan", "Nepal"],
        "answer": "India",
        "segment": "situation"
      },
      {
        "id": "29",
        "question": "29. Which of these is NOT a primary color?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "Green",
        "segment": "situation"
      },
      {
        "id": "30",
        "question": "30. Which is the next number in this Fibonacci series: 1, 1, 2, 3, 5, 8, ?",
        "options": ["10", "11", "13", "14"],
        "answer": "13",
        "segment": "situation"
      },
    {
      "id": "31",
      "question": "31. I actively listen to other perspectives and seek to understand them during conflicts.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Conflict Management"
    },
    {
      "id": "32",
      "question": "32. I work towards a solution in conflicts that respects everyone’s needs.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Conflict Management"
    },
    {
      "id": "33",
      "question": "33. I can easily sense others' feelings and imagine what they might be going through.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Empathy"
    },
    {
      "id": "34",
      "question": "34. I express understanding and provide emotional support when someone shares their problems with me.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Empathy"
    },
    {
      "id": "35",
      "question": "35. I often take initiatives that benefit other people or the community.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Pro Social Behavior"
    },
    {
      "id": "36",
      "question": "36. I willingly share my resources with others who might need them, even if I receive nothing in return.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Pro Social Behavior"
    },
    {
      "id": "37",
      "question": "37. I can maintain my composure and think clearly even when under significant emotional stress.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Regulation"
    },
    {
      "id": "38",
      "question": "38. I use strategies (like deep breathing, taking a break, etc.) to manage my emotions effectively.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Regulation"
    },
    {
      "id": "39",
      "question": "39. I am aware of my emotions as they arise and understand how they affect my behavior.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Self-Awareness"
    },
    {
      "id": "40",
      "question": "40. I can pinpoint the specific factors that trigger different emotional responses in me.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Self-Awareness"
    },
    {
      "id": "41",
      "question": "41, I feel confident in my ability to handle my emotional responses in various situations.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Self-Efficacy"
    },
    {
      "id": "42",
      "question": "42. I believe in my capacity to manage difficult emotional situations and regain my stability.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Emotional Self-Efficacy"
    },
    {
      "id": "43",
      "question": "43. I am self-motivated to pursue my goals, regardless of minor setbacks.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Motivation"
    },
    {
      "id": "44",
      "question": "44. I consistently seek out new challenges and opportunities for growth and learning.",
      "options" : [
				"1",
				"2",
				"3",
				"4",
				"5"
			],
      "answer": "",
      "segment": "Motivation"
    }
    ]
}


###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizes.insert_one(quiz_data)
