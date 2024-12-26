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
quiz_data = {"id": "3_11_comm_m",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. Which of the following is a real account?",
      "options": ["Cash Account", "Capital Account", "Sales Account", "Commission Account"],
      "answer": "Cash Account",
      "segment": "Accountancy"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. What is the primary objective of bookkeeping?",
      "options": ["To prepare financial statements", "To record all transactions", "To make a profit", "To avoid tax"],
      "answer": "To record all transactions",
      "segment": "Accountancy"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What is the accounting equation?",
      "options": [
        "Assets = Liabilities - Capital",
        "Assets + Liabilities = Capital",
        "Assets = Liabilities + Capital",
        "Assets = Capital - Liabilities"
      ],
      "answer": "Assets = Liabilities + Capital",
      "segment": "Accountancy"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. Which of the following is an example of a liability?",
      "options": ["Debtors", "Creditors", "Cash", "Stock"],
      "answer": "Creditors",
      "segment": "Accountancy"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. What type of account is 'Sales'?",
      "options": ["Personal Account", "Real Account", "Nominal Account", "Capital Account"],
      "answer": "Nominal Account",
      "segment": "Accountancy"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. Which principle requires that revenue should be recognized when earned, regardless of when it is received?",
      "options": ["Accrual Principle", "Consistency Principle", "Matching Principle", "Materiality Principle"],
      "answer": "Accrual Principle",
      "segment": "Accountancy"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. What does a Trial Balance show?",
      "options": [
        "Assets and liabilities of a business",
        "Balances of all ledger accounts",
        "Revenue and expenses of a business",
        "Profit or loss of a business"
      ],
      "answer": "Balances of all ledger accounts",
      "segment": "Accountancy"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. Which of the following is not a type of error in accounting?",
      "options": ["Error of Commission", "Error of Omission", "Error of Duplication", "Error of Principle"],
      "answer": "Error of Duplication",
      "segment": "Accountancy"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. What is recorded on the credit side of a ledger?",
      "options": ["Expenses", "Revenues", "Assets", "Drawings"],
      "answer": "Revenues",
      "segment": "Accountancy"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. In double-entry bookkeeping, every debit has:",
      "options": ["No effect on credit", "A corresponding credit", "Two credits", "A balance"],
      "answer": "A corresponding credit",
      "segment": "Accountancy"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. Which financial statement shows the financial position of a company at a specific point in time?",
      "options": ["Income Statement", "Cash Flow Statement", "Balance Sheet", "Trial Balance"],
      "answer": "Balance Sheet",
      "segment": "Accountancy"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. What is depreciation?",
      "options": [
        "Increase in the value of an asset",
        "Decrease in the value of an asset",
        "Expenditure on repairs",
        "Writing off bad debts"
      ],
      "answer": "Decrease in the value of an asset",
      "segment": "Accountancy"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. Which account is debited when goods are purchased on credit?",
      "options": ["Cash Account", "Purchase Account", "Sales Account", "Creditor's Account"],
      "answer": "Purchase Account",
      "segment": "Accountancy"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. The matching principle in accounting ensures that:",
      "options": [
        "Revenue is matched with income",
        "Expenses are matched with liabilities",
        "Expenses are matched with revenues of the same period",
        "Assets are matched with liabilities"
      ],
      "answer": "Expenses are matched with revenues of the same period",
      "segment": "Accountancy"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. Which of the following errors affect the Trial Balance?",
      "options": [
        "Error of Principle",
        "Error of Commission",
        "Compensating Error",
        "Error of Omission"
      ],
      "answer": "Error of Commission",
      "segment": "Accountancy"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. Which one of the following is considered a primary industry?",
      "options": ["Banking", "Fishing", "Retail", "Software Development"],
      "answer": "Fishing",
      "segment": "business_studies"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. What does GDP stand for?",
      "options": ["Gross Domestic Product", "Global Development Plan", "General Data Protection", "Gross Data Processing"],
      "answer": "Gross Domestic Product",
      "segment": "business_studies"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. Which form of business organization is owned by shareholders?",
      "options": ["Sole Proprietorship", "Partnership", "Company", "Co-operative Society"],
      "answer": "Company",
      "segment": "business_studies"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. What is the primary objective of a business?",
      "options": ["Maximize employee benefits", "Ensure customer satisfaction", "Earn profit", "Promote environmental sustainability"],
      "answer": "Earn profit",
      "segment": "business_studies"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which type of business risk arises due to changes in government policies?",
      "options": ["Financial risk", "Operational risk", "Legal risk", "Strategic risk"],
      "answer": "Legal risk",
      "segment": "business_studies"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. What is a key feature of a partnership firm?",
      "options": ["Limited liability", "Single ownership", "Profit-sharing among partners", "Registered with stock exchange"],
      "answer": "Profit-sharing among partners",
      "segment": "business_studies"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. Which document is known as the charter of a company?",
      "options": ["Memorandum of Association", "Articles of Association", "Share Certificate", "Prospectus"],
      "answer": "Memorandum of Association",
      "segment": "business_studies"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. Which type of business financing involves selling shares to the public?",
      "options": ["Debt Financing", "Equity Financing", "Lease Financing", "Trade Credit"],
      "answer": "Equity Financing",
      "segment": "business_studies"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. What is the primary purpose of a business plan?",
      "options": ["To secure funding", "To analyze competitors", "To forecast profits", "To define business goals and strategies"],
      "answer": "To define business goals and strategies",
      "segment": "business_studies"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. Which of the following is not a feature of a sole proprietorship?",
      "options": ["Quick decision-making", "Unlimited liability", "Sharing of profits", "Less legal formalities"],
      "answer": "Sharing of profits",
      "segment": "business_studies"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. What is the maximum number of partners allowed in a banking partnership as per the Indian Partnership Act, 1932?",
      "options": ["10", "20", "15", "50"],
      "answer": "10",
      "segment": "business_studies"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which of the following is an example of a public sector enterprise?",
      "options": ["Reliance Industries", "Indian Railways", "Infosys", "Tata Motors"],
      "answer": "Indian Railways",
      "segment": "business_studies"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. What is the minimum subscription requirement as per the Companies Act, 2013?",
      "options": ["75% of issued capital", "50% of issued capital", "90% of issued capital", "95% of issued capital"],
      "answer": "90% of issued capital",
      "segment": "business_studies"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. Which type of co-operative society focuses on providing financial assistance to its members?",
      "options": ["Housing society", "Credit society", "Consumer society", "Marketing society"],
      "answer": "Credit society",
      "segment": "business_studies"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. Which of the following business structures is governed by the Limited Liability Partnership Act, 2008?",
      "options": ["Private Company", "Sole Proprietorship", "Limited Liability Partnership", "Public Company"],
      "answer": "Limited Liability Partnership",
      "segment": "business_studies"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the primary focus of microeconomics?",
      "options": ["National income", "Individual markets", "Economic growth", "Inflation"],
      "answer": "Individual markets",
      "segment": "economics"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. What is the formula for calculating total revenue?",
      "options": ["Price × Quantity", "Price ÷ Quantity", "Price + Quantity", "Price − Quantity"],
      "answer": "Price × Quantity",
      "segment": "economics"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. Which of the following is a characteristic of a centrally planned economy?",
      "options": ["Decentralized decision-making", "Private ownership", "Government controls production", "Market-driven pricing"],
      "answer": "Government controls production",
      "segment": "economics"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. What is the basic economic problem?",
      "options": ["Scarcity", "Unemployment", "Inflation", "Deflation"],
      "answer": "Scarcity",
      "segment": "economics"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. Which factor of production earns wages?",
      "options": ["Land", "Labor", "Capital", "Entrepreneurship"],
      "answer": "Labor",
      "segment": "economics"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What does the Production Possibility Frontier (PPF) represent?",
      "options": [
        "All possible levels of economic growth",
        "Combination of goods and services an economy can produce using all resources efficiently",
        "Impact of inflation on production",
        "Comparison of demand and supply"
      ],
      "answer": "Combination of goods and services an economy can produce using all resources efficiently",
      "segment": "economics"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. Which type of elasticity measures the responsiveness of demand to changes in price?",
      "options": [
        "Price elasticity of supply",
        "Income elasticity of demand",
        "Price elasticity of demand",
        "Cross elasticity of demand"
      ],
      "answer": "Price elasticity of demand",
      "segment": "economics"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. In perfect competition, firms are considered to be:",
      "options": ["Price makers", "Price takers", "Monopolists", "Price discriminators"],
      "answer": "Price takers",
      "segment": "economics"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. What is meant by 'opportunity cost'?",
      "options": [
        "The cost of hiring an additional worker",
        "The cost of choosing one alternative over another",
        "The cost of producing one additional unit",
        "The cost of maintaining resources"
      ],
      "answer": "The cost of choosing one alternative over another",
      "segment": "economics"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. What does the term 'marginal utility' mean?",
      "options": [
        "Total satisfaction from consumption",
        "Satisfaction from consuming one additional unit",
        "Satisfaction from consuming half the units",
        "Diminishing satisfaction over time"
      ],
      "answer": "Satisfaction from consuming one additional unit",
      "segment": "economics"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. Which of the following is not a function of money?",
      "options": [
        "Medium of exchange",
        "Store of value",
        "Means of production",
        "Unit of account"
      ],
      "answer": "Means of production",
      "segment": "economics"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What does the Lorenz Curve represent?",
      "options": [
        "Inflation rate",
        "Income distribution",
        "Production possibilities",
        "Elasticity of demand"
      ],
      "answer": "Income distribution",
      "segment": "economics"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. What is the difference between GDP at factor cost and GDP at market price?",
      "options": [
        "Indirect taxes minus subsidies",
        "Direct taxes minus subsidies",
        "Exports minus imports",
        "Savings minus investments"
      ],
      "answer": "Indirect taxes minus subsidies",
      "segment": "economics"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Which type of market structure is characterized by a single seller with no close substitutes for its product?",
      "options": ["Monopoly", "Perfect competition", "Oligopoly", "Monopolistic competition"],
      "answer": "Monopoly",
      "segment": "economics"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. What does 'Giffen goods' refer to in economics?",
      "options": [
        "Normal goods with high demand",
        "Inferior goods with a positive price-demand relationship",
        "Luxury goods with no substitutes",
        "Goods with constant demand regardless of price"
      ],
      "answer": "Inferior goods with a positive price-demand relationship",
      "segment": "economics"
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
      "question": "61. What is the value of sin 30°?",
      "options": ["0", "1", "1/2", "√3/2"],
      "answer": "1/2",
      "segment": "Maths"
    },
    {
      "id": 62,
      "difficulty": "Easy",
      "question": "62. The derivative of x² with respect to x is?",
      "options": ["x", "2x", "x²", "2x²"],
      "answer": "2x",
      "segment": "Maths"
    },
    {
      "id": 63,
      "difficulty": "Easy",
      "question": "63. What is the sum of the angles in a triangle?",
      "options": ["90°", "180°", "360°", "120°"],
      "answer": "180°",
      "segment": "Maths"
    },
    {
      "id": 64,
      "difficulty": "Easy",
      "question": "64. If a matrix has dimensions 3x2, how many rows does it have?",
      "options": ["2", "3", "6", "5"],
      "answer": "3",
      "segment": "Maths"
    },
    {
      "id": 65,
      "difficulty": "Easy",
      "question": "65. What is the value of (a+b)²?",
      "options": ["a² + b²", "a² + 2ab + b²", "a² - 2ab + b²", "None of these"],
      "answer": "a² + 2ab + b²",
      "segment": "Maths"
    },
    {
      "id": 66,
      "difficulty": "Medium",
      "question": "66. What is the solution to the equation 2x - 5 = 3?",
      "options": ["x = 1", "x = 4", "x = -1", "x = 5"],
      "answer": "x = 4",
      "segment": "Maths"
    },
    {
      "id": 67,
      "difficulty": "Medium",
      "question": "67. What is the slope of the line passing through points (2, 3) and (4, 7)?",
      "options": ["2", "4", "1", "5"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 68,
      "difficulty": "Medium",
      "question": "68. What is the sum of the first 10 natural numbers?",
      "options": ["55", "50", "45", "60"],
      "answer": "55",
      "segment": "Maths"
    },
    {
      "id": 69,
      "difficulty": "Medium",
      "question": "69. If logₐ(x) = 3 and logₐ(y) = 4, what is logₐ(xy)?",
      "options": ["7", "12", "1", "0"],
      "answer": "7",
      "segment": "Maths"
    },
    {
      "id": 70,
      "difficulty": "Medium",
      "question": "70. What is the radius of a circle with area 25π?",
      "options": ["5", "25", "10", "50"],
      "answer": "5",
      "segment": "Maths"
    },
    {
      "id": 71,
      "difficulty": "Hard",
      "question": "71. Solve the inequality: 3x - 7 > 2x + 5.",
      "options": ["x > 12", "x < 12", "x = 12", "x > -12"],
      "answer": "x > 12",
      "segment": "Maths"
    },
    {
      "id": 72,
      "difficulty": "Hard",
      "question": "72. What is the determinant of the matrix [[1, 2], [3, 4]]?",
      "options": ["-2", "2", "0", "10"],
      "answer": "-2",
      "segment": "Maths"
    },
    {
      "id": 73,
      "difficulty": "Hard",
      "question": "73. If f(x) = 3x² + 2x + 1, what is f'(x)?",
      "options": ["6x + 2", "6x + 1", "3x + 2", "3x² + 2"],
      "answer": "6x + 2",
      "segment": "Maths"
    },
    {
      "id": 74,
      "difficulty": "Hard",
      "question": "74. Evaluate the integral ∫x dx.",
      "options": ["x²", "x²/2", "x + C", "x² + C"],
      "answer": "x²/2",
      "segment": "Maths"
    },
    {
      "id": 75,
      "difficulty": "Hard",
      "question": "75. Find the sum of the series: 2 + 4 + 6 + ... + 20.",
      "options": ["110", "120", "100", "90"],
      "answer": "110",
      "segment": "Maths"
    }
  ]
}



###############################################################
# Running the validation function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(validate_mongodb_connection())
    async_database.quizzes.insert_one(quiz_data)
