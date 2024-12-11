from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict

# Quiz schema
class Quiz(BaseModel):
    id: str
    questions: List[Dict[str, List[str]]]

# Response schema
class QuizResponse(BaseModel):
    username: str  # User's username
    email: EmailStr
    user_id: str
    mobile_number: str  # Mobile number
    quizId: str
    responses: Dict[str, str]
