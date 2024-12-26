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
quiz_data = { "id": "3_12_sc_mb",
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
      "question": "2. What is the speed of light in vacuum?",
      "options": ["3 × 10^8 m/s", "3 × 10^6 m/s", "3 × 10^7 m/s", "3 × 10^9 m/s"],
      "answer": "3 × 10^8 m/s",
      "segment": "Physics"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. Which type of mirror is used in a car’s rearview mirror?",
      "options": ["Concave", "Convex", "Plane", "None"],
      "answer": "Convex",
      "segment": "Physics"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. What does Ohm’s law state?",
      "options": [
        "V = IR",
        "I = VR",
        "R = VI",
        "None of these"
      ],
      "answer": "V = IR",
      "segment": "Physics"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. Which fundamental force is the weakest?",
      "options": ["Gravitational", "Electromagnetic", "Weak Nuclear", "Strong Nuclear"],
      "answer": "Gravitational",
      "segment": "Physics"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. What is the angular momentum of a particle with mass m, velocity v, and radius r?",
      "options": ["mvr", "mv/r", "mr/v", "1/2 mvr"],
      "answer": "mvr",
      "segment": "Physics"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. What is the potential energy of a charge q at a distance r from another charge Q?",
      "options": [
        "k(Qq)/r",
        "k(Qq)/r^2",
        "k(Q^2)/r",
        "k(q^2)/r"
      ],
      "answer": "k(Qq)/r",
      "segment": "Physics"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. What is the dimensional formula of Planck’s constant?",
      "options": [
        "[ML^2T^-1]",
        "[MLT^-1]",
        "[M^2L^2T^-1]",
        "[ML^2T^2]"
      ],
      "answer": "[ML^2T^-1]",
      "segment": "Physics"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. Which law is used to calculate the magnetic field produced by a current-carrying wire?",
      "options": [
        "Biot-Savart Law",
        "Faraday’s Law",
        "Lenz’s Law",
        "Ampere’s Law"
      ],
      "answer": "Biot-Savart Law",
      "segment": "Physics"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. In Young’s double-slit experiment, what happens if the slit separation decreases?",
      "options": [
        "Fringe width increases",
        "Fringe width decreases",
        "Fringe width remains constant",
        "Intensity decreases"
      ],
      "answer": "Fringe width increases",
      "segment": "Physics"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. In a circuit, the phase difference between voltage and current is 90°. What type of circuit is it?",
      "options": [
        "Purely Resistive",
        "Purely Capacitive",
        "Purely Inductive",
        "Resonant"
      ],
      "answer": "Purely Capacitive",
      "segment": "Physics"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. What is the ratio of de Broglie wavelengths for an electron and a proton moving with the same speed?",
      "options": [
        "√(m_p/m_e)",
        "√(m_e/m_p)",
        "m_p/m_e",
        "m_e/m_p"
      ],
      "answer": "√(m_p/m_e)",
      "segment": "Physics"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. In a hydrogen atom, if the electron jumps from n=3 to n=2, what type of spectrum is emitted?",
      "options": [
        "Lyman series",
        "Balmer series",
        "Paschen series",
        "Brackett series"
      ],
      "answer": "Balmer series",
      "segment": "Physics"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. What is the work function of a material if the threshold frequency is 5 × 10^14 Hz?",
      "options": [
        "3.3 × 10^-19 J",
        "3.3 × 10^-18 J",
        "3.3 × 10^-20 J",
        "3.3 × 10^-17 J"
      ],
      "answer": "3.3 × 10^-19 J",
      "segment": "Physics"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. Which of the following represents the correct expression for the relativistic mass of an object?",
      "options": [
        "m = m_0/(1 - v^2/c^2)^(1/2)",
        "m = m_0/(1 - v/c)",
        "m = m_0(1 - v^2/c^2)^(1/2)",
        "m = m_0(1 + v^2/c^2)"
      ],
      "answer": "m = m_0/(1 - v^2/c^2)^(1/2)",
      "segment": "Physics"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. Which element is the most abundant in the Earth's crust?",
      "options": ["Oxygen", "Silicon", "Aluminum", "Iron"],
      "answer": "Oxygen",
      "segment": "Chemistry"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. What is the chemical formula of water?",
      "options": ["H2O", "CO2", "NaCl", "H2O2"],
      "answer": "H2O",
      "segment": "Chemistry"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. Which of the following is a noble gas?",
      "options": ["Oxygen", "Helium", "Nitrogen", "Hydrogen"],
      "answer": "Helium",
      "segment": "Chemistry"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. What is the SI unit of amount of substance?",
      "options": ["Kilogram", "Mole", "Litre", "Ampere"],
      "answer": "Mole",
      "segment": "Chemistry"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which acid is commonly found in vinegar?",
      "options": ["Acetic acid", "Hydrochloric acid", "Sulfuric acid", "Citric acid"],
      "answer": "Acetic acid",
      "segment": "Chemistry"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. What is the hybridization of carbon in methane (CH4)?",
      "options": ["sp", "sp2", "sp3", "sp3d"],
      "answer": "sp3",
      "segment": "Chemistry"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. Which gas is produced when zinc reacts with dilute hydrochloric acid?",
      "options": ["Oxygen", "Hydrogen", "Chlorine", "Nitrogen"],
      "answer": "Hydrogen",
      "segment": "Chemistry"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. Which of the following is an example of a primary alcohol?",
      "options": ["Methanol", "Propan-2-ol", "2-methylpropan-2-ol", "Phenol"],
      "answer": "Methanol",
      "segment": "Chemistry"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What is the IUPAC name of CH3-CH=CH-CH3?",
      "options": ["Butane", "Butene", "1-Butene", "2-Butene"],
      "answer": "2-Butene",
      "segment": "Chemistry"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. What type of bond is present in a molecule of nitrogen (N2)?",
      "options": ["Single bond", "Double bond", "Triple bond", "Ionic bond"],
      "answer": "Triple bond",
      "segment": "Chemistry"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. What is the molecular geometry of SF6?",
      "options": ["Tetrahedral", "Square planar", "Trigonal bipyramidal", "Octahedral"],
      "answer": "Octahedral",
      "segment": "Chemistry"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which type of isomerism is shown by [Pt(NH3)2Cl2]?",
      "options": ["Geometrical", "Optical", "Ionization", "Linkage"],
      "answer": "Geometrical",
      "segment": "Chemistry"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. Which of the following is a crystalline solid?",
      "options": ["Glass", "Quartz", "Plastic", "Rubber"],
      "answer": "Quartz",
      "segment": "Chemistry"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. Which reagent is used in the Wurtz reaction?",
      "options": ["Sodium in dry ether", "AlCl3 in benzene", "KMnO4 in acidic medium", "Zn in HCl"],
      "answer": "Sodium in dry ether",
      "segment": "Chemistry"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. What is the name of the process by which a solid directly changes into a gas?",
      "options": ["Sublimation", "Condensation", "Vaporization", "Deposition"],
      "answer": "Sublimation",
      "segment": "Chemistry"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the derivative of x²?",
      "options": ["2x", "x", "x²", "1"],
      "answer": "2x",
      "segment": "Maths"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. What is the value of sin(90°)?",
      "options": ["0", "1", "-1", "0.5"],
      "answer": "1",
      "segment": "Maths"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. Which of the following is the value of π (pi) up to two decimal places?",
      "options": ["3.12", "3.14", "3.15", "3.16"],
      "answer": "3.14",
      "segment": "Maths"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. What is the solution of the equation 2x + 6 = 0?",
      "options": ["3", "-3", "0", "6"],
      "answer": "-3",
      "segment": "Maths"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. What is the area of a triangle with base 4 and height 3?",
      "options": ["12", "7", "6", "10"],
      "answer": "6",
      "segment": "Maths"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the integral of 3x²?",
      "options": ["x³", "x³ + C", "3x³", "x⁴ + C"],
      "answer": "x³ + C",
      "segment": "Maths"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. What is the value of tan(45°)?",
      "options": ["0", "1", "-1", "√3"],
      "answer": "1",
      "segment": "Maths"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∩ B?",
      "options": ["{1, 2}", "{3}", "{}", "{3, 4}"],
      "answer": "{3}",
      "segment": "Maths"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. What is the determinant of the matrix [[1, 2], [3, 4]]?",
      "options": ["2", "-2", "1", "0"],
      "answer": "-2",
      "segment": "Maths"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. What is the value of log₃(9)?",
      "options": ["1", "2", "3", "0"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. What is the derivative of e^(x²)?",
      "options": ["2xe^(x²)", "e^(x²)", "x²e^(x²)", "0"],
      "answer": "2xe^(x²)",
      "segment": "Maths"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What is the radius of a circle whose equation is x² + y² - 4x - 6y + 9 = 0?",
      "options": ["1", "2", "3", "5"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. Find the solution set of the inequality 2x - 5 > 1.",
      "options": ["x > 3", "x < 3", "x > 2", "x < 2"],
      "answer": "x > 3",
      "segment": "Maths"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. If the sum of the roots of a quadratic equation is 7 and the product is 10, what is the equation?",
      "options": ["x² - 7x + 10 = 0", "x² + 7x + 10 = 0", "x² + 7x - 10 = 0", "x² - 7x - 10 = 0"],
      "answer": "x² - 7x + 10 = 0",
      "segment": "Maths"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. Evaluate ∫(1/(1 + x²)) dx.",
      "options": ["ln(1 + x²) + C", "tan⁻¹(x) + C", "x + C", "e^x + C"],
      "answer": "tan⁻¹(x) + C",
      "segment": "Maths"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. Which is the powerhouse of the cell?",
      "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
      "answer": "Mitochondria",
      "segment": "Bio"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. What is the main photosynthetic pigment in plants?",
      "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
      "answer": "Chlorophyll",
      "segment": "Bio"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. What is the basic unit of heredity?",
      "options": ["Gene", "Chromosome", "DNA", "RNA"],
      "answer": "Gene",
      "segment": "Bio"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. Which part of the brain controls balance and coordination?",
      "options": ["Cerebrum", "Cerebellum", "Medulla", "Pons"],
      "answer": "Cerebellum",
      "segment": "Bio"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. What is the mode of nutrition in fungi?",
      "options": ["Autotrophic", "Heterotrophic", "Saprophytic", "Parasitic"],
      "answer": "Saprophytic",
      "segment": "Bio"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. Which enzyme is responsible for the transcription of RNA from DNA?",
      "options": ["DNA polymerase", "RNA polymerase", "Ligase", "Helicase"],
      "answer": "RNA polymerase",
      "segment": "Bio"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. What is the function of hemoglobin in the blood?",
      "options": ["Transport oxygen", "Clot blood", "Fight infection", "Regulate pH"],
      "answer": "Transport oxygen",
      "segment": "Bio"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. Which hormone is secreted by the adrenal medulla?",
      "options": ["Insulin", "Glucagon", "Epinephrine", "Thyroxine"],
      "answer": "Epinephrine",
      "segment": "Bio"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. What is the term for the exchange of genetic material between homologous chromosomes during meiosis?",
      "options": ["Mutation", "Transcription", "Crossing over", "Replication"],
      "answer": "Crossing over",
      "segment": "Bio"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. Which component of the blood helps in clotting?",
      "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"],
      "answer": "Platelets",
      "segment": "Bio"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. Which part of the nephron is primarily responsible for the reabsorption of glucose?",
      "options": ["Bowman's capsule", "Proximal convoluted tubule", "Loop of Henle", "Distal convoluted tubule"],
      "answer": "Proximal convoluted tubule",
      "segment": "Bio"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. What is the role of restriction enzymes in genetic engineering?",
      "options": ["Cut DNA at specific sites", "Replicate DNA", "Bind DNA fragments", "Synthesize RNA"],
      "answer": "Cut DNA at specific sites",
      "segment": "Bio"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. Which type of immunity is provided by vaccines?",
      "options": ["Active natural immunity", "Active artificial immunity", "Passive natural immunity", "Passive artificial immunity"],
      "answer": "Active artificial immunity",
      "segment": "Bio"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. Which process converts nitrogen gas into ammonia in the nitrogen cycle?",
      "options": ["Nitrification", "Nitrogen fixation", "Ammonification", "Denitrification"],
      "answer": "Nitrogen fixation",
      "segment": "Bio"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the genetic material in retroviruses?",
      "options": ["DNA", "RNA", "Proteins", "Carbohydrates"],
      "answer": "RNA",
      "segment": "Bio"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the synonym of the word 'Happy'?",
      "options": ["Sad", "Elated", "Angry", "Confused"],
      "answer": "Elated",
      "segment": "English"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Which of the following is a verb?",
      "options": ["Run", "Beautiful", "Quickly", "Happiness"],
      "answer": "Run",
      "segment": "English"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. Identify the correct sentence:",
      "options": [
        "She are going to school.",
        "She is going to school.",
        "She am going to school.",
        "She was going to school."
      ],
      "answer": "She is going to school.",
      "segment": "English"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. What is the plural form of 'Child'?",
      "options": ["Childs", "Childrens", "Children", "Child"],
      "answer": "Children",
      "segment": "English"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. Which article should be used before the word 'apple'?",
      "options": ["A", "An", "The", "No article"],
      "answer": "An",
      "segment": "English"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is the antonym of the word 'Generous'?",
      "options": ["Kind", "Selfish", "Benevolent", "Gracious"],
      "answer": "Selfish",
      "segment": "English"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Identify the correct passive form of the sentence: 'She writes a letter.'",
      "options": [
        "A letter is written by her.",
        "A letter was written by her.",
        "A letter has been written by her.",
        "A letter will be written by her."
      ],
      "answer": "A letter is written by her.",
      "segment": "English"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. Which figure of speech is used in the sentence 'The world is a stage'?",
      "options": ["Simile", "Metaphor", "Hyperbole", "Personification"],
      "answer": "Metaphor",
      "segment": "English"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. What is the meaning of the idiom 'A blessing in disguise'?",
      "options": [
        "A fortunate event hidden in misfortune",
        "A secret gift",
        "A disguised enemy",
        "A sudden blessing"
      ],
      "answer": "A fortunate event hidden in misfortune",
      "segment": "English"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. Choose the correctly punctuated sentence:",
      "options": [
        "It's a beautiful day isnt it?",
        "Its a beautiful day, isn't it?",
        "It's a beautiful day, isn't it?",
        "Its a beautiful day isnt it."
      ],
      "answer": "It's a beautiful day, isn't it?",
      "segment": "English"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. Which of the following is an example of a complex sentence?",
      "options": [
        "She loves to dance and sing.",
        "Although it was raining, we went for a walk.",
        "I will call you tomorrow.",
        "She is a teacher."
      ],
      "answer": "Although it was raining, we went for a walk.",
      "segment": "English"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Which tense is used in the sentence: 'He will have completed his project by next month'?",
      "options": [
        "Future Perfect",
        "Future Continuous",
        "Future Simple",
        "Future Perfect Continuous"
      ],
      "answer": "Future Perfect",
      "segment": "English"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. What is the difference between 'affect' and 'effect'?",
      "options": [
        "'Affect' is a noun, 'effect' is a verb.",
        "'Affect' is a verb, 'effect' is a noun.",
        "Both are nouns.",
        "Both are verbs."
      ],
      "answer": "'Affect' is a verb, 'effect' is a noun.",
      "segment": "English"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. Which literary device is used in the sentence: 'The thunder roared like a lion'?",
      "options": ["Personification", "Simile", "Alliteration", "Hyperbole"],
      "answer": "Simile",
      "segment": "English"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. What is the main clause in the sentence: 'When the rain stopped, we went outside to play'?",
      "options": [
        "'When the rain stopped'",
        "'We went outside to play'",
        "'To play'",
        "'The rain stopped'"
      ],
      "answer": "'We went outside to play'",
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
