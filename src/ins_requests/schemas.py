from datetime import datetime

from pydantic import BaseModel


class GetInsRequest(BaseModel):
    id: int
    name: str
    note: str
    state: int
    created_at: datetime
    
    class Config:
        orm_mode = True
