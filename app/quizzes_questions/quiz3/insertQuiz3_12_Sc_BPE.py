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
quiz_data = { "id": "3_12_sc_bpe",
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
      "question": "31. Which is the powerhouse of the cell?",
      "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
      "answer": "Mitochondria",
      "segment": "Bio"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. What is the main photosynthetic pigment in plants?",
      "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
      "answer": "Chlorophyll",
      "segment": "Bio"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. What is the basic unit of heredity?",
      "options": ["Gene", "Chromosome", "DNA", "RNA"],
      "answer": "Gene",
      "segment": "Bio"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. Which part of the brain controls balance and coordination?",
      "options": ["Cerebrum", "Cerebellum", "Medulla", "Pons"],
      "answer": "Cerebellum",
      "segment": "Bio"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. What is the mode of nutrition in fungi?",
      "options": ["Autotrophic", "Heterotrophic", "Saprophytic", "Parasitic"],
      "answer": "Saprophytic",
      "segment": "Bio"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. Which enzyme is responsible for the transcription of RNA from DNA?",
      "options": ["DNA polymerase", "RNA polymerase", "Ligase", "Helicase"],
      "answer": "RNA polymerase",
      "segment": "Bio"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. What is the function of hemoglobin in the blood?",
      "options": ["Transport oxygen", "Clot blood", "Fight infection", "Regulate pH"],
      "answer": "Transport oxygen",
      "segment": "Bio"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. Which hormone is secreted by the adrenal medulla?",
      "options": ["Insulin", "Glucagon", "Epinephrine", "Thyroxine"],
      "answer": "Epinephrine",
      "segment": "Bio"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. What is the term for the exchange of genetic material between homologous chromosomes during meiosis?",
      "options": ["Mutation", "Transcription", "Crossing over", "Replication"],
      "answer": "Crossing over",
      "segment": "Bio"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. Which component of the blood helps in clotting?",
      "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"],
      "answer": "Platelets",
      "segment": "Bio"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. Which part of the nephron is primarily responsible for the reabsorption of glucose?",
      "options": ["Bowman's capsule", "Proximal convoluted tubule", "Loop of Henle", "Distal convoluted tubule"],
      "answer": "Proximal convoluted tubule",
      "segment": "Bio"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What is the role of restriction enzymes in genetic engineering?",
      "options": ["Cut DNA at specific sites", "Replicate DNA", "Bind DNA fragments", "Synthesize RNA"],
      "answer": "Cut DNA at specific sites",
      "segment": "Bio"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. Which type of immunity is provided by vaccines?",
      "options": ["Active natural immunity", "Active artificial immunity", "Passive natural immunity", "Passive artificial immunity"],
      "answer": "Active artificial immunity",
      "segment": "Bio"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Which process converts nitrogen gas into ammonia in the nitrogen cycle?",
      "options": ["Nitrification", "Nitrogen fixation", "Ammonification", "Denitrification"],
      "answer": "Nitrogen fixation",
      "segment": "Bio"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. What is the genetic material in retroviruses?",
      "options": ["DNA", "RNA", "Proteins", "Carbohydrates"],
      "answer": "RNA",
      "segment": "Bio"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. What is the synonym of the word 'Happy'?",
      "options": ["Sad", "Elated", "Angry", "Confused"],
      "answer": "Elated",
      "segment": "English"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. Which of the following is a verb?",
      "options": ["Run", "Beautiful", "Quickly", "Happiness"],
      "answer": "Run",
      "segment": "English"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. Identify the correct sentence:",
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
      "id": 49,
      "difficulty": "Easy",
      "question": "49. What is the plural form of 'Child'?",
      "options": ["Childs", "Childrens", "Children", "Child"],
      "answer": "Children",
      "segment": "English"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. Which article should be used before the word 'apple'?",
      "options": ["A", "An", "The", "No article"],
      "answer": "An",
      "segment": "English"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. What is the antonym of the word 'Generous'?",
      "options": ["Kind", "Selfish", "Benevolent", "Gracious"],
      "answer": "Selfish",
      "segment": "English"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. Identify the correct passive form of the sentence: 'She writes a letter.'",
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
      "id": 53,
      "difficulty": "Medium",
      "question": "53. Which figure of speech is used in the sentence 'The world is a stage'?",
      "options": ["Simile", "Metaphor", "Hyperbole", "Personification"],
      "answer": "Metaphor",
      "segment": "English"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. What is the meaning of the idiom 'A blessing in disguise'?",
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
      "id": 55,
      "difficulty": "Medium",
      "question": "55. Choose the correctly punctuated sentence:",
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
      "id": 56,
      "difficulty": "Hard",
      "question": "56. Which of the following is an example of a complex sentence?",
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
      "id": 57,
      "difficulty": "Hard",
      "question": "57. Which tense is used in the sentence: 'He will have completed his project by next month'?",
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
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What is the difference between 'affect' and 'effect'?",
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
      "id": 59,
      "difficulty": "Hard",
      "question": "59. Which literary device is used in the sentence: 'The thunder roared like a lion'?",
      "options": ["Personification", "Simile", "Alliteration", "Hyperbole"],
      "answer": "Simile",
      "segment": "English"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the main clause in the sentence: 'When the rain stopped, we went outside to play'?",
      "options": [
        "'When the rain stopped'",
        "'We went outside to play'",
        "'To play'",
        "'The rain stopped'"
      ],
      "answer": "'We went outside to play'",
      "segment": "English"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the primary source of energy for human muscles?",
      "options": ["Proteins", "Carbohydrates", "Fats", "Vitamins"],
      "answer": "Carbohydrates",
      "segment": "physical_education"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. The process of warming up before exercise helps in:",
      "options": ["Increased muscle flexibility", "Reducing injury", "Improving performance", "All of the above"],
      "answer": "All of the above",
      "segment": "physical_education"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. Which of the following is a component of physical fitness?",
      "options": ["Strength", "Endurance", "Flexibility", "All of the above"],
      "answer": "All of the above",
      "segment": "physical_education"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. The ‘push-up’ is a type of exercise that primarily targets which muscles?",
      "options": ["Abdominals", "Legs", "Chest and arms", "Back"],
      "answer": "Chest and arms",
      "segment": "physical_education"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. What is the primary purpose of physical education?",
      "options": ["To promote mental well-being", "To maintain physical fitness", "To develop sports skills", "All of the above"],
      "answer": "All of the above",
      "segment": "physical_education"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. Which type of training is best for improving cardiovascular endurance?",
      "options": ["Strength training", "Flexibility training", "Aerobic training", "Anaerobic training"],
      "answer": "Aerobic training",
      "segment": "physical_education"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. In which sport is the concept of ‘Lateral Movement’ crucial?",
      "options": ["Basketball", "Football", "Tennis", "All of the above"],
      "answer": "All of the above",
      "segment": "physical_education"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What is the correct order of the stages in a warm-up routine?",
      "options": ["General warm-up, stretching, specific warm-up", "Stretching, general warm-up, specific warm-up", "Specific warm-up, stretching, general warm-up", "Stretching, specific warm-up, general warm-up"],
      "answer": "General warm-up, stretching, specific warm-up",
      "segment": "physical_education"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. The 'Overload Principle' in exercise suggests that:",
      "options": ["You should exercise without rest", "You should exercise at maximum intensity", "You should gradually increase exercise intensity", "You should exercise for longer periods of time"],
      "answer": "You should gradually increase exercise intensity",
      "segment": "physical_education"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. Which of the following is a benefit of strength training?",
      "options": ["Increased muscle mass", "Increased bone density", "Improved metabolic rate", "All of the above"],
      "answer": "All of the above",
      "segment": "physical_education"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. What is the 'FITT' principle in exercise?",
      "options": ["Frequency, Intensity, Time, Type", "Frequency, Intensity, Test, Type", "Fitness, Intensity, Time, Type", "Force, Intensity, Time, Technique"],
      "answer": "Frequency, Intensity, Time, Type",
      "segment": "physical_education"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Which of the following is a recommended method to improve flexibility?",
      "options": ["Static stretching", "Dynamic stretching", "Ballistic stretching", "All of the above"],
      "answer": "Static stretching",
      "segment": "physical_education"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. The ‘Three Energy Systems’ include all of the following EXCEPT:",
      "options": ["Phosphagen system", "Glycolytic system", "Aerobic system", "Circulatory system"],
      "answer": "Circulatory system",
      "segment": "physical_education"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. The principle of ‘Specificity’ in exercise suggests that:",
      "options": ["The body will adapt to the type of exercise performed", "Exercises must be performed at maximum intensity", "Exercise must be performed for a long duration", "Exercises must be performed in a group setting"],
      "answer": "The body will adapt to the type of exercise performed",
      "segment": "physical_education"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. Which of the following is true about lactic acid buildup during exercise?",
      "options": ["It occurs during anaerobic exercise", "It is beneficial for muscle recovery", "It results from aerobic exercise", "It is broken down in the presence of oxygen"],
      "answer": "It occurs during anaerobic exercise",
      "segment": "physical_education"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
