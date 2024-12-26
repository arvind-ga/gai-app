from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict

# Quiz schema
class BookingRequest(BaseModel):
    username: str
    dateTime: str
    remark: str

