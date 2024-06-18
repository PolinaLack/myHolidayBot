from pydantic import BaseModel

class Holiday(BaseModel):
    user_name: str
    start: str
    end_date: str