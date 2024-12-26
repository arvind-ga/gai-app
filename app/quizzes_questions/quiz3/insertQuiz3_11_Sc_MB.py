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
    "id": "3_11_sc_mb",
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
      "question": "31. What is the value of sin 30°?",
      "options": ["0", "1", "1/2", "√3/2"],
      "answer": "1/2",
      "segment": "Maths"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. The derivative of x² with respect to x is?",
      "options": ["x", "2x", "x²", "2x²"],
      "answer": "2x",
      "segment": "Maths"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. What is the sum of the angles in a triangle?",
      "options": ["90°", "180°", "360°", "120°"],
      "answer": "180°",
      "segment": "Maths"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. If a matrix has dimensions 3x2, how many rows does it have?",
      "options": ["2", "3", "6", "5"],
      "answer": "3",
      "segment": "Maths"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. What is the value of (a+b)²?",
      "options": ["a² + b²", "a² + 2ab + b²", "a² - 2ab + b²", "None of these"],
      "answer": "a² + 2ab + b²",
      "segment": "Maths"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the solution to the equation 2x - 5 = 3?",
      "options": ["x = 1", "x = 4", "x = -1", "x = 5"],
      "answer": "x = 4",
      "segment": "Maths"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. What is the slope of the line passing through points (2, 3) and (4, 7)?",
      "options": ["2", "4", "1", "5"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. What is the sum of the first 10 natural numbers?",
      "options": ["55", "50", "45", "60"],
      "answer": "55",
      "segment": "Maths"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. If logₐ(x) = 3 and logₐ(y) = 4, what is logₐ(xy)?",
      "options": ["7", "12", "1", "0"],
      "answer": "7",
      "segment": "Maths"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. What is the radius of a circle with area 25π?",
      "options": ["5", "25", "10", "50"],
      "answer": "5",
      "segment": "Maths"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. Solve the inequality: 3x - 7 > 2x + 5.",
      "options": ["x > 12", "x < 12", "x = 12", "x > -12"],
      "answer": "x > 12",
      "segment": "Maths"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What is the determinant of the matrix [[1, 2], [3, 4]]?",
      "options": ["-2", "2", "0", "10"],
      "answer": "-2",
      "segment": "Maths"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. If f(x) = 3x² + 2x + 1, what is f'(x)?",
      "options": ["6x + 2", "6x + 1", "3x + 2", "3x² + 2"],
      "answer": "6x + 2",
      "segment": "Maths"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Evaluate the integral ∫x dx.",
      "options": ["x²", "x²/2", "x + C", "x² + C"],
      "answer": "x²/2",
      "segment": "Maths"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. Find the sum of the series: 2 + 4 + 6 + ... + 20.",
      "options": ["110", "120", "100", "90"],
      "answer": "110",
      "segment": "Maths"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. What is the basic unit of life?",
      "options": ["Tissue", "Organ", "Cell", "Organism"],
      "answer": "Cell",
      "segment": "Bio"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. What is the pigment responsible for photosynthesis?",
      "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
      "answer": "Chlorophyll",
      "segment": "Bio"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. Which part of the plant is responsible for water absorption?",
      "options": ["Stem", "Leaves", "Roots", "Flowers"],
      "answer": "Roots",
      "segment": "Bio"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. Which biomolecule is the primary source of energy for the body?",
      "options": ["Proteins", "Lipids", "Carbohydrates", "Vitamins"],
      "answer": "Carbohydrates",
      "segment": "Bio"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. What is the functional unit of the kidney?",
      "options": ["Neuron", "Nephron", "Glomerulus", "Loop of Henle"],
      "answer": "Nephron",
      "segment": "Bio"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. What is the site of protein synthesis in a cell?",
      "options": ["Mitochondria", "Ribosomes", "Nucleus", "Golgi apparatus"],
      "answer": "Ribosomes",
      "segment": "Bio"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. Which hormone regulates the sugar level in blood?",
      "options": ["Insulin", "Adrenaline", "Thyroxine", "Glucagon"],
      "answer": "Insulin",
      "segment": "Bio"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. What is the main function of xylem in plants?",
      "options": ["Transport of water", "Transport of food", "Photosynthesis", "Reproduction"],
      "answer": "Transport of water",
      "segment": "Bio"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. Which enzyme is responsible for the digestion of proteins?",
      "options": ["Amylase", "Lipase", "Pepsin", "Trypsin"],
      "answer": "Pepsin",
      "segment": "Bio"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. What is the mode of nutrition in fungi?",
      "options": ["Autotrophic", "Parasitic", "Saprotrophic", "Symbiotic"],
      "answer": "Saprotrophic",
      "segment": "Bio"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. What is the chemical composition of a phospholipid molecule?",
      "options": ["Glycerol + 3 Fatty Acids", "Glycerol + 2 Fatty Acids + Phosphate group", "Glycerol + 1 Fatty Acid", "Glycerol + Phosphate group"],
      "answer": "Glycerol + 2 Fatty Acids + Phosphate group",
      "segment": "Bio"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. In which phase of the cell cycle does DNA replication occur?",
      "options": ["G1 phase", "S phase", "G2 phase", "M phase"],
      "answer": "S phase",
      "segment": "Bio"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What is the number of ATP molecules produced from one glucose molecule during aerobic respiration?",
      "options": ["32", "36", "38", "40"],
      "answer": "38",
      "segment": "Bio"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. Which structure in the human eye adjusts the focal length?",
      "options": ["Cornea", "Lens", "Retina", "Iris"],
      "answer": "Lens",
      "segment": "Bio"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the major nitrogenous waste in humans?",
      "options": ["Ammonia", "Urea", "Uric acid", "Creatinine"],
      "answer": "Urea",
      "segment": "Bio"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the synonym of the word 'Happy'?",
      "options": ["Sad", "Joyful", "Angry", "Bitter"],
      "answer": "Joyful",
      "segment": "English"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Identify the noun in the sentence: 'The boy plays football.'",
      "options": ["Boy", "Plays", "Football", "Both 'Boy' and 'Football'"],
      "answer": "Both 'Boy' and 'Football'",
      "segment": "English"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. Choose the correctly spelled word:",
      "options": ["Accomodate", "Acomodate", "Accommodate", "Accommadate"],
      "answer": "Accommodate",
      "segment": "English"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. What is the past tense of 'Go'?",
      "options": ["Goes", "Gone", "Went", "Going"],
      "answer": "Went",
      "segment": "English"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. What type of noun is 'Honesty'?",
      "options": ["Abstract Noun", "Proper Noun", "Common Noun", "Collective Noun"],
      "answer": "Abstract Noun",
      "segment": "English"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. Identify the figure of speech in: 'The wind howled in the night.'",
      "options": ["Simile", "Personification", "Metaphor", "Hyperbole"],
      "answer": "Personification",
      "segment": "English"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Fill in the blank: 'She ______ a song beautifully yesterday.'",
      "options": ["Sings", "Sang", "Singed", "Will sing"],
      "answer": "Sang",
      "segment": "English"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What is the antonym of 'Generous'?",
      "options": ["Kind", "Stingy", "Rich", "Thoughtful"],
      "answer": "Stingy",
      "segment": "English"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. Which of the following is a compound sentence?",
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
      "id": 70,
      "difficulty": "Medium",
      "question": "70. What does the word 'Epitome' mean?",
      "options": ["Summary", "Example", "Contradiction", "Exaggeration"],
      "answer": "Example",
      "segment": "English"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. What is the difference between 'Their', 'There', and 'They're'?",
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
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Identify the passive voice of: 'She is writing a letter.'",
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
      "id": 73,
      "difficulty": "Hard",
      "question": "73. What is the meaning of the idiom 'Break the ice'?",
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
      "id": 74,
      "difficulty": "Hard",
      "question": "74. What is a 'dangling modifier'?",
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
      "id": 75,
      "difficulty": "Hard",
      "question": "75. What is the term for the repetition of consonant sounds in poetry?",
      "options": ["Alliteration", "Assonance", "Consonance", "Rhyme"],
      "answer": "Alliteration",
      "segment": "English"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
