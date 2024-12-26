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
quiz_data = { "id": "3_10_allsubj",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. What is the SI unit of electric current?",
      "options": ["Ampere", "Volt", "Ohm", "Watt"],
      "answer": "Ampere",
      "segment": "Physics"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. Which type of lens is used to correct myopia?",
      "options": ["Convex", "Concave", "Cylindrical", "Plano-convex"],
      "answer": "Concave",
      "segment": "Physics"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What is the speed of light in a vacuum?",
      "options": [
        "3 × 10^8 m/s",
        "3 × 10^6 m/s",
        "3 × 10^10 m/s",
        "3 × 10^12 m/s"
      ],
      "answer": "3 × 10^8 m/s",
      "segment": "Physics"
    },
    {
      "id": 4,
      "difficulty": "Medium",
      "question": "4. What is the power of a concave lens with a focal length of -50 cm?",
      "options": ["+2 D", "-2 D", "+0.5 D", "-0.5 D"],
      "answer": "-2 D",
      "segment": "Physics"
    },
    {
      "id": 5,
      "difficulty": "Medium",
      "question": "5. What is the relationship between voltage (V), current (I), and resistance (R)?",
      "options": [
        "V = IR",
        "V = I/R",
        "V = R/I",
        "V = IR^2"
      ],
      "answer": "V = IR",
      "segment": "Physics"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. What is the phenomenon of splitting white light into its component colors called?",
      "options": ["Reflection", "Refraction", "Dispersion", "Diffraction"],
      "answer": "Dispersion",
      "segment": "Physics"
    },
    {
      "id": 7,
      "difficulty": "Hard",
      "question": "7. What is the formula for the magnification produced by a lens?",
      "options": [
        "m = -v/u",
        "m = v/u",
        "m = u/v",
        "m = -u/v"
      ],
      "answer": "m = -v/u",
      "segment": "Physics"
    },
    {
      "id": 8,
      "difficulty": "Hard",
      "question": "8. In a series circuit, the equivalent resistance is:",
      "options": [
        "Equal to the lowest resistance",
        "Equal to the highest resistance",
        "The sum of individual resistances",
        "The reciprocal of the sum of reciprocals of resistances"
      ],
      "answer": "The sum of individual resistances",
      "segment": "Physics"
    },
    {
      "id": 9,
      "difficulty": "Hard",
      "question": "9. What is the focal length of a convex lens of power +5D?",
      "options": ["+0.2 m", "-0.2 m", "+5 m", "-5 m"],
      "answer": "+0.2 m",
      "segment": "Physics"
    },
    {
      "id": 10,
      "difficulty": "Easy",
      "question": "10. What is the chemical formula of water?",
      "options": ["H2O", "CO2", "O2", "H2SO4"],
      "answer": "H2O",
      "segment": "Chemistry"
    },
    {
      "id": 11,
      "difficulty": "Easy",
      "question": "11. Which gas is released during photosynthesis?",
      "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
      "answer": "Oxygen",
      "segment": "Chemistry"
    },
    {
      "id": 12,
      "difficulty": "Easy",
      "question": "12. Which of the following is an element?",
      "options": ["Water", "Iron", "Salt", "Sugar"],
      "answer": "Iron",
      "segment": "Chemistry"
    },
    {
      "id": 13,
      "difficulty": "Medium",
      "question": "13. What is the pH value of a neutral solution?",
      "options": ["0", "7", "14", "5"],
      "answer": "7",
      "segment": "Chemistry"
    },
    {
      "id": 14,
      "difficulty": "Medium",
      "question": "14. What is the atomic number of Carbon?",
      "options": ["6", "12", "8", "14"],
      "answer": "6",
      "segment": "Chemistry"
    },
    {
      "id": 15,
      "difficulty": "Medium",
      "question": "15. What type of reaction is 2H2 + O2 → 2H2O?",
      "options": [
        "Decomposition",
        "Combination",
        "Displacement",
        "Double displacement"
      ],
      "answer": "Combination",
      "segment": "Chemistry"
    },
    {
      "id": 16,
      "difficulty": "Hard",
      "question": "16. What is the main ore of aluminium?",
      "options": ["Bauxite", "Haematite", "Copper pyrite", "Zinc blende"],
      "answer": "Bauxite",
      "segment": "Chemistry"
    },
    {
      "id": 17,
      "difficulty": "Hard",
      "question": "17. Which gas is evolved when dilute hydrochloric acid reacts with zinc?",
      "options": ["Oxygen", "Hydrogen", "Nitrogen", "Chlorine"],
      "answer": "Hydrogen",
      "segment": "Chemistry"
    },
    {
      "id": 18,
      "difficulty": "Hard",
      "question": "18. What is the common name of sodium bicarbonate?",
      "options": [
        "Washing soda",
        "Baking soda",
        "Caustic soda",
        "Sodium hydroxide"
      ],
      "answer": "Baking soda",
      "segment": "Chemistry"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. What is the basic unit of life?",
      "options": ["Tissue", "Organ", "Cell", "Organism"],
      "answer": "Cell",
      "segment": "Bio"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which organ in the human body is responsible for pumping blood?",
      "options": ["Liver", "Heart", "Kidney", "Lung"],
      "answer": "Heart",
      "segment": "Bio"
    },
    {
      "id": 21,
      "difficulty": "Easy",
      "question": "21. What is the process of conversion of sugar into alcohol by yeast called?",
      "options": ["Photosynthesis", "Fermentation", "Respiration", "Transpiration"],
      "answer": "Fermentation",
      "segment": "Bio"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. Which structure in a plant cell contains chlorophyll?",
      "options": ["Mitochondria", "Nucleus", "Chloroplast", "Vacuole"],
      "answer": "Chloroplast",
      "segment": "Bio"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. What is the main function of the xylem in plants?",
      "options": [
        "Transport of food",
        "Transport of water and minerals",
        "Photosynthesis",
        "Reproduction"
      ],
      "answer": "Transport of water and minerals",
      "segment": "Bio"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What type of reproduction occurs without the involvement of gametes?",
      "options": [
        "Sexual reproduction",
        "Asexual reproduction",
        "Cross-pollination",
        "Self-pollination"
      ],
      "answer": "Asexual reproduction",
      "segment": "Bio"
    },
    {
      "id": 25,
      "difficulty": "Hard",
      "question": "25. What is the term for the genetic makeup of an organism?",
      "options": ["Phenotype", "Genotype", "Chromosome", "Allele"],
      "answer": "Genotype",
      "segment": "Bio"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. Which part of the human brain is responsible for maintaining balance and posture?",
      "options": ["Cerebrum", "Cerebellum", "Medulla", "Pons"],
      "answer": "Cerebellum",
      "segment": "Bio"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. What is the primary nitrogenous waste in humans?",
      "options": ["Ammonia", "Urea", "Uric acid", "Creatinine"],
      "answer": "Urea",
      "segment": "Bio"
    },
    {
      "id": 28,
      "difficulty": "Easy",
      "question": "28. What is the value of √16?",
      "options": ["2", "4", "8", "16"],
      "answer": "4",
      "segment": "Math"
    },
    {
      "id": 29,
      "difficulty": "Easy",
      "question": "29. What is the area of a square with side length 5 cm?",
      "options": ["10 cm²", "15 cm²", "20 cm²", "25 cm²"],
      "answer": "25 cm²",
      "segment": "Math"
    },
    {
      "id": 30,
      "difficulty": "Easy",
      "question": "30. If a triangle has angles 60° and 90°, what is the third angle?",
      "options": ["30°", "45°", "60°", "90°"],
      "answer": "30°",
      "segment": "Math"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the perimeter of a rectangle with length 8 cm and width 4 cm?",
      "options": ["24 cm", "32 cm", "20 cm", "16 cm"],
      "answer": "24 cm",
      "segment": "Math"
    },
    {
      "id": 32,
      "difficulty": "Medium",
      "question": "32. Solve for x: 2x + 5 = 15.",
      "options": ["x = 5", "x = 10", "x = 15", "x = 20"],
      "answer": "x = 5",
      "segment": "Math"
    },
    {
      "id": 33,
      "difficulty": "Medium",
      "question": "33. What is the HCF of 18 and 24?",
      "options": ["2", "3", "6", "12"],
      "answer": "6",
      "segment": "Math"
    },
    {
      "id": 34,
      "difficulty": "Medium",
      "question": "34. If the circumference of a circle is 44 cm, what is its radius? (Use π = 22/7)",
      "options": ["7 cm", "14 cm", "21 cm", "28 cm"],
      "answer": "7 cm",
      "segment": "Math"
    },
    {
      "id": 35,
      "difficulty": "Medium",
      "question": "35. Find the value of x in the equation 3x - 9 = 0.",
      "options": ["x = 3", "x = -3", "x = 9", "x = -9"],
      "answer": "x = 3",
      "segment": "Math"
    },
    {
      "id": 36,
      "difficulty": "Hard",
      "question": "36. Solve: 2x² - 3x - 2 = 0.",
      "options": ["x = 2, x = -1/2", "x = -2, x = 1/2", "x = 1, x = -2", "x = 2, x = -2"],
      "answer": "x = 2, x = -1/2",
      "segment": "Math"
    },
    {
      "id": 37,
      "difficulty": "Hard",
      "question": "37. If the sum of the first n terms of an AP is 5n² + 3n, what is the first term?",
      "options": ["3", "8", "5", "10"],
      "answer": "8",
      "segment": "Math"
    },
    {
      "id": 38,
      "difficulty": "Hard",
      "question": "38. A cone has a base radius of 3 cm and height 4 cm. What is its slant height?",
      "options": ["3 cm", "4 cm", "5 cm", "6 cm"],
      "answer": "5 cm",
      "segment": "Math"
    },
    {
      "id": 39,
      "difficulty": "Hard",
      "question": "39. If sin θ = 3/5, what is the value of cos θ?",
      "options": ["4/5", "3/4", "5/3", "4/3"],
      "answer": "4/5",
      "segment": "Math"
    },
    {
      "id": 40,
      "difficulty": "Easy",
      "question": "40. Which of the following is an input device?",
      "options": ["Monitor", "Printer", "Keyboard", "Speaker"],
      "answer": "Keyboard",
      "segment": "Computer"
    },
    {
      "id": 41,
      "difficulty": "Easy",
      "question": "41. What does CPU stand for?",
      "options": ["Central Processing Unit", "Central Programming Unit", "Computer Processing Unit", "Central Process Utility"],
      "answer": "Central Processing Unit",
      "segment": "Computer"
    },
    {
      "id": 42,
      "difficulty": "Easy",
      "question": "42. What is the function of an operating system?",
      "options": [
        "Manage hardware and software",
        "Perform calculations",
        "Run antivirus software",
        "Create documents"
      ],
      "answer": "Manage hardware and software",
      "segment": "Computer"
    },
    {
      "id": 43,
      "difficulty": "Easy",
      "question": "43. Which of the following is an example of an output device?",
      "options": ["Mouse", "Scanner", "Printer", "Keyboard"],
      "answer": "Printer",
      "segment": "Computer"
    },
    {
      "id": 44,
      "difficulty": "Medium",
      "question": "44. What is the full form of HTTP?",
      "options": [
        "Hyper Transfer Text Protocol",
        "Hyper Text Transfer Protocol",
        "Hyper Text Transmission Protocol",
        "Hyper Text Translation Protocol"
      ],
      "answer": "Hyper Text Transfer Protocol",
      "segment": "Computer"
    },
    {
      "id": 45,
      "difficulty": "Medium",
      "question": "45. Which type of memory is used for temporary storage?",
      "options": ["ROM", "RAM", "Hard Drive", "Cache"],
      "answer": "RAM",
      "segment": "Computer"
    },
    {
      "id": 46,
      "difficulty": "Medium",
      "question": "46. Which language is known as the backbone of web development?",
      "options": ["Python", "JavaScript", "C++", "Ruby"],
      "answer": "JavaScript",
      "segment": "Computer"
    },
    {
      "id": 47,
      "difficulty": "Medium",
      "question": "47. Which device is used to connect two networks?",
      "options": ["Switch", "Router", "Hub", "Modem"],
      "answer": "Router",
      "segment": "Computer"
    },
    {
      "id": 48,
      "difficulty": "Hard",
      "question": "48. Which of the following is NOT a database management system?",
      "options": ["MySQL", "Oracle", "Python", "PostgreSQL"],
      "answer": "Python",
      "segment": "Computer"
    },
    {
      "id": 49,
      "difficulty": "Hard",
      "question": "49. Which protocol is used to send emails?",
      "options": ["HTTP", "SMTP", "FTP", "IMAP"],
      "answer": "SMTP",
      "segment": "Computer"
    },
    {
      "id": 50,
      "difficulty": "Hard",
      "question": "50. What is the primary purpose of a firewall in a network?",
      "options": [
        "To prevent unauthorized access",
        "To improve network speed",
        "To compress data",
        "To increase bandwidth"
      ],
      "answer": "To prevent unauthorized access",
      "segment": "Computer"
    },
    {
      "id": 51,
      "difficulty": "Hard",
      "question": "51. Which data structure uses FIFO (First In, First Out)?",
      "options": ["Stack", "Queue", "Array", "Tree"],
      "answer": "Queue",
      "segment": "Computer"
    },
    {
      "id": 52,
      "difficulty": "Easy",
      "question": "52. Which part of speech is the word 'quickly'?",
      "options": ["Noun", "Adjective", "Adverb", "Verb"],
      "answer": "Adverb",
      "segment": "English"
    },
    {
      "id": 53,
      "difficulty": "Easy",
      "question": "53. What is the plural form of 'child'?",
      "options": ["Childs", "Childrens", "Children", "Child"],
      "answer": "Children",
      "segment": "English"
    },
    {
      "id": 54,
      "difficulty": "Easy",
      "question": "54. Which tense is used in the sentence: 'She is singing a song'?",
      "options": ["Past Continuous", "Present Continuous", "Future Continuous", "Present Perfect"],
      "answer": "Present Continuous",
      "segment": "English"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. What is a synonym for the word 'benevolent'?",
      "options": ["Cruel", "Kind", "Mean", "Arrogant"],
      "answer": "Kind",
      "segment": "English"
    },
    {
      "id": 56,
      "difficulty": "Medium",
      "question": "56. Identify the figure of speech in the sentence: 'The world is a stage.'",
      "options": ["Simile", "Metaphor", "Personification", "Hyperbole"],
      "answer": "Metaphor",
      "segment": "English"
    },
    {
      "id": 57,
      "difficulty": "Medium",
      "question": "57. What does the idiom 'break the ice' mean?",
      "options": [
        "To break something cold",
        "To initiate a conversation",
        "To break a promise",
        "To cause trouble"
      ],
      "answer": "To initiate a conversation",
      "segment": "English"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. Which poetic device is used in the line: 'The sea danced to the rhythm of the wind'?",
      "options": ["Alliteration", "Personification", "Oxymoron", "Onomatopoeia"],
      "answer": "Personification",
      "segment": "English"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. What is the main theme of the poem 'The Road Not Taken' by Robert Frost?",
      "options": [
        "Love and Relationships",
        "Nature and Seasons",
        "Choices and Consequences",
        "Adventure and Exploration"
      ],
      "answer": "Choices and Consequences",
      "segment": "English"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the difference between a dependent clause and an independent clause?",
      "options": [
        "An independent clause cannot stand alone while a dependent clause can.",
        "A dependent clause cannot stand alone while an independent clause can.",
        "Both can stand alone as sentences.",
        "Both require conjunctions to form a sentence."
      ],
      "answer": "A dependent clause cannot stand alone while an independent clause can.",
      "segment": "English"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. Which of the following is the longest river in India?",
      "options": ["Ganga", "Brahmaputra", "Yamuna", "Godavari"],
      "answer": "Ganga",
      "segment": "SST"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Who is known as the 'Father of the Indian Constitution'?",
      "options": ["Mahatma Gandhi", "B. R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel"],
      "answer": "B. R. Ambedkar",
      "segment": "SST"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. What is the main occupation of people in rural India?",
      "options": ["Agriculture", "Manufacturing", "IT Services", "Trade"],
      "answer": "Agriculture",
      "segment": "SST"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. Who was the first President of India?",
      "options": ["Mahatma Gandhi", "Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel"],
      "answer": "Rajendra Prasad",
      "segment": "SST"
    },
    {
      "id": 65,
      "difficulty": "Medium",
      "question": "65. Which type of farming is practiced on small patches of land with the help of primitive tools?",
      "options": ["Commercial Farming", "Subsistence Farming", "Plantation Farming", "Intensive Farming"],
      "answer": "Subsistence Farming",
      "segment": "SST"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. In which year did the Indian National Congress launch the Quit India Movement?",
      "options": ["1930", "1942", "1947", "1920"],
      "answer": "1942",
      "segment": "SST"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. What does GDP stand for?",
      "options": [
        "Gross Domestic Product",
        "Gross Development Plan",
        "General Domestic Plan",
        "Global Domestic Product"
      ],
      "answer": "Gross Domestic Product",
      "segment": "SST"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What was the main objective of the Civil Disobedience Movement?",
      "options": [
        "Demand for complete independence",
        "Boycott of British goods",
        "To oppose the Rowlatt Act",
        "Protest against salt tax"
      ],
      "answer": "Protest against salt tax",
      "segment": "SST"
    },
    {
      "id": 69,
      "difficulty": "Hard",
      "question": "69. Which Indian state has the highest literacy rate according to the 2011 Census?",
      "options": ["Kerala", "Goa", "Tamil Nadu", "Himachal Pradesh"],
      "answer": "Kerala",
      "segment": "SST"
    },
    {
      "id": 70,
      "difficulty": "Hard",
      "question": "70. What is the tenure of the members of the Rajya Sabha?",
      "options": ["5 years", "6 years", "7 years", "Lifetime"],
      "answer": "6 years",
      "segment": "SST"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. Which global organization was established in 1945 to promote peace and security?",
      "options": ["World Trade Organization", "United Nations", "World Bank", "NATO"],
      "answer": "United Nations",
      "segment": "SST"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Which Act is referred to as the 'Charter of Slavery' by Jawaharlal Nehru?",
      "options": ["Rowlatt Act", "Regulating Act", "Government of India Act 1935", "Pitts India Act"],
      "answer": "Rowlatt Act",
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
