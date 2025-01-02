from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict
from datetime import datetime

# Quiz schema
class BookingRequest(BaseModel):
    bookingId: str
    username: str
    bookingTime: datetime  # This should match the format you're sending (ISO 8601)
    dateTime: datetime  # Same here
    remark: str

    class Config:
        # Ensure FastAPI understands the date format you're using
        json_encoders = {
            datetime: lambda v: v.isoformat(),  # Convert datetime to ISO format if needed
        }

