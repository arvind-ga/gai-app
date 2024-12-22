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
  "id": "3_10_allsub",
  "questions": [
    {
      "id": "1",
      "question": "1. Which of the following is a prime number?",
      "options": ["33", "39", "29", "25"],
      "answer": "29",
      "segment": "maths",
      "difficulty": "Easy"

    },
    {
      "id": "2",
      "question": "2. If x + 2 = 7, then the value of 3x is:",
      "options": ["10", "15", "12", "9"],
      "answer": "15",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "3",
      "question": "3. If the perimeter of a rectangle is 36 cm and its length is 10 cm, what is its breadth?",
      "options": ["8 cm", "6 cm", "9 cm", "7 cm"],
      "answer": "6 cm",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "4",
      "question": "4. If the area of a circle is 49π sq. cm, what is its radius?",
      "options": ["4 cm", "5 cm", "6 cm", "7 cm"],
      "answer": "7 cm",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "5",
      "question": "5. The value of 15/100 × 500 is:",
      "options": ["60", "50", "75", "45"],
      "answer": "75",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "6",
      "question": "6. What is the LCM of 12 and 18?",
      "options": ["36", "24", "72", "18"],
      "answer": "36",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "7",
      "question": "7. What is the perimeter of a square whose area is 81 sq. cm?",
      "options": ["36 cm", "40 cm", "30 cm", "42 cm"],
      "answer": "36 cm",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "8",
      "question": "8. If a = 2 and b = 3, then the value of a² + b² - 2ab is:",
      "options": ["0", "1", "2", "4"],
      "answer": "1",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "9",
      "question": "9. What is the cube root of 512?",
      "options": ["6", "7", "8", "9"],
      "answer": "8",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "10",
      "question": "10. The simple interest on Rs. 8000 for 2 years at an annual interest rate of 5% is:",
      "options": ["Rs. 400", "Rs. 600", "Rs. 800", "Rs. 900"],
      "answer": "Rs. 800",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "11",
      "question": "11. The average of the numbers 10, 20, 30, 40, 50 is:",
      "options": ["20", "30", "40", "50"],
      "answer": "30",
      "segment": "maths",
      "difficulty": "Easy"
    },
    {
      "id": "12",
      "question": "12. The ratio of 5 liters to 500 milliliters is:",
      "options": ["10:1", "1:10", "5:1", "2:1"],
      "answer": "10:1",
      "segment": "maths",
      "difficulty": "Medium"
    },
    {
      "id": "13",
      "question": "13. What is the value of 100/0.25?",
      "options": ["400", "250", "50", "500"],
      "answer": "400",
      "segment": "maths",
      "difficulty": "Medium"
    },
    {
      "id": "14",
      "question": "14. If x² = 64, what is the value of x?",
      "options": ["8", "-8", "±8", "16"],
      "answer": "±8",
      "segment": "maths",
      "difficulty": "Medium"
    },
    {
      "id": "15",
      "question": "15. Which of the following is a Pythagorean triplet?",
      "options": ["3, 4, 6", "5, 12, 13", "7, 24, 25", "Both b) and c)"],
      "answer": "Both b) and c)",
      "segment": "maths",
      "difficulty": "Medium"
    },
{
      "id": "16",
      "question": "16. What is the SI unit of force?",
      "options": ["Joule", "Newton", "Watt", "Pascal"],
      "answer": "Newton",
      "segment": "physics",
      "difficulty": "Easy"
    },
    {
      "id": "17",
      "question": "17. Which of the following is a scalar quantity?",
      "options": ["Velocity", "Force", "Speed", "Displacement"],
      "answer": "Speed",
      "segment": "physics",
      "difficulty": "Easy"
    },
    {
      "id": "18",
      "question": "18. If an object is moving with constant velocity, what is the net force acting on it?",
      "options": ["Zero", "Equal to its mass", "Greater than its weight", "Constant"],
      "answer": "Zero",
      "segment": "physics",
      "difficulty": "Easy"
    },
    {
      "id": "19",
      "question": "19. What is the relation between mass (m), acceleration (a), and force (F)?",
      "options": ["F = ma", "F = m/a", "F = m + a", "F = m - a"],
      "answer": "F = ma",
      "segment": "physics",
      "difficulty": "Easy"
    },
    {
      "id": "20",
      "question": "20. In which medium does sound travel the fastest?",
      "options": ["Solid", "Liquid", "Gas", "Vacuum"],
      "answer": "Solid",
      "segment": "physics",
      "difficulty": "Medium"
    },
    {
      "id": "21",
      "question": "21. Which of the following phenomena explains why we see lightning before hearing thunder?",
      "options": [
        "Sound travels faster than light",
        "Light travels faster than sound",
        "Both travel at the same speed",
        "Light is absorbed while sound is not"
      ],
      "answer": "Light travels faster than sound",
      "segment": "physics",
      "difficulty": "Medium"
    },
    {
      "id": "22",
      "question": "22. Which of the following energy transformations occurs in a hydroelectric power plant?",
      "options": [
        "Kinetic to Potential",
        "Electrical to Mechanical",
        "Potential to Electrical",
        "Thermal to Electrical"
      ],
      "answer": "Potential to Electrical",
      "segment": "physics",
      "difficulty": "Medium"
    },
    {
      "id": "23",
      "question": "23. A freely falling object experiences...",
      "options": [
        "Constant velocity",
        "Increasing acceleration",
        "Constant acceleration",
        "No acceleration"
      ],
      "answer": "Constant acceleration",
      "segment": "physics",
      "difficulty": "Hard"
    },
    {
      "id": "24",
      "question": "24. What is the kinetic energy of an object with a mass of 2 kg moving at 3 m/s?",
      "options": ["6 J", "9 J", "12 J", "18 J"],
      "answer": "18 J",
      "segment": "physics",
      "difficulty": "Hard"
    },
    {
      "id": "25",
      "question": "25. What is the frequency of a wave if its time period is 0.01 seconds?",
      "options": ["10 Hz", "50 Hz", "100 Hz", "200 Hz"],
      "answer": "100 Hz",
      "segment": "physics",
      "difficulty": "Hard"
    },
{
            "id": "26",
            "question": "26. Which of the following is NOT a chemical change?",
            "options": ["Rusting of iron", "Burning of paper", "Melting of ice", "Cooking of food"],
            "answer": "Melting of ice",
            "segment": "chemistry",
            "difficulty": "Easy"
        },
        {
            "id": "27",
            "question": "27. The chemical symbol for Sodium is...",
            "options": ["Na", "S", "So", "Sn"],
            "answer": "Na",
            "segment": "chemistry",
            "difficulty": "Easy"
        },
        {
            "id": "28",
            "question": "28. The number of protons in the nucleus of an atom is called its...",
            "options": ["Mass number", "Atomic number", "Neutron number", "Valency"],
            "answer": "Atomic number",
            "segment": "chemistry",
            "difficulty": "Easy"
        },
        {
            "id": "29",
            "question": "29. Which of the following is a heterogeneous mixture?",
            "options": ["Air", "Saltwater", "Sand and water", "Sugar solution"],
            "answer": "Sand and water",
            "segment": "chemistry",
            "difficulty": "Easy"
        },
        {
            "id": "30",
            "question": "30. Which of the following elements is a noble gas?",
            "options": ["Oxygen", "Helium", "Hydrogen", "Carbon"],
            "answer": "Helium",
            "segment": "chemistry",
            "difficulty": "Medium"
        },
        {
            "id": "31",
            "question": "31. The pH of a neutral solution at 25°C is...",
            "options": ["0", "7", "14", "3"],
            "answer": "7",
            "segment": "chemistry",
            "difficulty": "Medium"
        },
        {
            "id": "32",
            "question": "32. Which of the following methods can be used to separate salt from seawater?",
            "options": ["Filtration", "Distillation", "Chromatography", "Sublimation"],
            "answer": "Distillation",
            "segment": "chemistry",
            "difficulty": "Medium"
        },
        {
            "id": "33",
            "question": "33. In the periodic table, elements in the same group have the same...",
            "options": ["Atomic number", "Number of protons", "Number of valence electrons", "Number of neutrons"],
            "answer": "Number of valence electrons",
            "segment": "chemistry",
            "difficulty": "Hard"
        },
        {
            "id": "34",
            "question": "34. Which of the following metals reacts vigorously with water?",
            "options": ["Copper", "Magnesium", "Potassium", "Iron"],
            "answer": "Potassium",
            "segment": "chemistry",
            "difficulty": "Hard"
        },
        {
            "id": "35",
            "question": "35. Which of the following is an alloy?",
            "options": ["Water", "Brass", "Gold", "Diamond"],
            "answer": "Brass",
            "segment": "chemistry",
            "difficulty": "Hard"
        },
{
      "id": "36",
      "question": "36. Which of the following is the basic structural and functional unit of life?",
      "options": ["Tissue", "Organ", "Cell", "Organ system"],
      "answer": "Cell",
      "segment": "bio",
      "difficulty": "Easy"
    },
    {
      "id": "37",
      "question": "37. Which cell organelle is known as the ‘powerhouse’ of the cell?",
      "options": ["Nucleus", "Mitochondria", "Ribosomes", "Golgi apparatus"],
      "answer": "Mitochondria",
      "segment": "bio",
      "difficulty": "Easy"
    },
    {
      "id": "38",
      "question": "38. What is the main function of the xylem in plants?",
      "options": ["Transport of water", "Transport of food", "Photosynthesis", "Reproduction"],
      "answer": "Transport of water",
      "segment": "bio",
      "difficulty": "Easy"
    },
    {
      "id": "39",
      "question": "39. In which part of the plant does photosynthesis take place?",
      "options": ["Stem", "Roots", "Flowers", "Leaves"],
      "answer": "Leaves",
      "segment": "bio",
      "difficulty": "Easy"
    },
    {
      "id": "40",
      "question": "40. The green pigment in plants responsible for photosynthesis is:",
      "options": ["Chloroplast", "Chlorophyll", "Cytoplasm", "Mitochondria"],
      "answer": "Chlorophyll",
      "segment": "bio",
      "difficulty": "Easy"
    },
    {
      "id": "41",
      "question": "41. Which of the following organisms are prokaryotic?",
      "options": ["Fungi", "Bacteria", "Protists", "Plants"],
      "answer": "Bacteria",
      "segment": "bio",
      "difficulty": "Medium"
    },
    {
      "id": "42",
      "question": "42. Which part of the human body is primarily responsible for absorbing nutrients from food?",
      "options": ["Stomach", "Large intestine", "Small intestine", "Liver"],
      "answer": "Small intestine",
      "segment": "bio",
      "difficulty": "Medium"
    },
    {
      "id": "43",
      "question": "43. The process of cell division in which a single cell divides into two identical daughter cells is called:",
      "options": ["Mitosis", "Meiosis", "Fertilization", "Osmosis"],
      "answer": "Mitosis",
      "segment": "bio",
      "difficulty": "Medium"
    },
    {
      "id": "44",
      "question": "44. Which of the following is NOT a characteristic of living organisms?",
      "options": ["Reproduction", "Growth", "Respiration", "Decay"],
      "answer": "Decay",
      "segment": "bio",
      "difficulty": "Medium"
    },
    {
      "id": "45",
      "question": "45. Which of the following is a genetic material?",
      "options": ["DNA", "RNA", "Both DNA and RNA", "Lipids"],
      "answer": "Both DNA and RNA",
      "segment": "bio",
      "difficulty": "Medium"
    },
    {
      "id": "46",
      "question": "46. Which disease is caused by a deficiency of Vitamin C?",
      "options": ["Beriberi", "Scurvy", "Rickets", "Pellagra"],
      "answer": "Scurvy",
      "segment": "bio",
      "difficulty": "Hard"
    },
    {
      "id": "47",
      "question": "47. Which of the following organelles is responsible for protein synthesis?",
      "options": ["Golgi apparatus", "Ribosome", "Mitochondria", "Lysosome"],
      "answer": "Ribosome",
      "segment": "bio",
      "difficulty": "Hard"
    },
    {
      "id": "48",
      "question": "48. Which type of blood vessel carries blood away from the heart?",
      "options": ["Veins", "Arteries", "Capillaries", "Lymph vessels"],
      "answer": "Arteries",
      "segment": "bio",
      "difficulty": "Hard"
    },
    {
      "id": "49",
      "question": "49. What is the function of the enzyme amylase?",
      "options": ["Breaks down fats", "Breaks down proteins", "Breaks down starch into sugars", "Breaks down nucleic acids"],
      "answer": "Breaks down starch into sugars",
      "segment": "bio",
      "difficulty": "Hard"
    },
    {
      "id": "50",
      "question": "50. Which part of the brain controls balance and coordination?",
      "options": ["Cerebrum", "Cerebellum", "Medulla", "Pons"],
      "answer": "Cerebellum",
      "segment": "bio",
      "difficulty": "Hard"
    },
{
      "id": "51",
      "question": "51. What was the main aim of the French Revolution?",
      "options": ["To abolish monarchy", "To gain independence from British rule", "To expand French colonies", "To increase taxes on the poor"],
      "answer": "To abolish monarchy",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "52",
      "question": "52. Which of the following is not a characteristic of democracy?",
      "options": ["Free and fair elections", "Equal rights for all citizens", "Hereditary monarchy", "Rule of law"],
      "answer": "Hereditary monarchy",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "53",
      "question": "53. The Earth’s lithosphere consists of which of the following?",
      "options": ["Water and air", "Soil and rocks", "Plants and animals", "Ice and snow"],
      "answer": "Soil and rocks",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "54",
      "question": "54. Which of the following countries is not a member of the SAARC?",
      "options": ["India", "China", "Pakistan", "Nepal"],
      "answer": "China",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "55",
      "question": "55. Which of the following is a Rabi crop?",
      "options": ["Wheat", "Rice", "Cotton", "Jute"],
      "answer": "Wheat",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "56",
      "question": "56. Which river is known as the 'Sorrow of Bengal'?",
      "options": ["Ganga", "Yamuna", "Damodar", "Brahmaputra"],
      "answer": "Damodar",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "57",
      "question": "57. Who is known as the ‘Father of Indian Constitution’?",
      "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Patel"],
      "answer": "B.R. Ambedkar",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "58",
      "question": "58. Which revolution is related to the increase in milk production in India?",
      "options": ["Green Revolution", "White Revolution", "Blue Revolution", "Yellow Revolution"],
      "answer": "White Revolution",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "59",
      "question": "59. What is the significance of the Tropic of Cancer for India?",
      "options": ["Divides India into two equal halves", "Marks the boundary of Indian monsoon region", "Separates northern and southern plains", "Passes through the central part of India"],
      "answer": "Passes through the central part of India",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "60",
      "question": "60. Which of the following is a natural cause of soil erosion?",
      "options": ["Deforestation", "Floods", "Urbanization", "Agriculture"],
      "answer": "Floods",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "61",
      "question": "61. The fundamental right to equality ensures which of the following?",
      "options": ["Equal pay for equal work", "Equal treatment under the law", "Equal education for all", "Equality in income"],
      "answer": "Equal treatment under the law",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "62",
      "question": "62. What was the main feature of the Indian economy before British rule?",
      "options": ["Industrial economy", "Agrarian economy", "Socialist economy", "Capitalist economy"],
      "answer": "Agrarian economy",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "63",
      "question": "63. In which year was the Quit India Movement launched?",
      "options": ["1930", "1942", "1945", "1950"],
      "answer": "1942",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "64",
      "question": "64. Which of the following is a biotic component of the environment?",
      "options": ["Rocks", "Air", "Animals", "Water"],
      "answer": "Animals",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "65",
      "question": "65. Who was the first President of India?",
      "options": ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Sardar Patel", "Dr. B.R. Ambedkar"],
      "answer": "Dr. Rajendra Prasad",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "66",
      "question": "66. Which country’s constitution influenced the Indian Constitution the most in terms of fundamental rights?",
      "options": ["USA", "UK", "France", "Canada"],
      "answer": "USA",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "67",
      "question": "67. The type of farming in which crops are grown to meet the needs of the farmer’s family is known as:",
      "options": ["Commercial farming", "Subsistence farming", "Organic farming", "Plantation farming"],
      "answer": "Subsistence farming",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "68",
      "question": "68. What is the primary source of energy for the Earth’s climate system?",
      "options": ["The moon", "The sun", "Earth’s core", "The atmosphere"],
      "answer": "The sun",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "69",
      "question": "69. Which of the following is the oldest mountain range in India?",
      "options": ["Himalayas", "Western Ghats", "Aravalli", "Vindhyas"],
      "answer": "Aravalli",
      "segment": "sst",
      "difficulty": "Easy"
    },
    {
      "id": "70",
      "question": "70. Which movement was started by Mahatma Gandhi in 1919 against the Rowlatt Act?",
      "options": ["Non-Cooperation Movement", "Salt Satyagraha", "Civil Disobedience Movement", "Satyagraha Movement"],
      "answer": "Satyagraha Movement",
      "segment": "sst",
      "difficulty": "Easy"
    }
  ]
}


###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizes.insert_one(quiz_data)
