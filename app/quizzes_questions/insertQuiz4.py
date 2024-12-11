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
# Full dataset creation with all 70 questions, difficulty levels, and numbering
quiz_data = {
  "id": "4",
  "questions": [
    {
      "id": "1",
      "question": "1. Select one:",
      "options": [
        "I have been romantic & imaginative",
        "I have been pragmatic & down to earth"
      ]
    },
    {
      "id": "2",
      "question": "2. Select one:",
      "options": [
        "I have tended to take on confrontations",
        "I have tended to avoid confrontations"
      ]
    },
    {
      "id": "3",
      "question": "3. Select one:",
      "options": [
        "I have typically been diplomatic, charming, and ambitious",
        "I have typically been direct, formal, and idealistic"
      ]
    },
    {
      "id": "4",
      "question": "4. Select one:",
      "options": [
        "I have tended to be focused and intense",
        "I have tended to be spontaneous and fun-loving"
      ]
    },
    {
      "id": "5",
      "question": "5. Select one:",
      "options": [
        "I have been a hospitable person and have enjoyed welcoming new friends into my life",
        "I have been a private person and have not mixed much with others"
      ]
    },
    {
      "id": "6",
      "question": "6. Select one:",
      "options": [
        "Generally, it’s been easy to 'get a rise' out of me",
        "Generally, it’s been difficult to 'get a rise' out of me"
      ]
    },
    {
      "id": "7",
      "question": "7. Select one:",
      "options": [
        "I’ve been more of a 'street-smart' survivor",
        "I’ve been more of a 'high-minded' idealist"
      ]
    },
    {
      "id": "8",
      "question": "8. Select one:",
      "options": [
        "I have needed to show affection to people",
        "I have preferred to maintain a certain distance from people"
      ]
    },
    {
      "id": "9",
      "question": "9. Select one:",
      "options": [
        "When presented with a new experience, I’ve usually asked myself if it would be useful to me",
        "When presented with a new experience, I’ve usually asked myself if it would be enjoyable"
      ]
    },
    {
      "id": "10",
      "question": "10. Select one:",
      "options": [
        "I have tended to focus too much on myself",
        "I have tended to focus too much on others"
      ]
    },
    {
      "id": "11",
      "question": "11. Select one:",
      "options": [
        "Others have depended on my insight and knowledge",
        "Others have depended on my strength and decisiveness"
      ]
    },
    {
      "id": "12",
      "question": "12. Select one:",
      "options": [
        "I have come across as being too unsure of myself",
        "I have come across as being too sure of myself"
      ]
    },
    {
      "id": "13",
      "question": "13. Select one:",
      "options": [
        "I have been more relationship-oriented than goal-oriented",
        "I have been more goal-oriented than relationship-oriented"
      ]
    },
    {
      "id": "14",
      "question": "14. Select one:",
      "options": [
        "I have not been able to speak up for myself very well",
        "I have been outspoken—I’ve said what others wished they had the nerve to say"
      ]
    },
    {
      "id": "15",
      "question": "15. Select one:",
      "options": [
        "It’s been difficult for me to stop considering alternatives and do something definite",
        "It’s been difficult for me to take it easy and be more relaxed"
      ]
    },
    {
      "id": "16",
      "question": "16. Select one:",
      "options": [
        "I have tended to be hesitant and procrastinating",
        "I have tended to be bold and domineering"
      ]
    },
    {
      "id": "17",
      "question": "17. Select one:",
      "options": [
        "My reluctance to get too involved has gotten me into trouble with people",
        "My eagerness to have people depend on me has gotten me into trouble with them"
      ]
    },
    {
      "id": "18",
      "question": "18. Select one:",
      "options": [
        "Usually, I have been able to put my feelings aside to get the job done",
        "Usually, I have needed to work through my feelings before I could act"
      ]
    },
    {
      "id": "19",
      "question": "19. Select one:",
      "options": [
        "Generally, I’ve been methodical and cautious",
        "Generally, I’ve been adventurous and taken risks"
      ]
    },
    {
      "id": "20",
      "question": "20. Select one:",
      "options": [
        "I have tended to be a supportive, giving person who enjoys the company of others",
        "I have tended to be a serious, reserved person who likes discussing issues"
      ]
    },
    {
      "id": "21",
      "question": "21. Select one:",
      "options": [
        "I’ve often felt the need to be a 'pillar of strength'",
        "I’ve often felt the need to perform perfectly"
      ]
    },
    {
      "id": "22",
      "question": "22. Select one:",
      "options": [
        "I’ve typically been interested in asking tough questions and maintaining my independence",
        "I’ve typically been interested in maintaining my stability and peace of mind"
      ]
    },
    {
      "id": "23",
      "question": "23. Select one:",
      "options": [
        "I’ve been too hard-nosed and skeptical",
        "I’ve been too soft-hearted and sentimental"
      ]
    },
    {
      "id": "24",
      "question": "24. Select one:",
      "options": [
        "I’ve often worried that I’m missing out on something better",
        "I’ve often worried that, if I let down my guard, someone will take advantage of me"
      ]
    },
    {
      "id": "25",
      "question": "25. Select one:",
      "options": [
        "My habit of being 'stand-offish' has annoyed people",
        "My habit of telling people what to do has annoyed people"
      ]
    },
    {
      "id": "26",
      "question": "26. Select one:",
      "options": [
        "Usually, when troubles have gotten to me, I have been able to 'tune them out'",
        "Usually, when troubles have gotten to me, I have treated myself to something I’ve enjoyed"
      ]
    },
    {
      "id": "27",
      "question": "27. Select one:",
      "options": [
        "I have depended on my friends, and they have known that they can depend on me",
        "I have not depended on people; I have done things on my own"
      ]
    },
    {
      "id": "28",
      "question": "28. Select one:",
      "options": [
        "I have tended to be detached and preoccupied",
        "I have tended to be moody and self-absorbed"
      ]
    },
    {
      "id": "29",
      "question": "29. Select one:",
      "options": [
        "I have liked to challenge people and 'shake them up'",
        "I have liked to comfort people and calm them down"
      ]
    },
    {
      "id": "30",
      "question": "30. Select one:",
      "options": [
        "I have generally been an outgoing, sociable person",
        "I have generally been an earnest, self-disciplined person"
      ]
    },
{
        "id": "31",
        "question": "31. Select One",
        "options": [
          "I’ve usually been shy about showing my abilities",
          "I’ve usually liked to let people know what I can do well"
        ]
      },
      {
        "id": "32",
        "question": "32. Select One",
        "options": [
          "Pursuing my personal interests has been more important to me than having comfort and security",
          "Having comfort and security has been more important to me than pursuing my personal interests"
        ]
      },
      {
        "id": "33",
        "question": "33. Select One",
        "options": [
          "When I’ve had conflicts with others, I’ve tended to withdraw",
          "When I’ve had conflicts with others, I’ve rarely backed down"
        ]
      },
      {
        "id": "34",
        "question": "34. Select One",
        "options": [
          "I have given in too easily and let others push me around",
          "I have been too uncompromising and demanding with others"
        ]
      },
      {
        "id": "35",
        "question": "35. Select One",
        "options": [
          "I’ve been appreciated for my unsinkable spirit and great sense of humor",
          "I’ve been appreciated for my quiet strength and exceptional generosity"
        ]
      },
      {
        "id": "36",
        "question": "36. Select One",
        "options": [
          "Much of my success has been due to my talent for making a favorable impression",
          "Much of my success has been achieved despite my lack of interest in developing 'interpersonal skills'"
        ]
      },
      {
        "id": "37",
        "question": "37. Select One",
        "options": [
          "I’ve prided myself on my perseverance and common sense",
          "I’ve prided myself on my originality and creativity"
        ]
      },
      {
        "id": "38",
        "question": "38. Select One",
        "options": [
          "Basically, I have been easy-going and agreeable",
          "Basically, I have been hard-driving and assertive"
        ]
      },
      {
        "id": "39",
        "question": "39. Select One",
        "options": [
          "I have worked hard to be accepted and well-liked",
          "Being accepted and well-liked has not been a high priority for me"
        ]
      },
      {
        "id": "40",
        "question": "40. Select One",
        "options": [
          "In reaction to pressure from others, I have become more withdrawn",
          "In reaction to pressure from others, I have become more aggressive"
        ]
      },
      {
        "id": "41",
        "question": "41. Select One",
        "options": [
          "People have been interested in me because I’ve been outgoing, engaging, and interested in them",
          "People have been interested in me because I’ve been quiet, unusual, and deep"
        ]
      },
      {
        "id": "42",
        "question": "42. Select One",
        "options": [
          "Duty and responsibility have been important values for me",
          "Harmony and acceptance have been important values for me"
        ]
      },
      {
        "id": "43",
        "question": "43. Select One",
        "options": [
          "I’ve tried to motivate people by making big plans and big promises",
          "I’ve tried to motivate people by pointing out the consequences of not following my advice"
        ]
      },
      {
        "id": "44",
        "question": "44. Select One",
        "options": [
          "I have seldom been emotionally demonstrative",
          "I have often been emotionally demonstrative"
        ]
      },
      {
        "id": "45",
        "question": "45. Select One",
        "options": [
          "Dealing with details has not been one of my strong suits",
          "I have excelled at dealing with details"
        ]
      },
      {
        "id": "46",
        "question": "46. Select One",
        "options": [
          "More often, I have emphasized how different I am from my friends",
          "More often, I have emphasized how much I have in common with my friends"
        ]
      },
      {
        "id": "47",
        "question": "47. Select One",
        "options": [
          "When situations have gotten heated, I have tended to stay on the sidelines",
          "When situations have gotten heated, I have tended to get right into the middle of things"
        ]
      },
      {
        "id": "48",
        "question": "48. Select One",
        "options": [
          "I have stood by my friends, even when they have been wrong",
          "I have not wanted to compromise what is right for friendship"
        ]
      },
      {
        "id": "49",
        "question": "49. Select One",
        "options": [
          "I’ve been a well-meaning supporter",
          "I’ve been a highly-motivated go-getter"
        ]
      },
      {
        "id": "50",
        "question": "50. Select One",
        "options": [
          "When troubled, I have tended to brood about my problems",
          "When troubled, I have tended to find distractions for myself"
        ]
      },
      {
        "id": "51",
        "question": "51. Select One",
        "options": [
          "Generally, I’ve had strong convictions and a sense of how things should be",
          "Generally, I’ve had serious doubts and have questioned how things seemed to be"
        ]
      },
      {
        "id": "52",
        "question": "52. Select One",
        "options": [
          "I’ve created problems with others by being too pessimistic and complaining",
          "I’ve created problems with others by being too bossy and controlling"
        ]
      },
      {
        "id": "53",
        "question": "53. Select One",
        "options": [
          "I have tended to act on my feelings and let the 'chips fall where they may'",
          "I have tended not to act on my feelings lest they stir up more problems"
        ]
      },
      {
        "id": "54",
        "question": "54. Select One",
        "options": [
          "Being the center of attention has usually felt natural to me",
          "Being the center of attention has usually felt strange to me"
        ]
      },
      {
        "id": "55",
        "question": "55. Select One",
        "options": [
          "I’ve been careful and have tried to prepare for unforeseen problems",
          "I’ve been spontaneous and have preferred to improvise as problems come up"
        ]
      },
      {
        "id": "56",
        "question": "56. Select One",
        "options": [
          "I have gotten angry when others have not shown enough appreciation for what I have done for them",
          "I have gotten angry when others have not listened to what I have told them"
        ]
      },
      {
        "id": "57",
        "question": "57. Select One",
        "options": [
          "Being independent and self-reliant has been important to me",
          "Being valued and admired has been important to me"
        ]
      },
      {
        "id": "58",
        "question": "58. Select One",
        "options": [
          "When I’ve debated with friends, I’ve tended to press my arguments forcefully",
          "When I’ve debated with friends, I’ve tended to let things go to prevent hard feelings"
        ]
      },
      {
        "id": "59",
        "question": "59. Select One",
        "options": [
          "I have often been possessive of loved ones—I have had trouble letting them be",
          "I have often 'tested' loved ones to see if they were really there for me"
        ]
      },
      {
        "id": "60",
        "question": "60. Select One",
        "options": [
          "Organizing resources and making things happen has been one of my major strengths",
          "Coming up with new ideas and getting people excited about them has been one of my major strengths"
        ]
      },
{
        "id": "61",
        "question": "61. Select One",
        "options": [
          "I have often felt the need to be a 'pillar of strength'",
          "I have often felt the need to perform perfectly"
        ]
      },
      {
        "id": "62",
        "question": "62. Select One",
        "options": [
          "I have often been a self-absorbed dreamer, lost in my own world",
          "I have often been a driven competitor, relentlessly focused on my goals"
        ]
      },
      {
        "id": "63",
        "question": "63. Select One",
        "options": [
          "When conflicts have come up, I have tended to repress my feelings",
          "When conflicts have come up, I have tended to assert my feelings"
        ]
      },
      {
        "id": "64",
        "question": "64. Select One",
        "options": [
          "I have often been self-conscious and unassertive",
          "I have often been self-confident and assertive"
        ]
      },
      {
        "id": "65",
        "question": "65. Select One",
        "options": [
          "I have tended to keep my relationships intense and somewhat exclusive",
          "I have tended to be more casual and laid-back about my relationships"
        ]
      },
      {
        "id": "66",
        "question": "66. Select One",
        "options": [
          "I have often been focused and intense",
          "I have often been spontaneous and fun-loving"
        ]
      },
      {
        "id": "67",
        "question": "67. Select One",
        "options": [
          "I have tended to value being flexible and free-spirited",
          "I have tended to value being disciplined and industrious"
        ]
      },
      {
        "id": "68",
        "question": "68. Select One",
        "options": [
          "Over the years, my values and lifestyle have changed several times",
          "Over the years, my values and lifestyle have remained fairly consistent"
        ]
      },
      {
        "id": "69",
        "question": "69. Select One",
        "options": [
          "I have often been too direct and outspoken",
          "I have often not spoken up enough"
        ]
      },
      {
        "id": "70",
        "question": "70. Select One",
        "options": [
          "When situations have gotten difficult, I have usually wanted to withdraw",
          "When situations have gotten difficult, I have usually wanted to take charge"
        ]
      },
      {
        "id": "71",
        "question": "71. Select One",
        "options": [
          "Criticism and scolding have affected me deeply",
          "Criticism and scolding have not had much effect on me"
        ]
      },
      {
        "id": "72",
        "question": "72. Select One",
        "options": [
          "I have liked to challenge people and shake them up",
          "I have liked to comfort people and calm them down"
        ]
      },
      {
        "id": "73",
        "question": "73. Select One",
        "options": [
          "I have often been drawn to working on large projects and making big plans",
          "I have often been drawn to exploring the depths of my own psyche"
        ]
      },
      {
        "id": "74",
        "question": "74. Select One",
        "options": [
          "I have usually been shy about taking the initiative with people",
          "I have usually been bold about taking the initiative with people"
        ]
      },
      {
        "id": "75",
        "question": "75. Select One",
        "options": [
          "I have been attracted to ambitious people who are doing impressive things",
          "I have been attracted to caring people who show depth and sensitivity"
        ]
      },
      {
        "id": "76",
        "question": "76. Select One",
        "options": [
          "In most situations, I have needed to believe in something",
          "In most situations, I have needed to do something"
        ]
      },
      {
        "id": "77",
        "question": "77. Select One",
        "options": [
          "I have rarely worried much about what I was doing",
          "I have often worried about what I was doing"
        ]
      },
      {
        "id": "78",
        "question": "78. Select One",
        "options": [
          "I have been independent and somewhat private",
          "I have been outgoing and enthusiastic"
        ]
      },
      {
        "id": "79",
        "question": "79. Select One",
        "options": [
          "I have tried hard to make the people in my life feel valued",
          "I have tried hard to get the people in my life to take care of themselves"
        ]
      },
      {
        "id": "80",
        "question": "80. Select One",
        "options": [
          "I have tended to dwell on my mistakes and bad feelings",
          "I have tended to move on from my mistakes and bad feelings"
        ]
      },
      {
        "id": "81",
        "question": "81. Select One",
        "options": [
          "When I’ve had conflicts with others, I have often been the one to hold firm",
          "When I’ve had conflicts with others, I have often been the one to give in"
        ]
      },
      {
        "id": "82",
        "question": "82. Select One",
        "options": [
          "In my personal relationships, I have wanted to build on regular contact and shared activities",
          "In my personal relationships, I have wanted to build on quiet trust and mutual respect"
        ]
      },
      {
        "id": "83",
        "question": "83. Select One",
        "options": [
          "I have generally been an outgoing, sociable person",
          "I have generally been an earnest, self-disciplined person"
        ]
      },
      {
        "id": "84",
        "question": "84. Select One",
        "options": [
          "I have tended to value logic and reason over feelings and impulses",
          "I have tended to value feelings and impulses over logic and reason"
        ]
      },
      {
        "id": "85",
        "question": "85. Select One",
        "options": [
          "I have often been drawn to fast-paced, exciting situations",
          "I have often been drawn to calm, quiet settings"
        ]
      },
      {
        "id": "86",
        "question": "86. Select One",
        "options": [
          "I have often felt the need to keep people at a distance",
          "I have often felt the need to win people over"
        ]
      },
      {
        "id": "87",
        "question": "87. Select One",
        "options": [
          "I have often been meticulous and methodical",
          "I have often been easy-going and adaptable"
        ]
      },
      {
        "id": "88",
        "question": "88. Select One",
        "options": [
          "I have often taken pride in my powerful imagination",
          "I have often taken pride in my reliable practicality"
        ]
      },
      {
        "id": "89",
        "question": "89. Select One",
        "options": [
          "When I’ve needed to confront people, I have tended to get quite emotional",
          "When I’ve needed to confront people, I have tended to stay calm and collected"
        ]
      },
      {
        "id": "90",
        "question": "90. Select One",
        "options": [
          "I have usually been proud of my uniqueness and differentness",
          "I have usually been proud of my stability and dependability"
        ]
      },
{
        "id": "91",
        "question": "91. Select One",
        "options": [
          "I have been drawn to situations that are exciting and unpredictable",
          "I have been drawn to situations that are safe and familiar"
        ]
      },
      {
        "id": "92",
        "question": "92. Select One",
        "options": [
          "I have often tried to motivate others by inspiring them",
          "I have often tried to motivate others by persuading them"
        ]
      },
      {
        "id": "93",
        "question": "93. Select One",
        "options": [
          "I have tended to be fair and objective",
          "I have tended to be emotional and idealistic"
        ]
      },
      {
        "id": "94",
        "question": "94. Select One",
        "options": [
          "I have had difficulty setting boundaries in relationships",
          "I have had difficulty opening up in relationships"
        ]
      },
      {
        "id": "95",
        "question": "95. Select One",
        "options": [
          "I have been more relationship-oriented than goal-oriented",
          "I have been more goal-oriented than relationship-oriented"
        ]
      },
      {
        "id": "96",
        "question": "96. Select One",
        "options": [
          "I have often pushed myself too hard to achieve success",
          "I have often held myself back from achieving success"
        ]
      },
      {
        "id": "97",
        "question": "97. Select One",
        "options": [
          "I have usually been good at managing my time and responsibilities",
          "I have usually struggled with managing my time and responsibilities"
        ]
      },
      {
        "id": "98",
        "question": "98. Select One",
        "options": [
          "I have often enjoyed working in groups or teams",
          "I have often enjoyed working alone or independently"
        ]
      },
      {
        "id": "99",
        "question": "99. Select One",
        "options": [
          "I have frequently been intrigued by abstract ideas and theories",
          "I have frequently been focused on practical applications"
        ]
      },
      {
        "id": "100",
        "question": "100. Select One",
        "options": [
          "I have usually preferred to go with the flow",
          "I have usually preferred to follow a plan"
        ]
      },
      {
        "id": "101",
        "question": "101. Select One",
        "options": [
          "I have tended to focus more on my strengths and abilities",
          "I have tended to focus more on my challenges and limitations"
        ]
      },
      {
        "id": "102",
        "question": "102. Select One",
        "options": [
          "I have been drawn to opportunities to lead or direct others",
          "I have been drawn to opportunities to support or assist others"
        ]
      },
      {
        "id": "103",
        "question": "103. Select One",
        "options": [
          "I have tended to be introspective and reflective",
          "I have tended to be action-oriented and proactive"
        ]
      },
      {
        "id": "104",
        "question": "104. Select One",
        "options": [
          "I have sought out new and stimulating experiences",
          "I have sought out stability and predictability"
        ]
      },
      {
        "id": "105",
        "question": "105. Select One",
        "options": [
          "I have often avoided taking risks",
          "I have often embraced taking risks"
        ]
      },
      {
        "id": "106",
        "question": "106. Select One",
        "options": [
          "I have usually taken my commitments seriously",
          "I have sometimes struggled to honor my commitments"
        ]
      },
      {
        "id": "107",
        "question": "107. Select One",
        "options": [
          "I have often preferred to analyze situations before acting",
          "I have often preferred to act on my instincts"
        ]
      },
      {
        "id": "108",
        "question": "108. Select One",
        "options": [
          "I have been comfortable with change and uncertainty",
          "I have preferred stability and predictability"
        ]
      },
      {
        "id": "109",
        "question": "109. Select One",
        "options": [
          "I have often felt driven to excel and succeed",
          "I have often felt content with simplicity and balance"
        ]
      },
      {
        "id": "110",
        "question": "110. Select One",
        "options": [
          "I have tended to approach problems creatively",
          "I have tended to approach problems practically"
        ]
      },
      {
        "id": "111",
        "question": "111. Select One",
        "options": [
          "I have been someone who prioritizes harmony in relationships",
          "I have been someone who prioritizes honesty in relationships"
        ]
      },
      {
        "id": "112",
        "question": "112. Select One",
        "options": [
          "I have often enjoyed exploring my inner world of thoughts and feelings",
          "I have often enjoyed engaging with the external world of activities and people"
        ]
      },
      {
        "id": "113",
        "question": "113. Select One",
        "options": [
          "I have been good at managing conflicts and resolving issues",
          "I have tended to avoid conflicts and leave issues unresolved"
        ]
      },
      {
        "id": "114",
        "question": "114. Select One",
        "options": [
          "I have often focused on what is missing or could be improved",
          "I have often focused on what is working well and should be maintained"
        ]
      },
      {
        "id": "115",
        "question": "115. Select One",
        "options": [
          "I have been drawn to leadership and guiding others",
          "I have been drawn to creative or supportive roles"
        ]
      },
      {
        "id": "116",
        "question": "116. Select One",
        "options": [
          "I have often relied on detailed planning and organization",
          "I have often relied on flexibility and adaptability"
        ]
      },
      {
        "id": "117",
        "question": "117. Select One",
        "options": [
          "I have preferred to take things step-by-step",
          "I have preferred to jump into things headfirst"
        ]
      },
      {
        "id": "118",
        "question": "118. Select One",
        "options": [
          "I have been motivated by a sense of duty and responsibility",
          "I have been motivated by a sense of curiosity and exploration"
        ]
      },
      {
        "id": "119",
        "question": "119. Select One",
        "options": [
          "I have often felt comfortable following established norms and expectations",
          "I have often felt comfortable challenging established norms and expectations"
        ]
      },
      {
        "id": "120",
        "question": "120. Select One",
        "options": [
          "I have often been motivated by the desire to make an impact",
          "I have often been motivated by the desire to enjoy life"
        ]
      },
{
        "id": "121",
        "question": "121. Select One",
        "options": [
          "I have been interested in understanding how systems work",
          "I have been interested in understanding how people work"
        ]
      },
      {
        "id": "122",
        "question": "122. Select One",
        "options": [
          "I have often been excited by novelty and change",
          "I have often preferred routine and familiarity"
        ]
      },
      {
        "id": "123",
        "question": "123. Select One",
        "options": [
          "I have enjoyed facing challenges head-on",
          "I have enjoyed analyzing challenges before taking action"
        ]
      },
      {
        "id": "124",
        "question": "124. Select One",
        "options": [
          "I have been motivated by the pursuit of success and achievement",
          "I have been motivated by the pursuit of personal growth and learning"
        ]
      },
      {
        "id": "125",
        "question": "125. Select One",
        "options": [
          "I have been someone who values independence and autonomy",
          "I have been someone who values collaboration and teamwork"
        ]
      },
      {
        "id": "126",
        "question": "126. Select One",
        "options": [
          "I have been quick to make decisions based on logic and reasoning",
          "I have been quick to make decisions based on my feelings and intuition"
        ]
      },
      {
        "id": "127",
        "question": "127. Select One",
        "options": [
          "I have often been focused on the long-term vision",
          "I have often been focused on immediate results"
        ]
      },
      {
        "id": "128",
        "question": "128. Select One",
        "options": [
          "I have been comfortable taking on leadership roles",
          "I have been comfortable taking on supporting roles"
        ]
      },
      {
        "id": "129",
        "question": "129. Select One",
        "options": [
          "I have often focused on the emotional side of situations",
          "I have often focused on the practical side of situations"
        ]
      },
      {
        "id": "130",
        "question": "130. Select One",
        "options": [
          "I have found it easy to adapt to new circumstances",
          "I have found it difficult to adapt to new circumstances"
        ]
      },
      {
        "id": "131",
        "question": "131. Select One",
        "options": [
          "I have often been excited by the unknown and the unexpected",
          "I have often felt uneasy about the unknown and the unexpected"
        ]
      },
      {
        "id": "132",
        "question": "132. Select One",
        "options": [
          "I have usually been the one to initiate conversations",
          "I have usually waited for others to initiate conversations"
        ]
      },
      {
        "id": "133",
        "question": "133. Select One",
        "options": [
          "I have tended to value results more than processes",
          "I have tended to value processes more than results"
        ]
      },
      {
        "id": "134",
        "question": "134. Select One",
        "options": [
          "I have been someone who values harmony over conflict",
          "I have been someone who values honesty over harmony"
        ]
      },
      {
        "id": "135",
        "question": "135. Select One",
        "options": [
          "I have often been more interested in ideas than in people",
          "I have often been more interested in people than in ideas"
        ]
      },
      {
        "id": "136",
        "question": "136. Select One",
        "options": [
          "I have often felt energized by social interactions",
          "I have often felt drained by social interactions"
        ]
      },
      {
        "id": "137",
        "question": "137. Select One",
        "options": [
          "I have often preferred to work in a structured, organized environment",
          "I have often preferred to work in a flexible, spontaneous environment"
        ]
      },
      {
        "id": "138",
        "question": "138. Select One",
        "options": [
          "I have tended to avoid making decisions until I have all the facts",
          "I have tended to make decisions quickly, even with limited information"
        ]
      },
      {
        "id": "139",
        "question": "139. Select One",
        "options": [
          "I have been more focused on achieving my goals than on the process",
          "I have been more focused on the process than on achieving my goals"
        ]
      },
      {
        "id": "140",
        "question": "140. Select One",
        "options": [
          "I have preferred to follow the rules and established procedures",
          "I have preferred to bend or break the rules to achieve my goals"
        ]
      },
      {
        "id": "141",
        "question": "141. Select One",
        "options": [
          "I have often been the one to take charge in situations",
          "I have often preferred to follow others' lead in situations"
        ]
      },
      {
        "id": "142",
        "question": "142. Select One",
        "options": [
          "I have often found it difficult to set boundaries with others",
          "I have often found it easy to set boundaries with others"
        ]
      },
      {
        "id": "143",
        "question": "143. Select One",
        "options": [
          "I have often enjoyed solving problems by thinking outside the box",
          "I have often enjoyed solving problems by using established methods"
        ]
      },
      {
        "id": "144",
        "question": "144. Select One",
        "options": [
          "I have tended to be more focused on the present moment",
          "I have tended to be more focused on the future"
        ]
      }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizes.insert_one(quiz_data)
