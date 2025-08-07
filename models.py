from pydantic import BaseModel, Field
from datetime import datetime


class RequestModel(BaseModel):
    operation: str
    input: str
    output: int
    timestamp: datetime = Field(default_factory=datetime.now)
