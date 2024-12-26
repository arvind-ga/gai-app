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
quiz_data = {"id": "3_12_comm_m",
  "questions": [
    {
      "id": 1,
      "difficulty": "Easy",
      "question": "1. What is the primary objective of accounting?",
      "options": [
        "To prepare budgets",
        "To record financial transactions",
        "To calculate taxes",
        "To audit financial statements"
      ],
      "answer": "To record financial transactions",
      "segment": "Accountancy"
    },
    {
      "id": 2,
      "difficulty": "Easy",
      "question": "2. Which account is credited when cash is deposited into a bank?",
      "options": [
        "Cash Account",
        "Bank Account",
        "Capital Account",
        "Expense Account"
      ],
      "answer": "Cash Account",
      "segment": "Accountancy"
    },
    {
      "id": 3,
      "difficulty": "Easy",
      "question": "3. What is the rule for a real account?",
      "options": [
        "Debit what comes in, credit what goes out",
        "Debit the receiver, credit the giver",
        "Debit all expenses, credit all incomes",
        "Debit and credit equally"
      ],
      "answer": "Debit what comes in, credit what goes out",
      "segment": "Accountancy"
    },
    {
      "id": 4,
      "difficulty": "Easy",
      "question": "4. Which of the following is a liability?",
      "options": ["Cash", "Debtors", "Loan", "Furniture"],
      "answer": "Loan",
      "segment": "Accountancy"
    },
    {
      "id": 5,
      "difficulty": "Easy",
      "question": "5. What is the full form of IFRS?",
      "options": [
        "Indian Financial Reporting Standards",
        "International Financial Reporting Standards",
        "International Finance Regulatory Standards",
        "Indian Finance Regulatory Standards"
      ],
      "answer": "International Financial Reporting Standards",
      "segment": "Accountancy"
    },
    {
      "id": 6,
      "difficulty": "Medium",
      "question": "6. Which financial statement shows a company's financial position at a specific point in time?",
      "options": [
        "Profit and Loss Statement",
        "Cash Flow Statement",
        "Balance Sheet",
        "Ledger"
      ],
      "answer": "Balance Sheet",
      "segment": "Accountancy"
    },
    {
      "id": 7,
      "difficulty": "Medium",
      "question": "7. What type of account is 'Goodwill'?",
      "options": [
        "Personal Account",
        "Real Account",
        "Nominal Account",
        "Expense Account"
      ],
      "answer": "Real Account",
      "segment": "Accountancy"
    },
    {
      "id": 8,
      "difficulty": "Medium",
      "question": "8. What is depreciation?",
      "options": [
        "Increase in value of an asset over time",
        "Decrease in value of an asset over time",
        "Adjustment for an error",
        "Payment of an expense"
      ],
      "answer": "Decrease in value of an asset over time",
      "segment": "Accountancy"
    },
    {
      "id": 9,
      "difficulty": "Medium",
      "question": "9. In the absence of partnership deed, how are profits shared among partners?",
      "options": [
        "According to capital contribution",
        "Equally",
        "As per mutual agreement",
        "Based on seniority"
      ],
      "answer": "Equally",
      "segment": "Accountancy"
    },
    {
      "id": 10,
      "difficulty": "Medium",
      "question": "10. Which is not included in the capital expenditure?",
      "options": [
        "Purchase of machinery",
        "Construction of a building",
        "Wages for installation of machinery",
        "Repairs of machinery"
      ],
      "answer": "Repairs of machinery",
      "segment": "Accountancy"
    },
    {
      "id": 11,
      "difficulty": "Hard",
      "question": "11. What is the treatment for 'Bad Debts Recovered' in the financial statements?",
      "options": [
        "Credited to the Profit and Loss Account",
        "Debited to the Profit and Loss Account",
        "Added to the Balance Sheet as an asset",
        "Subtracted from total revenue"
      ],
      "answer": "Credited to the Profit and Loss Account",
      "segment": "Accountancy"
    },
    {
      "id": 12,
      "difficulty": "Hard",
      "question": "12. What is the journal entry for the distribution of profit among partners?",
      "options": [
        "Profit and Loss Account Dr. To Capital Account",
        "Profit and Loss Appropriation Account Dr. To Partners’ Capital Account",
        "Capital Account Dr. To Profit and Loss Account",
        "Partners’ Current Account Dr. To Profit and Loss Account"
      ],
      "answer": "Profit and Loss Appropriation Account Dr. To Partners’ Capital Account",
      "segment": "Accountancy"
    },
    {
      "id": 13,
      "difficulty": "Hard",
      "question": "13. Which method of depreciation provides a constant charge over the useful life of the asset?",
      "options": [
        "Straight Line Method",
        "Diminishing Balance Method",
        "Sum-of-Digits Method",
        "Double Declining Balance Method"
      ],
      "answer": "Straight Line Method",
      "segment": "Accountancy"
    },
    {
      "id": 14,
      "difficulty": "Hard",
      "question": "14. What does the 'Cash Flow from Investing Activities' section include?",
      "options": [
        "Operating profits",
        "Purchase and sale of fixed assets",
        "Issue of shares",
        "Payment of dividends"
      ],
      "answer": "Purchase and sale of fixed assets",
      "segment": "Accountancy"
    },
    {
      "id": 15,
      "difficulty": "Hard",
      "question": "15. How are the goodwill adjustments recorded when a new partner is admitted?",
      "options": [
        "Debit Goodwill Account and Credit Capital Account",
        "Debit New Partner’s Capital Account and Credit Old Partners’ Capital Account",
        "Debit Old Partners’ Capital Account and Credit New Partner’s Capital Account",
        "Credit Goodwill Account and Debit Capital Account"
      ],
      "answer": "Debit New Partner’s Capital Account and Credit Old Partners’ Capital Account",
      "segment": "Accountancy"
    },
    {
      "id": 16,
      "difficulty": "Easy",
      "question": "16. What is the primary objective of management?",
      "options": [
        "To achieve organizational goals",
        "To maximize employee satisfaction",
        "To minimize expenses",
        "To ensure social welfare"
      ],
      "answer": "To achieve organizational goals",
      "segment": "Business_Studies"
    },
    {
      "id": 17,
      "difficulty": "Easy",
      "question": "17. Who is known as the 'Father of Scientific Management'?",
      "options": [
        "Henry Fayol",
        "F.W. Taylor",
        "Elton Mayo",
        "Peter Drucker"
      ],
      "answer": "F.W. Taylor",
      "segment": "Business_Studies"
    },
    {
      "id": 18,
      "difficulty": "Easy",
      "question": "18. Which of the following is a function of management?",
      "options": [
        "Marketing",
        "Organizing",
        "Selling",
        "Manufacturing"
      ],
      "answer": "Organizing",
      "segment": "Business_Studies"
    },
    {
      "id": 19,
      "difficulty": "Easy",
      "question": "19. Which principle of management emphasizes 'team spirit'?",
      "options": [
        "Division of Work",
        "Unity of Command",
        "Espirit de Corps",
        "Discipline"
      ],
      "answer": "Espirit de Corps",
      "segment": "Business_Studies"
    },
    {
      "id": 20,
      "difficulty": "Easy",
      "question": "20. Which of the following is a feature of a sole proprietorship?",
      "options": [
        "Limited liability",
        "Separate legal entity",
        "Unlimited liability",
        "Corporate structure"
      ],
      "answer": "Unlimited liability",
      "segment": "Business_Studies"
    },
    {
      "id": 21,
      "difficulty": "Medium",
      "question": "21. What does 'Planning' involve in the process of management?",
      "options": [
        "Defining objectives and deciding the future course of action",
        "Recruiting and training employees",
        "Evaluating employee performance",
        "Supervising and controlling operations"
      ],
      "answer": "Defining objectives and deciding the future course of action",
      "segment": "Business_Studies"
    },
    {
      "id": 22,
      "difficulty": "Medium",
      "question": "22. Which type of organizational structure is suitable for large-scale businesses with diverse operations?",
      "options": [
        "Functional structure",
        "Divisional structure",
        "Matrix structure",
        "Flat structure"
      ],
      "answer": "Divisional structure",
      "segment": "Business_Studies"
    },
    {
      "id": 23,
      "difficulty": "Medium",
      "question": "23. What does 'span of control' refer to in management?",
      "options": [
        "The level of authority a manager has",
        "The number of subordinates under a manager",
        "The overall goals of the organization",
        "The distribution of resources"
      ],
      "answer": "The number of subordinates under a manager",
      "segment": "Business_Studies"
    },
    {
      "id": 24,
      "difficulty": "Medium",
      "question": "24. Which type of communication flows from subordinates to superiors?",
      "options": [
        "Horizontal communication",
        "Upward communication",
        "Downward communication",
        "Diagonal communication"
      ],
      "answer": "Upward communication",
      "segment": "Business_Studies"
    },
    {
      "id": 25,
      "difficulty": "Medium",
      "question": "25. Which leadership style involves high levels of employee participation?",
      "options": [
        "Autocratic",
        "Democratic",
        "Laissez-faire",
        "Bureaucratic"
      ],
      "answer": "Democratic",
      "segment": "Business_Studies"
    },
    {
      "id": 26,
      "difficulty": "Hard",
      "question": "26. Which concept focuses on 'satisfying consumer needs while achieving business goals'?",
      "options": [
        "Production concept",
        "Sales concept",
        "Marketing concept",
        "Social concept"
      ],
      "answer": "Marketing concept",
      "segment": "Business_Studies"
    },
    {
      "id": 27,
      "difficulty": "Hard",
      "question": "27. Which financial market deals in long-term securities?",
      "options": [
        "Money Market",
        "Capital Market",
        "Forex Market",
        "Commodity Market"
      ],
      "answer": "Capital Market",
      "segment": "Business_Studies"
    },
    {
      "id": 28,
      "difficulty": "Hard",
      "question": "28. What is the primary focus of 'Taylor's Scientific Management'?",
      "options": [
        "Improving employee satisfaction",
        "Enhancing operational efficiency",
        "Encouraging innovation",
        "Reducing competition"
      ],
      "answer": "Enhancing operational efficiency",
      "segment": "Business_Studies"
    },
    {
      "id": 29,
      "difficulty": "Hard",
      "question": "29. Which principle of management advocates for 'fair wages and treatment of employees'?",
      "options": [
        "Centralization",
        "Remuneration of Personnel",
        "Equity",
        "Unity of Direction"
      ],
      "answer": "Equity",
      "segment": "Business_Studies"
    },
    {
      "id": 30,
      "difficulty": "Hard",
      "question": "30. What does the 'Debt-Equity Ratio' measure?",
      "options": [
        "Liquidity of the business",
        "Profitability of the business",
        "Proportion of debt to equity in capital structure",
        "Efficiency of asset utilization"
      ],
      "answer": "Proportion of debt to equity in capital structure",
      "segment": "Business_Studies"
    },
    {
      "id": 31,
      "difficulty": "Easy",
      "question": "31. What is the study of economics primarily concerned with?",
      "options": [
        "Production, distribution, and consumption of goods and services",
        "Human psychology",
        "Physical sciences",
        "Natural resources"
      ],
      "answer": "Production, distribution, and consumption of goods and services",
      "segment": "Economics"
    },
    {
      "id": 32,
      "difficulty": "Easy",
      "question": "32. What does GDP stand for?",
      "options": [
        "Gross Domestic Product",
        "Global Development Project",
        "General Domestic Policy",
        "Gross Development Plan"
      ],
      "answer": "Gross Domestic Product",
      "segment": "Economics"
    },
    {
      "id": 33,
      "difficulty": "Easy",
      "question": "33. Which sector of the economy is concerned with agriculture?",
      "options": [
        "Primary sector",
        "Secondary sector",
        "Tertiary sector",
        "Quaternary sector"
      ],
      "answer": "Primary sector",
      "segment": "Economics"
    },
    {
      "id": 34,
      "difficulty": "Easy",
      "question": "34. What is the meaning of 'demand' in economics?",
      "options": [
        "The desire to own something",
        "The quantity of a good that consumers are willing and able to buy at a given price",
        "The supply of goods in the market",
        "The cost of production"
      ],
      "answer": "The quantity of a good that consumers are willing and able to buy at a given price",
      "segment": "Economics"
    },
    {
      "id": 35,
      "difficulty": "Easy",
      "question": "35. Which of the following is an example of a microeconomic concept?",
      "options": [
        "National income",
        "Consumer behavior",
        "Inflation rate",
        "Gross Domestic Product"
      ],
      "answer": "Consumer behavior",
      "segment": "Economics"
    },
    {
      "id": 36,
      "difficulty": "Medium",
      "question": "36. What is the primary objective of monetary policy?",
      "options": [
        "To control inflation and stabilize the economy",
        "To reduce unemployment",
        "To promote foreign trade",
        "To enhance agriculture production"
      ],
      "answer": "To control inflation and stabilize the economy",
      "segment": "Economics"
    },
    {
      "id": 37,
      "difficulty": "Medium",
      "question": "37. What is the term for the situation where demand exceeds supply?",
      "options": [
        "Inflation",
        "Recession",
        "Shortage",
        "Surplus"
      ],
      "answer": "Shortage",
      "segment": "Economics"
    },
    {
      "id": 38,
      "difficulty": "Medium",
      "question": "38. Which of the following is an example of a public good?",
      "options": [
        "Electricity",
        "National defense",
        "Cars",
        "Clothing"
      ],
      "answer": "National defense",
      "segment": "Economics"
    },
    {
      "id": 39,
      "difficulty": "Medium",
      "question": "39. What does 'elasticity of demand' measure?",
      "options": [
        "The change in demand due to a change in income",
        "The change in supply due to a change in price",
        "The responsiveness of demand to changes in price",
        "The responsiveness of supply to changes in production"
      ],
      "answer": "The responsiveness of demand to changes in price",
      "segment": "Economics"
    },
    {
      "id": 40,
      "difficulty": "Medium",
      "question": "40. Which factor is NOT considered while calculating national income?",
      "options": [
        "Income from illegal activities",
        "Salaries of employees",
        "Profits of firms",
        "Income from abroad"
      ],
      "answer": "Income from illegal activities",
      "segment": "Economics"
    },
    {
      "id": 41,
      "difficulty": "Hard",
      "question": "41. What does the 'Lorenz Curve' represent?",
      "options": [
        "The relationship between inflation and unemployment",
        "The distribution of income or wealth in a society",
        "The relationship between supply and demand",
        "The rate of economic growth over time"
      ],
      "answer": "The distribution of income or wealth in a society",
      "segment": "Economics"
    },
    {
      "id": 42,
      "difficulty": "Hard",
      "question": "42. What is 'opportunity cost' in economics?",
      "options": [
        "The cost of an alternative forgone",
        "The cost of production",
        "The cost of borrowing money",
        "The cost of advertising a product"
      ],
      "answer": "The cost of an alternative forgone",
      "segment": "Economics"
    },
    {
      "id": 43,
      "difficulty": "Hard",
      "question": "43. What does 'marginal utility' refer to?",
      "options": [
        "The total satisfaction from all units consumed",
        "The additional satisfaction from consuming one more unit of a good",
        "The utility derived from the most expensive product",
        "The utility derived from the least expensive product"
      ],
      "answer": "The additional satisfaction from consuming one more unit of a good",
      "segment": "Economics"
    },
    {
      "id": 44,
      "difficulty": "Hard",
      "question": "44. Which economist introduced the concept of 'invisible hand'?",
      "options": [
        "John Maynard Keynes",
        "Adam Smith",
        "Milton Friedman",
        "Karl Marx"
      ],
      "answer": "Adam Smith",
      "segment": "Economics"
    },
    {
      "id": 45,
      "difficulty": "Hard",
      "question": "45. What is the Phillips Curve used to illustrate?",
      "options": [
        "The relationship between inflation and unemployment",
        "The trade-off between national income and growth",
        "The relationship between demand and supply",
        "The growth rate of GDP"
      ],
      "answer": "The relationship between inflation and unemployment",
      "segment": "Economics"
    },
    {
      "id": 46,
      "difficulty": "Easy",
      "question": "46. What is the derivative of x²?",
      "options": ["2x", "x", "x²", "1"],
      "answer": "2x",
      "segment": "Maths"
    },
    {
      "id": 47,
      "difficulty": "Easy",
      "question": "47. What is the value of sin(90°)?",
      "options": ["0", "1", "-1", "0.5"],
      "answer": "1",
      "segment": "Maths"
    },
    {
      "id": 48,
      "difficulty": "Easy",
      "question": "48. Which of the following is the value of π (pi) up to two decimal places?",
      "options": ["3.12", "3.14", "3.15", "3.16"],
      "answer": "3.14",
      "segment": "Maths"
    },
    {
      "id": 49,
      "difficulty": "Easy",
      "question": "49. What is the solution of the equation 2x + 6 = 0?",
      "options": ["3", "-3", "0", "6"],
      "answer": "-3",
      "segment": "Maths"
    },
    {
      "id": 50,
      "difficulty": "Easy",
      "question": "50. What is the area of a triangle with base 4 and height 3?",
      "options": ["12", "7", "6", "10"],
      "answer": "6",
      "segment": "Maths"
    },
    {
      "id": 51,
      "difficulty": "Medium",
      "question": "51. What is the integral of 3x²?",
      "options": ["x³", "x³ + C", "3x³", "x⁴ + C"],
      "answer": "x³ + C",
      "segment": "Maths"
    },
    {
      "id": 52,
      "difficulty": "Medium",
      "question": "52. What is the value of tan(45°)?",
      "options": ["0", "1", "-1", "√3"],
      "answer": "1",
      "segment": "Maths"
    },
    {
      "id": 53,
      "difficulty": "Medium",
      "question": "53. If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∩ B?",
      "options": ["{1, 2}", "{3}", "{}", "{3, 4}"],
      "answer": "{3}",
      "segment": "Maths"
    },
    {
      "id": 54,
      "difficulty": "Medium",
      "question": "54. What is the determinant of the matrix [[1, 2], [3, 4]]?",
      "options": ["2", "-2", "1", "0"],
      "answer": "-2",
      "segment": "Maths"
    },
    {
      "id": 55,
      "difficulty": "Medium",
      "question": "55. What is the value of log₃(9)?",
      "options": ["1", "2", "3", "0"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 56,
      "difficulty": "Hard",
      "question": "56. What is the derivative of e^(x²)?",
      "options": ["2xe^(x²)", "e^(x²)", "x²e^(x²)", "0"],
      "answer": "2xe^(x²)",
      "segment": "Maths"
    },
    {
      "id": 57,
      "difficulty": "Hard",
      "question": "57. What is the radius of a circle whose equation is x² + y² - 4x - 6y + 9 = 0?",
      "options": ["1", "2", "3", "5"],
      "answer": "2",
      "segment": "Maths"
    },
    {
      "id": 58,
      "difficulty": "Hard",
      "question": "58. Find the solution set of the inequality 2x - 5 > 1.",
      "options": ["x > 3", "x < 3", "x > 2", "x < 2"],
      "answer": "x > 3",
      "segment": "Maths"
    },
    {
      "id": 59,
      "difficulty": "Hard",
      "question": "59. If the sum of the roots of a quadratic equation is 7 and the product is 10, what is the equation?",
      "options": ["x² - 7x + 10 = 0", "x² + 7x + 10 = 0", "x² + 7x - 10 = 0", "x² - 7x - 10 = 0"],
      "answer": "x² - 7x + 10 = 0",
      "segment": "Maths"
    },
    {
      "id": 60,
      "difficulty": "Hard",
      "question": "60. Evaluate ∫(1/(1 + x²)) dx.",
      "options": ["ln(1 + x²) + C", "tan⁻¹(x) + C", "x + C", "e^x + C"],
      "answer": "tan⁻¹(x) + C",
      "segment": "Maths"
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
