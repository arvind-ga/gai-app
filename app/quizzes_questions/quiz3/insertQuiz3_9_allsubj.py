import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv
load_dotenv()  # loading environment variables
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")

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
  "id": "3_9_allsubj",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. What is the SI unit of force?",
      "options": ["Newton", "Joule", "Pascal", "Watt"],
      "answer": "Newton",
      "segment": "Physics"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. Which law states that every action has an equal and opposite reaction?",
      "options": [
        "Newton's First Law",
        "Newton's Second Law",
        "Newton's Third Law",
        "Law of Gravitation"
      ],
      "answer": "Newton's Third Law",
      "segment": "Physics"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What is the acceleration due to gravity on Earth?",
      "options": ["9.8 m/s²", "5 m/s²", "10 m/s²", "12 m/s²"],
      "answer": "9.8 m/s²",
      "segment": "Physics"
    },
    {
      "id": 4,
      "difficulty": "Medium",
      "question": "4. What is the formula for calculating work done?",
      "options": [
        "Work = Force × Distance",
        "Work = Mass × Velocity",
        "Work = Force × Time",
        "Work = Energy × Time"
      ],
      "answer": "Work = Force × Distance",
      "segment": "Physics"
    },
    {
      "id": 5,
      "difficulty": "Medium",
      "question": "5. Which of these is a scalar quantity?",
      "options": ["Velocity", "Force", "Acceleration", "Speed"],
      "answer": "Speed",
      "segment": "Physics"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. What is the power of a machine that does 100 Joules of work in 2 seconds?",
      "options": ["50 Watts", "200 Watts", "100 Watts", "20 Watts"],
      "answer": "50 Watts",
      "segment": "Physics"
    },
    {
      "id": 7,
      "difficulty": "Hard",
      "question": "7. Which phenomenon explains the bending of light when it passes from one medium to another?",
      "options": ["Reflection", "Refraction", "Diffraction", "Dispersion"],
      "answer": "Refraction",
      "segment": "Physics"
    },
    {
      "id": 8,
      "difficulty": "Hard",
      "question": "8. What is the relationship between pressure, force, and area?",
      "options": [
        "Pressure = Force × Area",
        "Pressure = Force / Area",
        "Pressure = Area / Force",
        "Pressure = Force × Volume"
      ],
      "answer": "Pressure = Force / Area",
      "segment": "Physics"
    },
    {
      "id": 9,
      "difficulty": "Hard",
      "question": "9. Which type of mirror is used in a car's rearview mirror?",
      "options": ["Plane mirror", "Concave mirror", "Convex mirror", "Spherical mirror"],
      "answer": "Convex mirror",
      "segment": "Physics"
    },
    {
      "id": 10,
      "difficulty": "Easy",
      "question": "10. Which of the following is a chemical change?",
      "options": [
        "Melting of ice",
        "Burning of paper",
        "Boiling of water",
        "Breaking of glass"
      ],
      "answer": "Burning of paper",
      "segment": "Chemistry"
    },
    {
      "id": 11,
      "difficulty": "Easy",
      "question": "11. What is the chemical symbol for water?",
      "options": ["H2", "O2", "H2O", "CO2"],
      "answer": "H2O",
      "segment": "Chemistry"
    },
    {
      "id": 12,
      "difficulty": "Easy",
      "question": "12. Which gas is known as the 'laughing gas'?",
      "options": ["Oxygen", "Nitrogen", "Nitrous oxide", "Carbon dioxide"],
      "answer": "Nitrous oxide",
      "segment": "Chemistry"
    },
    {
      "id": 13,
      "difficulty": "Medium",
      "question": "13. What is the pH value of a neutral solution?",
      "options": ["0", "7", "14", "10"],
      "answer": "7",
      "segment": "Chemistry"
    },
    {
      "id": 14,
      "difficulty": "Medium",
      "question": "14. Which element is most abundant in the Earth's crust?",
      "options": ["Iron", "Oxygen", "Silicon", "Aluminum"],
      "answer": "Oxygen",
      "segment": "Chemistry"
    },
    {
      "id": 15,
      "difficulty": "Medium",
      "question": "15. What type of bond is present in NaCl (table salt)?",
      "options": [
        "Covalent bond",
        "Ionic bond",
        "Metallic bond",
        "Hydrogen bond"
      ],
      "answer": "Ionic bond",
      "segment": "Chemistry"
    },
    {
      "id": 16,
      "difficulty": "Hard",
      "question": "16. What is the name of the process in which a gas changes to a liquid?",
      "options": ["Sublimation", "Condensation", "Evaporation", "Freezing"],
      "answer": "Condensation",
      "segment": "Chemistry"
    },
    {
      "id": 17,
      "difficulty": "Hard",
      "question": "17. Which law states that mass cannot be created or destroyed in a chemical reaction?",
      "options": [
        "Law of Multiple Proportions",
        "Law of Conservation of Mass",
        "Law of Constant Composition",
        "Avogadro's Law"
      ],
      "answer": "Law of Conservation of Mass",
      "segment": "Chemistry"
    },
    {
      "id": 18,
      "difficulty": "Hard",
      "question": "18. Which is the main constituent of biogas?",
      "options": ["Methane", "Ethane", "Propane", "Butane"],
      "answer": "Methane",
      "segment": "Chemistry"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. Which part of the cell is known as the 'powerhouse'?",
      "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
      "answer": "Mitochondria",
      "segment": "Bio"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. What is the functional unit of the kidney?",
      "options": ["Neuron", "Nephron", "Alveoli", "Villi"],
      "answer": "Nephron",
      "segment": "Bio"
    },
    {
      "id": 21,
      "difficulty": "Easy",
      "question": "21. What is the process by which green plants make their food?",
      "options": ["Respiration", "Digestion", "Photosynthesis", "Fermentation"],
      "answer": "Photosynthesis",
      "segment": "Bio"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. Which blood group is known as the universal donor?",
      "options": ["A", "B", "AB", "O"],
      "answer": "O",
      "segment": "Bio"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. Which organ is responsible for producing insulin?",
      "options": ["Liver", "Pancreas", "Stomach", "Intestines"],
      "answer": "Pancreas",
      "segment": "Bio"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What is the main component of the xylem tissue?",
      "options": ["Phloem", "Tracheids", "Chlorophyll", "Cuticle"],
      "answer": "Tracheids",
      "segment": "Bio"
    },
    {
      "id": 25,
      "difficulty": "Hard",
      "question": "25. Which gas is released during the process of photosynthesis?",
      "options": ["Carbon dioxide", "Nitrogen", "Oxygen", "Methane"],
      "answer": "Oxygen",
      "segment": "Bio"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. What is the scientific term for the study of heredity?",
      "options": ["Biochemistry", "Genetics", "Cytology", "Ecology"],
      "answer": "Genetics",
      "segment": "Bio"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which part of the brain controls voluntary actions?",
      "options": ["Cerebellum", "Medulla", "Cerebrum", "Pons"],
      "answer": "Cerebrum",
      "segment": "Bio"
    },
    {
      "id": 28,
      "difficulty": "Easy",
      "question": "28. What is the value of π (pi) approximately?",
      "options": ["3.12", "3.14", "3.16", "3.18"],
      "answer": "3.14",
      "segment": "Maths"
    },
    {
      "id": 29,
      "difficulty": "Easy",
      "question": "29. What is the area of a rectangle with length 5 cm and breadth 3 cm?",
      "options": ["15 cm²", "8 cm²", "10 cm²", "20 cm²"],
      "answer": "15 cm²",
      "segment": "Maths"
    },
    {
      "id": 30,
      "difficulty": "Easy",
      "question": "30. What is the square of 7?",
      "options": ["49", "14", "21", "28"],
      "answer": "49",
      "segment": "Maths"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the sum of the angles in a triangle?",
      "options": ["180°", "360°", "90°", "270°"],
      "answer": "180°",
      "segment": "Maths"
    },
    {
      "id": 32,
      "difficulty": "Medium",
      "question": "32. Solve for x: 2x + 5 = 15.",
      "options": ["x = 5", "x = 10", "x = 15", "x = 20"],
      "answer": "x = 5",
      "segment": "Maths"
    },
    {
      "id": 33,
      "difficulty": "Medium",
      "question": "33. What is the cube root of 64?",
      "options": ["2", "3", "4", "8"],
      "answer": "4",
      "segment": "Maths"
    },
    {
      "id": 34,
      "difficulty": "Medium",
      "question": "34. What is the value of 5² + 6²?",
      "options": ["61", "49", "55", "50"],
      "answer": "61",
      "segment": "Maths"
    },
    {
      "id": 35,
      "difficulty": "Medium",
      "question": "35. Which of the following is a Pythagorean triplet?",
      "options": [
        "3, 4, 5",
        "5, 6, 7",
        "8, 15, 18",
        "2, 3, 4"
      ],
      "answer": "3, 4, 5",
      "segment": "Maths"
    },
    {
      "id": 36,
      "difficulty": "Hard",
      "question": "36. Solve for x: 3x - 7 = 2x + 9.",
      "options": ["x = 16", "x = -16", "x = 7", "x = -7"],
      "answer": "x = 16",
      "segment": "Maths"
    },
    {
      "id": 37,
      "difficulty": "Hard",
      "question": "37. What is the value of (2x² + 3x - 2) when x = -1?",
      "options": ["3", "-3", "0", "1"],
      "answer": "0",
      "segment": "Maths"
    },
    {
      "id": 38,
      "difficulty": "Hard",
      "question": "38. If a = 3 and b = 4, find the value of √(a² + b²).",
      "options": ["7", "5", "25", "9"],
      "answer": "5",
      "segment": "Maths"
    },
    {
      "id": 39,
      "difficulty": "Hard",
      "question": "39. What is the sum of the first 10 natural numbers?",
      "options": ["45", "55", "60", "50"],
      "answer": "55",
      "segment": "Maths"
    },
    {
      "id": 40,
      "difficulty": "Easy",
      "question": "40. What does CPU stand for?",
      "options": ["Central Processing Unit", "Computer Processing Unit", "Central Programming Unit", "Computer Programming Unit"],
      "answer": "Central Processing Unit",
      "segment": "Computer"
    },
    {
      "id": 41,
      "difficulty": "Easy",
      "question": "41. Which of the following is an example of an input device?",
      "options": ["Monitor", "Printer", "Keyboard", "Speaker"],
      "answer": "Keyboard",
      "segment": "Computer"
    },
    {
      "id": 42,
      "difficulty": "Easy",
      "question": "42. What is the full form of HTML?",
      "options": ["HyperText Markup Language", "HyperText Markdown Language", "HighText Markup Language", "HyperTool Markup Language"],
      "answer": "HyperText Markup Language",
      "segment": "Computer"
    },
    {
      "id": 43,
      "difficulty": "Easy",
      "question": "43. Which key is used to create a new line in a word processor?",
      "options": ["Ctrl", "Shift", "Enter", "Alt"],
      "answer": "Enter",
      "segment": "Computer"
    },
    {
      "id": 44,
      "difficulty": "Medium",
      "question": "44. What is the function of an operating system?",
      "options": ["Manages hardware and software resources", "Compiles code", "Acts as an input device", "Stores data permanently"],
      "answer": "Manages hardware and software resources",
      "segment": "Computer"
    },
    {
      "id": 45,
      "difficulty": "Medium",
      "question": "45. Which of the following is a secondary storage device?",
      "options": ["RAM", "ROM", "Hard Disk", "Cache"],
      "answer": "Hard Disk",
      "segment": "Computer"
    },
    {
      "id": 46,
      "difficulty": "Medium",
      "question": "46. What is the binary equivalent of the decimal number 5?",
      "options": ["101", "110", "111", "100"],
      "answer": "101",
      "segment": "Computer"
    },
    {
      "id": 47,
      "difficulty": "Medium",
      "question": "47. Which language is known as the 'mother of programming languages'?",
      "options": ["Python", "C", "Java", "Assembly"],
      "answer": "C",
      "segment": "Computer"
    },
    {
      "id": 48,
      "difficulty": "Hard",
      "question": "48. What does DNS stand for in computer networks?",
      "options": ["Data Network Service", "Domain Name System", "Digital Network Security", "Domain Network Service"],
      "answer": "Domain Name System",
      "segment": "Computer"
    },
    {
      "id": 49,
      "difficulty": "Hard",
      "question": "49. Which sorting algorithm has the best average case time complexity?",
      "options": ["Bubble Sort", "Merge Sort", "Insertion Sort", "Selection Sort"],
      "answer": "Merge Sort",
      "segment": "Computer"
    },
    {
      "id": 50,
      "difficulty": "Hard",
      "question": "50. What is the purpose of the 'ping' command?",
      "options": ["To test network connectivity", "To download files", "To encrypt data", "To configure IP addresses"],
      "answer": "To test network connectivity",
      "segment": "Computer"
    },
    {
      "id": 51,
      "difficulty": "Hard",
      "question": "51. Which protocol is used for secure communication over the internet?",
      "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
      "answer": "HTTPS",
      "segment": "Computer"
    },
      {
      "id": 52,
      "difficulty": "Easy",
      "question": "52. Which is a synonym of 'happy'?",
      "options": ["Sad", "Joyful", "Angry", "Bored"],
      "answer": "Joyful",
      "segment": "English"
    },
    {
      "id": 53,
      "difficulty": "Easy",
      "question": "53. What is the plural form of 'child'?",
      "options": ["Childs", "Children", "Childes", "Childen"],
      "answer": "Children",
      "segment": "English"
    },
    {
      "id": 54,
      "difficulty": "Easy",
      "question": "54. Which of these is a declarative sentence?",
      "options": [
        "What a beautiful day!",
        "Please close the door.",
        "I enjoy reading books.",
        "Are you coming to the party?"
      ],
      "answer": "I enjoy reading books.",
      "segment": "English"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. Identify the figure of speech in: 'The wind howled in the night.'",
      "options": ["Simile", "Personification", "Metaphor", "Hyperbole"],
      "answer": "Personification",
      "segment": "English"
    },
    {
      "id": 56,
      "difficulty": "Medium",
      "question": "56. Which verb tense is used in the sentence: 'She will have finished her homework by tomorrow'?",
      "options": ["Present Perfect", "Past Perfect", "Future Perfect", "Future Continuous"],
      "answer": "Future Perfect",
      "segment": "English"
    },
    {
      "id": 57,
      "difficulty": "Medium",
      "question": "57. What is the subject in the sentence: 'The book on the table is mine.'?",
      "options": ["Book", "Table", "Is", "Mine"],
      "answer": "Book",
      "segment": "English"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What is the antonym of 'ephemeral'?",
      "options": ["Short-lived", "Permanent", "Temporary", "Transitory"],
      "answer": "Permanent",
      "segment": "English"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. What does 'euphemism' mean?",
      "options": [
        "A harsh expression",
        "A polite term for something unpleasant",
        "An exaggeration for effect",
        "A repetition of sounds"
      ],
      "answer": "A polite term for something unpleasant",
      "segment": "English"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. Identify the correct indirect speech: 'He said, \\\"I am reading a book.\\\"'",
      "options": [
        "He said that he is reading a book.",
        "He said that he was reading a book.",
        "He said that I am reading a book.",
        "He said that I was reading a book."
      ],
      "answer": "He said that he was reading a book.",
      "segment": "English"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the capital of India?",
      "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
      "answer": "New Delhi",
      "segment": "SST"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Who is known as the Father of the Indian Constitution?",
      "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Sardar Patel"],
      "answer": "Dr. B.R. Ambedkar",
      "segment": "SST"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. Which river is known as the 'Sorrow of Bihar'?",
      "options": ["Ganga", "Kosi", "Yamuna", "Brahmaputra"],
      "answer": "Kosi",
      "segment": "SST"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. Which planet is known as the 'Red Planet'?",
      "options": ["Mars", "Earth", "Venus", "Jupiter"],
      "answer": "Mars",
      "segment": "SST"
    },
    {
      "id": 65,
      "difficulty": "Medium",
      "question": "65. Who was the founder of the Maurya Empire?",
      "options": ["Ashoka", "Chandragupta Maurya", "Bindusara", "Harshavardhana"],
      "answer": "Chandragupta Maurya",
      "segment": "SST"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is the primary occupation of people in the Ganga plains?",
      "options": ["Fishing", "Agriculture", "Mining", "Manufacturing"],
      "answer": "Agriculture",
      "segment": "SST"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Which battle marked the beginning of British rule in India?",
      "options": [
        "Battle of Panipat",
        "Battle of Plassey",
        "Battle of Buxar",
        "Battle of Haldighati"
      ],
      "answer": "Battle of Plassey",
      "segment": "SST"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What is the main reason for the seasonal variation in temperature?",
      "options": [
        "Rotation of Earth",
        "Revolution of Earth",
        "Distance from the Sun",
        "Gravitational pull of the Moon"
      ],
      "answer": "Revolution of Earth",
      "segment": "SST"
    },
    {
      "id": 69,
      "difficulty": "Hard",
      "question": "69. Which Indian state has the highest literacy rate as per recent data?",
      "options": ["Kerala", "Goa", "Tamil Nadu", "Himachal Pradesh"],
      "answer": "Kerala",
      "segment": "SST"
    },
    {
      "id": 70,
      "difficulty": "Hard",
      "question": "70. What was the primary aim of the 'Chipko Movement'?",
      "options": [
        "Promoting afforestation",
        "Preventing deforestation",
        "Development of irrigation",
        "Spreading literacy"
      ],
      "answer": "Preventing deforestation",
      "segment": "SST"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. Which part of the Indian Constitution deals with Fundamental Rights?",
      "options": ["Part I", "Part II", "Part III", "Part IV"],
      "answer": "Part III",
      "segment": "SST"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Which mountain range separates Europe from Asia?",
      "options": ["Himalayas", "Ural Mountains", "Andes", "Rockies"],
      "answer": "Ural Mountains",
      "segment": "SST"
    }
  ]
}




###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
