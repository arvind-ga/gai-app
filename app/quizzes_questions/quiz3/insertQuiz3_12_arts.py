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
quiz_data = {"id": "3_12_arts",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. Who was the first President of India?",
      "options": [
        "Mahatma Gandhi",
        "Jawaharlal Nehru",
        "Dr. Rajendra Prasad",
        "Sardar Vallabhbhai Patel"
      ],
      "answer": "Dr. Rajendra Prasad",
      "segment": "History"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. Which empire built the Taj Mahal?",
      "options": [
        "Gupta Empire",
        "Mughal Empire",
        "Maurya Empire",
        "Chola Empire"
      ],
      "answer": "Mughal Empire",
      "segment": "History"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What was the name of the movement led by Mahatma Gandhi in 1942?",
      "options": [
        "Non-Cooperation Movement",
        "Civil Disobedience Movement",
        "Quit India Movement",
        "Swadeshi Movement"
      ],
      "answer": "Quit India Movement",
      "segment": "History"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. Who was the founder of the Maurya Dynasty?",
      "options": [
        "Chandragupta Maurya",
        "Ashoka",
        "Bindusara",
        "Samudragupta"
      ],
      "answer": "Chandragupta Maurya",
      "segment": "History"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. Where did the Industrial Revolution begin?",
      "options": [
        "France",
        "Germany",
        "United Kingdom",
        "United States"
      ],
      "answer": "United Kingdom",
      "segment": "History"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. Who was the author of 'Arthashastra'?",
      "options": [
        "Chanakya",
        "Kalidasa",
        "Banabhatta",
        "Varahamihira"
      ],
      "answer": "Chanakya",
      "segment": "History"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. Which battle marked the beginning of Mughal rule in India?",
      "options": [
        "Battle of Panipat (1526)",
        "Battle of Buxar",
        "Battle of Plassey",
        "Battle of Haldighati"
      ],
      "answer": "Battle of Panipat (1526)",
      "segment": "History"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. What was the capital of the Vijayanagara Empire?",
      "options": [
        "Hampi",
        "Madurai",
        "Kanchipuram",
        "Pataliputra"
      ],
      "answer": "Hampi",
      "segment": "History"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. Who introduced the 'Doctrine of Lapse' in India?",
      "options": [
        "Lord Dalhousie",
        "Lord Curzon",
        "Lord Wellesley",
        "Lord Hastings"
      ],
      "answer": "Lord Dalhousie",
      "segment": "History"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. Which treaty ended the First World War?",
      "options": [
        "Treaty of Versailles",
        "Treaty of Paris",
        "Treaty of Vienna",
        "Treaty of Ghent"
      ],
      "answer": "Treaty of Versailles",
      "segment": "History"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. Who was the founder of the Brahmo Samaj?",
      "options": [
        "Raja Rammohan Roy",
        "Swami Vivekananda",
        "Ishwar Chandra Vidyasagar",
        "Dayananda Saraswati"
      ],
      "answer": "Raja Rammohan Roy",
      "segment": "History"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. Which ancient text is considered the first historical record of India?",
      "options": [
        "Vedas",
        "Ramayana",
        "Rigveda",
        "Indica by Megasthenes"
      ],
      "answer": "Indica by Megasthenes",
      "segment": "History"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. Who was the last ruler of the Delhi Sultanate?",
      "options": [
        "Ibrahim Lodi",
        "Sher Shah Suri",
        "Babur",
        "Humayun"
      ],
      "answer": "Ibrahim Lodi",
      "segment": "History"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. Which council resulted in the division of Buddhism into two sects?",
      "options": [
        "First Buddhist Council",
        "Second Buddhist Council",
        "Third Buddhist Council",
        "Fourth Buddhist Council"
      ],
      "answer": "Second Buddhist Council",
      "segment": "History"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. Who signed the Treaty of Alinagar?",
      "options": [
        "Robert Clive",
        "Siraj-ud-Daulah",
        "Mir Jafar",
        "Shah Alam II"
      ],
      "answer": "Robert Clive",
      "segment": "History"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. Which is the largest continent by area?",
      "options": ["Africa", "Asia", "Europe", "Antarctica"],
      "answer": "Asia",
      "segment": "Geography"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. What is the capital of India?",
      "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
      "answer": "New Delhi",
      "segment": "Geography"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. Which river is known as the 'Sorrow of Bihar'?",
      "options": ["Ganga", "Kosi", "Brahmaputra", "Son"],
      "answer": "Kosi",
      "segment": "Geography"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. Which planet is known as the 'Blue Planet'?",
      "options": ["Mars", "Earth", "Venus", "Jupiter"],
      "answer": "Earth",
      "segment": "Geography"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which is the highest mountain peak in the world?",
      "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
      "answer": "Mount Everest",
      "segment": "Geography"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. Which is the longest river in the world?",
      "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
      "answer": "Nile",
      "segment": "Geography"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. What is the primary cause of desertification?",
      "options": ["Deforestation", "Urbanization", "Overgrazing", "All of the above"],
      "answer": "All of the above",
      "segment": "Geography"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. What is the significance of the Tropic of Cancer?",
      "options": [
        "It marks the southernmost point of the Sun's vertical rays",
        "It marks the northernmost point of the Sun's vertical rays",
        "It divides the Earth into two hemispheres",
        "It is a reference for ocean currents"
      ],
      "answer": "It marks the northernmost point of the Sun's vertical rays",
      "segment": "Geography"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. Which type of rock is formed by the cooling of magma?",
      "options": ["Sedimentary", "Igneous", "Metamorphic", "Fossil"],
      "answer": "Igneous",
      "segment": "Geography"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. What is the name of the boundary line between India and Pakistan?",
      "options": ["McMahon Line", "Radcliffe Line", "Durand Line", "Hindenburg Line"],
      "answer": "Radcliffe Line",
      "segment": "Geography"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. Which type of soil is best suited for cotton cultivation?",
      "options": ["Alluvial", "Black", "Red", "Laterite"],
      "answer": "Black",
      "segment": "Geography"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which ocean current is responsible for the mild climate of Western Europe?",
      "options": ["Canary Current", "Gulf Stream", "Humboldt Current", "Kuroshio Current"],
      "answer": "Gulf Stream",
      "segment": "Geography"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. What is the main factor causing the monsoon in India?",
      "options": [
        "Temperature difference",
        "Pressure difference",
        "Wind direction",
        "All of the above"
      ],
      "answer": "All of the above",
      "segment": "Geography"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. Which is the largest continent by area?",
      "options": ["Africa", "Asia", "Europe", "Antarctica"],
      "answer": "Asia",
      "segment": "Geography"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. What is the capital of India?",
      "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
      "answer": "New Delhi",
      "segment": "Geography"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. Which river is known as the 'Sorrow of Bihar'?",
      "options": ["Ganga", "Kosi", "Brahmaputra", "Son"],
      "answer": "Kosi",
      "segment": "Geography"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. Which planet is known as the 'Blue Planet'?",
      "options": ["Mars", "Earth", "Venus", "Jupiter"],
      "answer": "Earth",
      "segment": "Geography"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which is the highest mountain peak in the world?",
      "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
      "answer": "Mount Everest",
      "segment": "Geography"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. Which is the longest river in the world?",
      "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
      "answer": "Nile",
      "segment": "Geography"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. What is the primary cause of desertification?",
      "options": ["Deforestation", "Urbanization", "Overgrazing", "All of the above"],
      "answer": "All of the above",
      "segment": "Geography"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. What is the significance of the Tropic of Cancer?",
      "options": [
        "It marks the southernmost point of the Sun's vertical rays",
        "It marks the northernmost point of the Sun's vertical rays",
        "It divides the Earth into two hemispheres",
        "It is a reference for ocean currents"
      ],
      "answer": "It marks the northernmost point of the Sun's vertical rays",
      "segment": "Geography"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. Which type of rock is formed by the cooling of magma?",
      "options": ["Sedimentary", "Igneous", "Metamorphic", "Fossil"],
      "answer": "Igneous",
      "segment": "Geography"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. What is the name of the boundary line between India and Pakistan?",
      "options": ["McMahon Line", "Radcliffe Line", "Durand Line", "Hindenburg Line"],
      "answer": "Radcliffe Line",
      "segment": "Geography"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. Which type of soil is best suited for cotton cultivation?",
      "options": ["Alluvial", "Black", "Red", "Laterite"],
      "answer": "Black",
      "segment": "Geography"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which ocean current is responsible for the mild climate of Western Europe?",
      "options": ["Canary Current", "Gulf Stream", "Humboldt Current", "Kuroshio Current"],
      "answer": "Gulf Stream",
      "segment": "Geography"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. What is the main factor causing the monsoon in India?",
      "options": [
        "Temperature differences between land and sea",
        "Ocean currents",
        "Mountain ranges",
        "Tropical cyclones"
      ],
      "answer": "Temperature differences between land and sea",
      "segment": "Geography"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. What is the term for the process of water movement through plants and evaporation from soil?",
      "options": ["Infiltration", "Transpiration", "Evapotranspiration", "Percolation"],
      "answer": "Evapotranspiration",
      "segment": "Geography"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. Which country has the largest forest cover in the world?",
      "options": ["Brazil", "Russia", "Canada", "United States"],
      "answer": "Russia",
      "segment": "Geography"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the primary function of the legislature?",
      "options": ["To make laws", "To enforce laws", "To interpret laws", "To defend laws"],
      "answer": "To make laws",
      "segment": "Political Science"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. Who is considered the Father of the Indian Constitution?",
      "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "B.R. Ambedkar", "Sardar Patel"],
      "answer": "B.R. Ambedkar",
      "segment": "Political Science"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. What does the term 'sovereignty' mean?",
      "options": [
        "Freedom from external control",
        "Rule by divine right",
        "Economic independence",
        "Cultural unity"
      ],
      "answer": "Freedom from external control",
      "segment": "Political Science"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. Which part of the Indian Constitution deals with Fundamental Rights?",
      "options": ["Part III", "Part IV", "Part V", "Part VI"],
      "answer": "Part III",
      "segment": "Political Science"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. What is the tenure of the President of India?",
      "options": ["4 years", "5 years", "6 years", "7 years"],
      "answer": "5 years",
      "segment": "Political Science"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the primary objective of the Non-Aligned Movement (NAM)?",
      "options": [
        "To maintain neutrality during the Cold War",
        "To form a military alliance",
        "To promote colonialism",
        "To establish a new currency system"
      ],
      "answer": "To maintain neutrality during the Cold War",
      "segment": "Political Science"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. Which schedule of the Indian Constitution contains details about languages?",
      "options": ["Schedule VII", "Schedule VIII", "Schedule IX", "Schedule X"],
      "answer": "Schedule VIII",
      "segment": "Political Science"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. What does the term 'Secularism' imply in the Indian Constitution?",
      "options": [
        "Absence of religion",
        "Preference to one religion",
        "Equal treatment of all religions",
        "Religious intolerance"
      ],
      "answer": "Equal treatment of all religions",
      "segment": "Political Science"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. Who has the authority to declare a national emergency in India?",
      "options": ["Prime Minister", "Parliament", "President", "Supreme Court"],
      "answer": "President",
      "segment": "Political Science"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. Which article of the Indian Constitution deals with the Right to Equality?",
      "options": ["Article 12", "Article 14", "Article 16", "Article 18"],
      "answer": "Article 14",
      "segment": "Political Science"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. What was the main purpose of the 'Panchsheel Agreement'?",
      "options": [
        "To establish trade relations",
        "To promote religious harmony",
        "To define peaceful coexistence principles",
        "To resolve border disputes"
      ],
      "answer": "To define peaceful coexistence principles",
      "segment": "Political Science"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. Which country first adopted universal adult suffrage?",
      "options": ["USA", "France", "New Zealand", "India"],
      "answer": "New Zealand",
      "segment": "Political Science"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. What is 'Judicial Review'?",
      "options": [
        "Power to amend the Constitution",
        "Power to appoint judges",
        "Power to declare laws unconstitutional",
        "Power to review economic policies"
      ],
      "answer": "Power to declare laws unconstitutional",
      "segment": "Political Science"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Which institution is known as the 'Guardian of the Constitution' in India?",
      "options": ["President", "Parliament", "Supreme Court", "Prime Minister"],
      "answer": "Supreme Court",
      "segment": "Political Science"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. What is the primary role of the Election Commission of India?",
      "options": [
        "To amend election laws",
        "To conduct free and fair elections",
        "To manage party finances",
        "To appoint members of Parliament"
      ],
      "answer": "To conduct free and fair elections",
      "segment": "Political Science"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. Who is considered the father of modern psychology?",
      "options": ["Sigmund Freud", "Wilhelm Wundt", "Carl Jung", "B.F. Skinner"],
      "answer": "Wilhelm Wundt",
      "segment": "Psychology"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. Which branch of psychology focuses on the study of mental processes such as perception, memory, and problem-solving?",
      "options": ["Behavioral Psychology", "Cognitive Psychology", "Humanistic Psychology", "Developmental Psychology"],
      "answer": "Cognitive Psychology",
      "segment": "Psychology"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. What does IQ stand for?",
      "options": ["Intelligence Quotient", "Intellectual Quality", "Ideal Quotient", "Intellectual Quotient"],
      "answer": "Intelligence Quotient",
      "segment": "Psychology"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. What is the main focus of developmental psychology?",
      "options": ["Changes across the lifespan", "Abnormal behaviors", "Brain functions", "Group dynamics"],
      "answer": "Changes across the lifespan",
      "segment": "Psychology"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. Which psychological approach emphasizes the role of the unconscious mind?",
      "options": ["Behavioral", "Humanistic", "Psychoanalytic", "Cognitive"],
      "answer": "Psychoanalytic",
      "segment": "Psychology"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. What is self-actualization according to Maslow?",
      "options": [
        "Achieving financial success",
        "Meeting one's basic needs",
        "Reaching one's full potential",
        "Maintaining social relationships"
      ],
      "answer": "Reaching one's full potential",
      "segment": "Psychology"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. In classical conditioning, what is the term for a stimulus that elicits a response naturally?",
      "options": ["Unconditioned Stimulus", "Neutral Stimulus", "Conditioned Stimulus", "Primary Stimulus"],
      "answer": "Unconditioned Stimulus",
      "segment": "Psychology"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. Who developed the theory of operant conditioning?",
      "options": ["Ivan Pavlov", "Sigmund Freud", "B.F. Skinner", "Albert Bandura"],
      "answer": "B.F. Skinner",
      "segment": "Psychology"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. What does the term 'schema' refer to in cognitive psychology?",
      "options": [
        "A mental framework for organizing information",
        "A psychological disorder",
        "A type of memory loss",
        "A behavioral response pattern"
      ],
      "answer": "A mental framework for organizing information",
      "segment": "Psychology"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. Which neurotransmitter is primarily associated with mood regulation?",
      "options": ["Dopamine", "Serotonin", "Acetylcholine", "Glutamate"],
      "answer": "Serotonin",
      "segment": "Psychology"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. What is the main concept behind Carl Rogers' client-centered therapy?",
      "options": [
        "Behavior modification",
        "Unconditional positive regard",
        "Cognitive restructuring",
        "Psychoanalysis"
      ],
      "answer": "Unconditional positive regard",
      "segment": "Psychology"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. What is the term for the phenomenon where individuals perform better on tasks when in the presence of others?",
      "options": ["Social Loafing", "Groupthink", "Social Facilitation", "Diffusion of Responsibility"],
      "answer": "Social Facilitation",
      "segment": "Psychology"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. What does the 'Big Five' model of personality traits include?",
      "options": [
        "Introversion, Extroversion, Agreeableness, Neuroticism, Conscientiousness",
        "Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism",
        "Aggressiveness, Passivity, Extraversion, Introversion, Neuroticism",
        "Creativity, Leadership, Empathy, Introversion, Extroversion"
      ],
      "answer": "Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism",
      "segment": "Psychology"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. What is the concept of 'Cognitive Dissonance' introduced by Leon Festinger?",
      "options": [
        "Conflict between attitudes and behaviors",
        "Memory loss over time",
        "Group pressure leading to conformity",
        "Reduced performance due to anxiety"
      ],
      "answer": "Conflict between attitudes and behaviors",
      "segment": "Psychology"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. Which part of the brain is primarily responsible for forming new memories?",
      "options": ["Hippocampus", "Amygdala", "Cerebellum", "Thalamus"],
      "answer": "Hippocampus",
      "segment": "Psychology"
    },
    {
      "id": 61,
      "difficulty": "Easy",
      "question": "61. Who is known as the father of sociology?",
      "options": ["Karl Marx", "Emile Durkheim", "Auguste Comte", "Max Weber"],
      "answer": "Auguste Comte",
      "segment": "Sociology"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. What does 'socialization' mean?",
      "options": [
        "The process of learning to interact in society",
        "The study of economic growth",
        "A method of conducting surveys",
        "The act of protesting"
      ],
      "answer": "The process of learning to interact in society",
      "segment": "Sociology"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. Which of these is an example of a primary group?",
      "options": ["A family", "A political party", "A workplace", "A football team"],
      "answer": "A family",
      "segment": "Sociology"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. What is a caste system?",
      "options": [
        "A system of economic hierarchy",
        "A form of religious worship",
        "A rigid social stratification system",
        "A political ideology"
      ],
      "answer": "A rigid social stratification system",
      "segment": "Sociology"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. What does 'urbanization' refer to?",
      "options": [
        "Movement from rural to urban areas",
        "Development of agricultural practices",
        "Decline of industrial cities",
        "Study of ancient societies"
      ],
      "answer": "Movement from rural to urban areas",
      "segment": "Sociology"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is 'anomie' according to Durkheim?",
      "options": [
        "A breakdown of social norms",
        "A type of social institution",
        "A theory of economic growth",
        "A form of cultural integration"
      ],
      "answer": "A breakdown of social norms",
      "segment": "Sociology"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. Which term refers to the cultural aspects that unify a society?",
      "options": [
        "Ethnocentrism",
        "Cultural integration",
        "Cultural diffusion",
        "Social stratification"
      ],
      "answer": "Cultural integration",
      "segment": "Sociology"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What is 'ethnocentrism'?",
      "options": [
        "Belief in the superiority of one's culture",
        "Study of different ethnic groups",
        "A type of social mobility",
        "Practice of cultural relativism"
      ],
      "answer": "Belief in the superiority of one's culture",
      "segment": "Sociology"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. Which sociologist is associated with the theory of class conflict?",
      "options": ["Max Weber", "Karl Marx", "Emile Durkheim", "Auguste Comte"],
      "answer": "Karl Marx",
      "segment": "Sociology"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. What is a 'role conflict'?",
      "options": [
        "Conflict between different cultural groups",
        "Tension between different roles held by an individual",
        "Disagreement within a social institution",
        "A form of social inequality"
      ],
      "answer": "Tension between different roles held by an individual",
      "segment": "Sociology"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. What is 'cultural lag'?",
      "options": [
        "The delay in cultural adjustment to technological change",
        "A lack of cultural diversity",
        "The integration of multiple cultures",
        "A theory of social mobility"
      ],
      "answer": "The delay in cultural adjustment to technological change",
      "segment": "Sociology"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. What is the focus of Weber's concept of 'verstehen'?",
      "options": [
        "Statistical analysis of societies",
        "Understanding social action through empathy",
        "Structural analysis of economies",
        "The historical analysis of cultural norms"
      ],
      "answer": "Understanding social action through empathy",
      "segment": "Sociology"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. What does the term 'patriarchy' describe?",
      "options": [
        "A society dominated by men",
        "A political system ruled by a king",
        "A social system based on equality",
        "An economic system promoting agriculture"
      ],
      "answer": "A society dominated by men",
      "segment": "Sociology"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. What is 'alienation' according to Marxist theory?",
      "options": [
        "A condition where workers feel disconnected from their work",
        "The separation of cultural groups",
        "A process of cultural assimilation",
        "The integration of diverse societies"
      ],
      "answer": "A condition where workers feel disconnected from their work",
      "segment": "Sociology"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. What does the term 'social mobility' refer to?",
      "options": [
        "Movement of individuals between social strata",
        "Interaction between different societies",
        "Formation of new social norms",
        "A theory of urban development"
      ],
      "answer": "Movement of individuals between social strata",
      "segment": "Sociology"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
