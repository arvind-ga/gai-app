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
quiz_data = { "id": "3_11_sc_bpe",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. What is the SI unit of force?",
      "options": ["Newton", "Joule", "Watt", "Pascal"],
      "answer": "Newton",
      "segment": "Physics"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. What is the speed of light in vacuum?",
      "options": ["3 × 10^8 m/s", "3 × 10^6 m/s", "3 × 10^10 m/s", "3 × 10^4 m/s"],
      "answer": "3 × 10^8 m/s",
      "segment": "Physics"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What does Newton's first law of motion define?",
      "options": ["Force", "Inertia", "Energy", "Momentum"],
      "answer": "Inertia",
      "segment": "Physics"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. Which quantity is scalar?",
      "options": ["Force", "Velocity", "Work", "Acceleration"],
      "answer": "Work",
      "segment": "Physics"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. The value of acceleration due to gravity on Earth is approximately?",
      "options": ["9.8 m/s^2", "10.8 m/s^2", "8.8 m/s^2", "11.8 m/s^2"],
      "answer": "9.8 m/s^2",
      "segment": "Physics"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. Which physical quantity has the unit Joule-second?",
      "options": ["Energy", "Planck's constant", "Angular momentum", "Power"],
      "answer": "Planck's constant",
      "segment": "Physics"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. The range of a projectile is maximum for an angle of?",
      "options": ["30°", "45°", "60°", "90°"],
      "answer": "45°",
      "segment": "Physics"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. A body of mass 10 kg is moving with a velocity of 5 m/s. What is its kinetic energy?",
      "options": ["125 J", "250 J", "50 J", "500 J"],
      "answer": "125 J",
      "segment": "Physics"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. What is the escape velocity from the Earth's surface?",
      "options": ["11.2 km/s", "12.2 km/s", "10.2 km/s", "9.8 km/s"],
      "answer": "11.2 km/s",
      "segment": "Physics"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. A force acts on a body and changes its velocity from 5 m/s to 10 m/s in 5 seconds. What is the acceleration?",
      "options": ["1 m/s²", "2 m/s²", "5 m/s²", "10 m/s²"],
      "answer": "1 m/s²",
      "segment": "Physics"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. The moment of inertia of a thin rod about an axis perpendicular to its length and passing through its center is given by?",
      "options": ["(1/12)ML²", "(1/3)ML²", "(1/2)ML²", "(1/4)ML²"],
      "answer": "(1/12)ML²",
      "segment": "Physics"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. What is the relation between linear velocity (v) and angular velocity (ω) in circular motion?",
      "options": ["v = rω", "v = ω/r", "v = r/ω", "v = ω²r"],
      "answer": "v = rω",
      "segment": "Physics"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. A satellite revolves around the Earth in a circular orbit. What is its total energy?",
      "options": ["Kinetic energy", "Potential energy", "Zero", "Negative"],
      "answer": "Negative",
      "segment": "Physics"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. In simple harmonic motion, the velocity of the particle is maximum at?",
      "options": ["Mean position", "Extreme position", "Between mean and extreme", "None of these"],
      "answer": "Mean position",
      "segment": "Physics"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. What is the time period of a simple pendulum of length 1m on the moon? (g_moon = 1.6 m/s²)",
      "options": ["4.9 s", "5 s", "7.8 s", "10 s"],
      "answer": "4.9 s",
      "segment": "Physics"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. What is the SI unit of amount of substance?",
      "options": ["Mole", "Gram", "Kilogram", "Litre"],
      "answer": "Mole",
      "segment": "Chemistry"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. Which of the following is a noble gas?",
      "options": ["Oxygen", "Nitrogen", "Helium", "Hydrogen"],
      "answer": "Helium",
      "segment": "Chemistry"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. What is the chemical symbol for Sodium?",
      "options": ["Na", "S", "Sn", "N"],
      "answer": "Na",
      "segment": "Chemistry"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. Which element has the atomic number 1?",
      "options": ["Oxygen", "Nitrogen", "Hydrogen", "Carbon"],
      "answer": "Hydrogen",
      "segment": "Chemistry"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. What is the valency of Carbon?",
      "options": ["2", "4", "6", "8"],
      "answer": "4",
      "segment": "Chemistry"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. Which of the following is a state function?",
      "options": ["Heat", "Work", "Entropy", "Distance"],
      "answer": "Entropy",
      "segment": "Chemistry"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. What is the hybridization of Carbon in methane (CH4)?",
      "options": ["sp", "sp2", "sp3", "sp3d"],
      "answer": "sp3",
      "segment": "Chemistry"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. Which acid is known as the king of chemicals?",
      "options": ["Nitric acid", "Sulfuric acid", "Hydrochloric acid", "Phosphoric acid"],
      "answer": "Sulfuric acid",
      "segment": "Chemistry"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What is the pH of a neutral solution at 25°C?",
      "options": ["0", "7", "14", "10"],
      "answer": "7",
      "segment": "Chemistry"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. Which of the following molecules has a linear shape?",
      "options": ["H2O", "CO2", "CH4", "NH3"],
      "answer": "CO2",
      "segment": "Chemistry"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. What is the standard enthalpy change for the formation of water (H2O)?",
      "options": ["-285.8 kJ/mol", "-240.5 kJ/mol", "0 kJ/mol", "285.8 kJ/mol"],
      "answer": "-285.8 kJ/mol",
      "segment": "Chemistry"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. The bond angle in an ammonia (NH3) molecule is approximately?",
      "options": ["120°", "90°", "109.5°", "107°"],
      "answer": "107°",
      "segment": "Chemistry"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. Which of the following has the highest ionization energy?",
      "options": ["Na", "Mg", "Al", "Cl"],
      "answer": "Cl",
      "segment": "Chemistry"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. What is the oxidation state of Sulfur in H2SO4?",
      "options": ["+6", "+4", "+2", "0"],
      "answer": "+6",
      "segment": "Chemistry"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. What is the molecular geometry of SF6?",
      "options": ["Tetrahedral", "Octahedral", "Square planar", "Trigonal planar"],
      "answer": "Octahedral",
      "segment": "Chemistry"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the basic unit of life?",
      "options": ["Tissue", "Organ", "Cell", "Organism"],
      "answer": "Cell",
      "segment": "Bio"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. What is the pigment responsible for photosynthesis?",
      "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
      "answer": "Chlorophyll",
      "segment": "Bio"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. Which part of the plant is responsible for water absorption?",
      "options": ["Stem", "Leaves", "Roots", "Flowers"],
      "answer": "Roots",
      "segment": "Bio"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. Which biomolecule is the primary source of energy for the body?",
      "options": ["Proteins", "Lipids", "Carbohydrates", "Vitamins"],
      "answer": "Carbohydrates",
      "segment": "Bio"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. What is the functional unit of the kidney?",
      "options": ["Neuron", "Nephron", "Glomerulus", "Loop of Henle"],
      "answer": "Nephron",
      "segment": "Bio"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the site of protein synthesis in a cell?",
      "options": ["Mitochondria", "Ribosomes", "Nucleus", "Golgi apparatus"],
      "answer": "Ribosomes",
      "segment": "Bio"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. Which hormone regulates the sugar level in blood?",
      "options": ["Insulin", "Adrenaline", "Thyroxine", "Glucagon"],
      "answer": "Insulin",
      "segment": "Bio"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. What is the main function of xylem in plants?",
      "options": ["Transport of water", "Transport of food", "Photosynthesis", "Reproduction"],
      "answer": "Transport of water",
      "segment": "Bio"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. Which enzyme is responsible for the digestion of proteins?",
      "options": ["Amylase", "Lipase", "Pepsin", "Trypsin"],
      "answer": "Pepsin",
      "segment": "Bio"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. What is the mode of nutrition in fungi?",
      "options": ["Autotrophic", "Parasitic", "Saprotrophic", "Symbiotic"],
      "answer": "Saprotrophic",
      "segment": "Bio"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. What is the chemical composition of a phospholipid molecule?",
      "options": ["Glycerol + 3 Fatty Acids", "Glycerol + 2 Fatty Acids + Phosphate group", "Glycerol + 1 Fatty Acid", "Glycerol + Phosphate group"],
      "answer": "Glycerol + 2 Fatty Acids + Phosphate group",
      "segment": "Bio"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. In which phase of the cell cycle does DNA replication occur?",
      "options": ["G1 phase", "S phase", "G2 phase", "M phase"],
      "answer": "S phase",
      "segment": "Bio"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. What is the number of ATP molecules produced from one glucose molecule during aerobic respiration?",
      "options": ["32", "36", "38", "40"],
      "answer": "38",
      "segment": "Bio"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Which structure in the human eye adjusts the focal length?",
      "options": ["Cornea", "Lens", "Retina", "Iris"],
      "answer": "Lens",
      "segment": "Bio"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. What is the major nitrogenous waste in humans?",
      "options": ["Ammonia", "Urea", "Uric acid", "Creatinine"],
      "answer": "Urea",
      "segment": "Bio"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. What is the synonym of the word 'Happy'?",
      "options": ["Sad", "Joyful", "Angry", "Bitter"],
      "answer": "Joyful",
      "segment": "English"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. Identify the noun in the sentence: 'The boy plays football.'",
      "options": ["Boy", "Plays", "Football", "Both 'Boy' and 'Football'"],
      "answer": "Both 'Boy' and 'Football'",
      "segment": "English"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. Choose the correctly spelled word:",
      "options": ["Accomodate", "Acomodate", "Accommodate", "Accommadate"],
      "answer": "Accommodate",
      "segment": "English"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. What is the past tense of 'Go'?",
      "options": ["Goes", "Gone", "Went", "Going"],
      "answer": "Went",
      "segment": "English"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. What type of noun is 'Honesty'?",
      "options": ["Abstract Noun", "Proper Noun", "Common Noun", "Collective Noun"],
      "answer": "Abstract Noun",
      "segment": "English"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. Identify the figure of speech in: 'The wind howled in the night.'",
      "options": ["Simile", "Personification", "Metaphor", "Hyperbole"],
      "answer": "Personification",
      "segment": "English"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. Fill in the blank: 'She ______ a song beautifully yesterday.'",
      "options": ["Sings", "Sang", "Singed", "Will sing"],
      "answer": "Sang",
      "segment": "English"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. What is the antonym of 'Generous'?",
      "options": ["Kind", "Stingy", "Rich", "Thoughtful"],
      "answer": "Stingy",
      "segment": "English"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. Which of the following is a compound sentence?",
      "options": [
        "I was late, so I took a taxi.",
        "She plays the piano.",
        "Because it was raining, we stayed inside.",
        "He left early to catch the train."
      ],
      "answer": "I was late, so I took a taxi.",
      "segment": "English"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. What does the word 'Epitome' mean?",
      "options": ["Summary", "Example", "Contradiction", "Exaggeration"],
      "answer": "Example",
      "segment": "English"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. What is the difference between 'Their', 'There', and 'They're'?",
      "options": [
        "'Their' is possessive, 'There' is a place, 'They're' is a contraction.",
        "'Their' is a place, 'There' is possessive, 'They're' is a verb.",
        "'Their' is a contraction, 'There' is possessive, 'They're' is a noun.",
        "'Their' is a verb, 'There' is a noun, 'They're' is possessive."
      ],
      "answer": "'Their' is possessive, 'There' is a place, 'They're' is a contraction.",
      "segment": "English"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. Identify the passive voice of: 'She is writing a letter.'",
      "options": [
        "A letter is written by her.",
        "A letter is being written by her.",
        "A letter was written by her.",
        "A letter has been written by her."
      ],
      "answer": "A letter is being written by her.",
      "segment": "English"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What is the meaning of the idiom 'Break the ice'?",
      "options": [
        "To shatter something",
        "To initiate a conversation",
        "To cool down",
        "To make peace"
      ],
      "answer": "To initiate a conversation",
      "segment": "English"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. What is a 'dangling modifier'?",
      "options": [
        "A modifier that lacks a subject",
        "A misplaced adjective",
        "A phrase that describes an unrelated word",
        "A pronoun that replaces a noun"
      ],
      "answer": "A phrase that describes an unrelated word",
      "segment": "English"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the term for the repetition of consonant sounds in poetry?",
      "options": ["Alliteration", "Assonance", "Consonance", "Rhyme"],
      "answer": "Alliteration",
      "segment": "English"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the full form of BMI?",
      "options": ["Body Mass Index", "Body Measurement Indicator", "Basic Mass Index", "Body Measurement Index"],
      "answer": "Body Mass Index",
      "segment": "Physical_Edu"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Which of the following is a component of physical fitness?",
      "options": ["Flexibility", "Intelligence", "Memory", "Speed Reading"],
      "answer": "Flexibility",
      "segment": "Physical_Edu"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. What is the national game of India?",
      "options": ["Cricket", "Hockey", "Football", "Kabaddi"],
      "answer": "Hockey",
      "segment": "Physical_Edu"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. Which of the following is an outdoor game?",
      "options": ["Chess", "Carrom", "Badminton", "Hockey"],
      "answer": "Hockey",
      "segment": "Physical_Edu"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. How many players are there in a standard volleyball team?",
      "options": ["6", "5", "7", "8"],
      "answer": "6",
      "segment": "Physical_Edu"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is the main purpose of warming up before exercise?",
      "options": ["To tire the muscles", "To increase flexibility", "To cool the body", "To relax the mind"],
      "answer": "To increase flexibility",
      "segment": "Physical_Edu"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Which is the correct sequence of fitness components in a workout?",
      "options": [
        "Strength, Warm-up, Flexibility",
        "Warm-up, Flexibility, Strength",
        "Flexibility, Warm-up, Endurance",
        "Warm-up, Strength, Endurance"
      ],
      "answer": "Warm-up, Flexibility, Strength",
      "segment": "Physical_Edu"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. Which test is used to measure cardiovascular endurance?",
      "options": ["Sit and Reach Test", "Push-up Test", "12-Minute Run Test", "Sprint Test"],
      "answer": "12-Minute Run Test",
      "segment": "Physical_Edu"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. What is the ideal heart rate for an adult during moderate exercise?",
      "options": ["60-80 bpm", "100-120 bpm", "120-160 bpm", "80-100 bpm"],
      "answer": "120-160 bpm",
      "segment": "Physical_Edu"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. What is the term for the ability of muscles to exert force repeatedly over a period of time?",
      "options": ["Muscular Strength", "Muscular Endurance", "Flexibility", "Agility"],
      "answer": "Muscular Endurance",
      "segment": "Physical_Edu"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. What is the term for the maximum amount of oxygen a person can utilize during exercise?",
      "options": ["VO2 Max", "Tidal Volume", "Lung Capacity", "Oxygen Reserve"],
      "answer": "VO2 Max",
      "segment": "Physical_Edu"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. In athletics, what is the standard length of a marathon race?",
      "options": ["42.195 km", "40.000 km", "21.097 km", "50.000 km"],
      "answer": "42.195 km",
      "segment": "Physical_Edu"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. What is the official size of a basketball court in international competitions?",
      "options": [
        "28 m x 15 m",
        "30 m x 15 m",
        "28 m x 14 m",
        "30 m x 14 m"
      ],
      "answer": "28 m x 15 m",
      "segment": "Physical_Edu"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. What is the term for the amount of energy needed to raise the temperature of one kilogram of water by one degree Celsius?",
      "options": ["Joule", "Calorie", "Watt", "Newton"],
      "answer": "Calorie",
      "segment": "Physical_Edu"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. Which of the following is a principle of training to improve performance?",
      "options": ["Overload", "Stability", "Relaxation", "Endurance"],
      "answer": "Overload",
      "segment": "Physical_Edu"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
