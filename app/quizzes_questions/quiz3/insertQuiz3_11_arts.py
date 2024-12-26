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
quiz_data = {"id": "3_11_arts",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. Who was the founder of the Maurya Empire?",
      "options": ["Ashoka", "Bindusara", "Chandragupta Maurya", "Chanakya"],
      "answer": "Chandragupta Maurya",
      "segment": "history"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. What is the main source of information about the Indus Valley Civilization?",
      "options": ["Vedas", "Archaeological remains", "Buddhist texts", "Coins"],
      "answer": "Archaeological remains",
      "segment": "history"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. Who wrote the 'Arthashastra'?",
      "options": ["Kalidasa", "Chanakya", "Valmiki", "Banabhatta"],
      "answer": "Chanakya",
      "segment": "history"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. What was the primary occupation of the people of the Indus Valley Civilization?",
      "options": ["Hunting", "Farming", "Fishing", "Trade"],
      "answer": "Farming",
      "segment": "history"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. Which Indian king is known for embracing Buddhism after the Kalinga War?",
      "options": ["Chandragupta Maurya", "Ashoka", "Harsha", "Kanishka"],
      "answer": "Ashoka",
      "segment": "history"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. Which Mughal emperor is known as 'Zinda Pir' or 'Living Saint'?",
      "options": ["Akbar", "Aurangzeb", "Shah Jahan", "Jahangir"],
      "answer": "Aurangzeb",
      "segment": "history"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. Who established the 'Gupta Empire' in ancient India?",
      "options": ["Chandragupta I", "Samudragupta", "Chandragupta II", "Skandagupta"],
      "answer": "Chandragupta I",
      "segment": "history"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. The Iron Pillar at Mehrauli in Delhi was erected during which dynasty?",
      "options": ["Maurya", "Gupta", "Kushan", "Chola"],
      "answer": "Gupta",
      "segment": "history"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. Who was the author of 'Prithviraj Raso'?",
      "options": ["Tulsidas", "Kalhana", "Chand Bardai", "Banabhatta"],
      "answer": "Chand Bardai",
      "segment": "history"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. Which ruler is associated with the establishment of the Delhi Sultanate?",
      "options": ["Qutb-ud-din Aibak", "Alauddin Khalji", "Iltutmish", "Balban"],
      "answer": "Qutb-ud-din Aibak",
      "segment": "history"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. What is the significance of the rock edicts of Ashoka?",
      "options": [
        "They glorify his military conquests",
        "They provide insights into his administration and spread of Buddhism",
        "They describe the architecture of the Mauryan Empire",
        "They record his alliances with foreign rulers"
      ],
      "answer": "They provide insights into his administration and spread of Buddhism",
      "segment": "history"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. Which dynasty is known for the development of temple architecture in South India?",
      "options": ["Maurya", "Chola", "Gupta", "Satavahana"],
      "answer": "Chola",
      "segment": "history"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. The famous 'Tripartite Struggle' was fought between which kingdoms?",
      "options": [
        "Cholas, Cheras, and Pandyas",
        "Palas, Rashtrakutas, and Pratiharas",
        "Mauryas, Guptas, and Chalukyas",
        "Mughals, Rajputs, and Marathas"
      ],
      "answer": "Palas, Rashtrakutas, and Pratiharas",
      "segment": "history"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. What was the main purpose of the 'Dome of the Rock' built during the Rashidun Caliphate?",
      "options": [
        "It served as a military base",
        "It was a commemorative structure for Prophet Muhammad's night journey",
        "It housed the royal treasury",
        "It was used for astronomical studies"
      ],
      "answer": "It was a commemorative structure for Prophet Muhammad's night journey",
      "segment": "history"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. Who was the founder of the 'Vijayanagara Empire'?",
      "options": ["Harihara I and Bukka I", "Krishnadevaraya", "Devaraya II", "Narasa Nayaka"],
      "answer": "Harihara I and Bukka I",
      "segment": "history"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. Which is the largest continent by area?",
      "options": ["Africa", "Asia", "Europe", "North America"],
      "answer": "Asia",
      "segment": "geography"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. What is the primary source of energy for the Earth?",
      "options": ["Moon", "Sun", "Wind", "Geothermal"],
      "answer": "Sun",
      "segment": "geography"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. What is the longest river in the world?",
      "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
      "answer": "Nile",
      "segment": "geography"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. What is the term for a narrow strip of land connecting two larger landmasses?",
      "options": ["Isthmus", "Strait", "Delta", "Peninsula"],
      "answer": "Isthmus",
      "segment": "geography"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which layer of the Earth contains the tectonic plates?",
      "options": ["Core", "Mantle", "Crust", "Outer Core"],
      "answer": "Crust",
      "segment": "geography"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. What is the term for a seasonal wind in South Asia that brings heavy rainfall?",
      "options": ["Cyclone", "Monsoon", "Hurricane", "Tornado"],
      "answer": "Monsoon",
      "segment": "geography"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. What are the two main types of glaciers?",
      "options": [
        "Continental and Valley",
        "Mountain and Oceanic",
        "Polar and Tropical",
        "Erosional and Depositional"
      ],
      "answer": "Continental and Valley",
      "segment": "geography"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. Which latitude is also known as the Tropic of Cancer?",
      "options": ["0°", "23.5° North", "23.5° South", "66.5° North"],
      "answer": "23.5° North",
      "segment": "geography"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What type of volcano is Mount Vesuvius?",
      "options": [
        "Shield volcano",
        "Cinder cone volcano",
        "Stratovolcano",
        "Caldera"
      ],
      "answer": "Stratovolcano",
      "segment": "geography"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. What is the main reason for the formation of ocean currents?",
      "options": [
        "Wind patterns",
        "Earth's rotation",
        "Temperature and salinity differences",
        "All of the above"
      ],
      "answer": "All of the above",
      "segment": "geography"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. Which type of soil is formed by the deposition of sediments by rivers?",
      "options": ["Alluvial soil", "Black soil", "Laterite soil", "Red soil"],
      "answer": "Alluvial soil",
      "segment": "geography"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. What is the term for the point on the Earth's surface directly above an earthquake's focus?",
      "options": ["Hypocenter", "Epicenter", "Fault", "Seismic Zone"],
      "answer": "Epicenter",
      "segment": "geography"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. What does the 'Greenwich Meridian' refer to?",
      "options": [
        "The 0° longitude line",
        "The 0° latitude line",
        "The International Date Line",
        "The Equatorial line"
      ],
      "answer": "The 0° longitude line",
      "segment": "geography"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. What is the name of the process by which water changes directly from solid to gas?",
      "options": ["Condensation", "Sublimation", "Evaporation", "Deposition"],
      "answer": "Sublimation",
      "segment": "geography"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. Which of the following is not a greenhouse gas?",
      "options": ["Carbon dioxide", "Methane", "Oxygen", "Water vapor"],
      "answer": "Oxygen",
      "segment": "geography"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the term used for a government run by elected representatives?",
      "options": ["Monarchy", "Dictatorship", "Democracy", "Oligarchy"],
      "answer": "Democracy",
      "segment": "political_science"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. Which body is responsible for making laws in India?",
      "options": ["Executive", "Judiciary", "Legislature", "President"],
      "answer": "Legislature",
      "segment": "political_science"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. What is the minimum age for voting in India?",
      "options": ["16 years", "18 years", "21 years", "25 years"],
      "answer": "18 years",
      "segment": "political_science"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. Which article of the Indian Constitution guarantees the right to equality?",
      "options": ["Article 14", "Article 19", "Article 21", "Article 32"],
      "answer": "Article 14",
      "segment": "political_science"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. Who is the constitutional head of the Indian state?",
      "options": ["Prime Minister", "President", "Chief Minister", "Governor"],
      "answer": "President",
      "segment": "political_science"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the term for a system where power is divided between a central authority and various constituent units?",
      "options": ["Unitary system", "Federal system", "Confederal system", "Dictatorial system"],
      "answer": "Federal system",
      "segment": "political_science"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. Which house of the Indian Parliament is known as the 'House of the People'?",
      "options": ["Rajya Sabha", "Lok Sabha", "Vidhan Sabha", "Vidhan Parishad"],
      "answer": "Lok Sabha",
      "segment": "political_science"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. What does the term 'sovereignty' mean?",
      "options": [
        "Supreme power or authority",
        "A system of alliances",
        "Economic independence",
        "Military dominance"
      ],
      "answer": "Supreme power or authority",
      "segment": "political_science"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. Which political ideology emphasizes equality and the elimination of class distinctions?",
      "options": ["Capitalism", "Socialism", "Liberalism", "Conservatism"],
      "answer": "Socialism",
      "segment": "political_science"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. Who was the chairman of the drafting committee of the Indian Constitution?",
      "options": ["Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Patel", "Rajendra Prasad"],
      "answer": "B.R. Ambedkar",
      "segment": "political_science"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. What is the maximum strength of the Lok Sabha as per the Indian Constitution?",
      "options": ["500", "545", "552", "560"],
      "answer": "552",
      "segment": "political_science"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What does the term 'bicameral legislature' mean?",
      "options": [
        "A legislature with two houses",
        "A legislature with one house",
        "A legislature with three houses",
        "A legislature with no houses"
      ],
      "answer": "A legislature with two houses",
      "segment": "political_science"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. Which schedule of the Indian Constitution deals with the allocation of powers between the Union and the States?",
      "options": ["First Schedule", "Seventh Schedule", "Eighth Schedule", "Tenth Schedule"],
      "answer": "Seventh Schedule",
      "segment": "political_science"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. What is the tenure of a judge of the Supreme Court of India?",
      "options": [
        "5 years",
        "10 years",
        "Until the age of 65",
        "Until the age of 70"
      ],
      "answer": "Until the age of 65",
      "segment": "political_science"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. Which part of the Indian Constitution deals with the Fundamental Duties of citizens?",
      "options": ["Part III", "Part IV", "Part IVA", "Part V"],
      "answer": "Part IVA",
      "segment": "political_science"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. Who is considered the father of modern psychology?",
      "options": ["Sigmund Freud", "Wilhelm Wundt", "B.F. Skinner", "Carl Rogers"],
      "answer": "Wilhelm Wundt",
      "segment": "psychology"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. What does the term 'cognition' refer to?",
      "options": ["Physical movement", "Mental processes", "Emotions", "Dreams"],
      "answer": "Mental processes",
      "segment": "psychology"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. Which part of the brain is responsible for balance and coordination?",
      "options": ["Cerebrum", "Cerebellum", "Medulla", "Hypothalamus"],
      "answer": "Cerebellum",
      "segment": "psychology"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. What is the term for a test designed to measure intelligence?",
      "options": ["IQ test", "Personality test", "Aptitude test", "Emotional test"],
      "answer": "IQ test",
      "segment": "psychology"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. What does the term 'motivation' refer to in psychology?",
      "options": [
        "Behavior that is learned",
        "The reason behind actions and goals",
        "The state of being awake",
        "Emotional imbalance"
      ],
      "answer": "The reason behind actions and goals",
      "segment": "psychology"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. Which psychological perspective emphasizes the role of the unconscious mind?",
      "options": ["Behavioral", "Cognitive", "Psychoanalytic", "Humanistic"],
      "answer": "Psychoanalytic",
      "segment": "psychology"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. What is the main focus of developmental psychology?",
      "options": [
        "Behavior in social settings",
        "The growth and changes over a lifespan",
        "Cognitive disorders",
        "Human motivation"
      ],
      "answer": "The growth and changes over a lifespan",
      "segment": "psychology"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. What is a conditioned stimulus in classical conditioning?",
      "options": [
        "A stimulus that triggers a natural response",
        "A stimulus that triggers a learned response",
        "A response to a natural stimulus",
        "A response to an unconditioned stimulus"
      ],
      "answer": "A stimulus that triggers a learned response",
      "segment": "psychology"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. What does the term 'schema' refer to in cognitive psychology?",
      "options": [
        "A mental framework or structure",
        "A method of data collection",
        "A type of brain injury",
        "A behavioral reward system"
      ],
      "answer": "A mental framework or structure",
      "segment": "psychology"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. Who developed the hierarchy of needs theory?",
      "options": ["Carl Jung", "Sigmund Freud", "Abraham Maslow", "B.F. Skinner"],
      "answer": "Abraham Maslow",
      "segment": "psychology"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. What is the primary focus of psychophysics?",
      "options": [
        "The study of brain anatomy",
        "The relationship between stimuli and perception",
        "The treatment of mental disorders",
        "The study of genetic behavior"
      ],
      "answer": "The relationship between stimuli and perception",
      "segment": "psychology"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. What does the term 'neuroplasticity' refer to?",
      "options": [
        "The brain's ability to change and adapt",
        "A type of neurotransmitter",
        "A disorder affecting neurons",
        "The rigidity of neural connections"
      ],
      "answer": "The brain's ability to change and adapt",
      "segment": "psychology"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What is the key idea behind the concept of 'cognitive dissonance'?",
      "options": [
        "Conflict between attitudes and behaviors",
        "Learning through observation",
        "Emotional detachment",
        "Memory retrieval issues"
      ],
      "answer": "Conflict between attitudes and behaviors",
      "segment": "psychology"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. Which neurotransmitter is primarily associated with mood regulation?",
      "options": ["Dopamine", "Serotonin", "GABA", "Acetylcholine"],
      "answer": "Serotonin",
      "segment": "psychology"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. What is the main focus of humanistic psychology?",
      "options": [
        "Unconscious drives",
        "Observable behavior",
        "Self-actualization and personal growth",
        "Genetic predispositions"
      ],
      "answer": "Self-actualization and personal growth",
      "segment": "psychology"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. What is the primary focus of sociology?",
      "options": [
        "Study of biological processes",
        "Study of human society and social behavior",
        "Study of physical geography",
        "Study of individual psychology"
      ],
      "answer": "Study of human society and social behavior",
      "segment": "sociology"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. Who is known as the father of sociology?",
      "options": ["Karl Marx", "Max Weber", "Auguste Comte", "Emile Durkheim"],
      "answer": "Auguste Comte",
      "segment": "sociology"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. What does the term 'culture' refer to in sociology?",
      "options": [
        "Inherited traits",
        "Shared beliefs, norms, and values of a society",
        "Economic systems",
        "Technological advancements"
      ],
      "answer": "Shared beliefs, norms, and values of a society",
      "segment": "sociology"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. What is 'socialization'?",
      "options": [
        "A political process",
        "The process of learning and adopting societal norms",
        "Economic planning",
        "The study of ancient societies"
      ],
      "answer": "The process of learning and adopting societal norms",
      "segment": "sociology"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. Which term refers to the study of population dynamics in sociology?",
      "options": ["Demography", "Anthropology", "Economics", "Ecology"],
      "answer": "Demography",
      "segment": "sociology"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is 'ethnocentrism' in sociology?",
      "options": [
        "Studying only one's own culture",
        "Judging another culture by one's own cultural standards",
        "Promoting cultural diversity",
        "Ignoring cultural differences"
      ],
      "answer": "Judging another culture by one's own cultural standards",
      "segment": "sociology"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Who developed the concept of 'ideal types' in sociology?",
      "options": ["Auguste Comte", "Max Weber", "Karl Marx", "Emile Durkheim"],
      "answer": "Max Weber",
      "segment": "sociology"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What does the term 'anomie' mean in sociology?",
      "options": [
        "A strong sense of community",
        "A state of normlessness or lack of social regulation",
        "Excessive adherence to norms",
        "A cultural movement"
      ],
      "answer": "A state of normlessness or lack of social regulation",
      "segment": "sociology"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. Which sociological perspective emphasizes the role of power and inequality in society?",
      "options": [
        "Functionalist perspective",
        "Conflict perspective",
        "Interactionist perspective",
        "Evolutionary perspective"
      ],
      "answer": "Conflict perspective",
      "segment": "sociology"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. What is the term for a group of people sharing similar social, economic, and cultural status?",
      "options": ["Community", "Caste", "Social class", "Ethnic group"],
      "answer": "Social class",
      "segment": "sociology"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. What does 'symbolic interactionism' focus on?",
      "options": [
        "The structure of society",
        "The use of symbols and interactions in social processes",
        "Economic changes in society",
        "Cultural evolution"
      ],
      "answer": "The use of symbols and interactions in social processes",
      "segment": "sociology"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. Who authored the book *The Division of Labour in Society*?",
      "options": ["Karl Marx", "Max Weber", "Emile Durkheim", "Auguste Comte"],
      "answer": "Emile Durkheim",
      "segment": "sociology"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. What is the term for a change in social status relative to others in society?",
      "options": ["Social mobility", "Cultural change", "Social stratification", "Anomie"],
      "answer": "Social mobility",
      "segment": "sociology"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. Which concept refers to a set of expected behaviors for individuals in a social position?",
      "options": ["Role", "Norm", "Status", "Value"],
      "answer": "Role",
      "segment": "sociology"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. What is the term for a system in which social positions are inherited and fixed?",
      "options": ["Class system", "Caste system", "Meritocracy", "Oligarchy"],
      "answer": "Caste system",
      "segment": "sociology"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
