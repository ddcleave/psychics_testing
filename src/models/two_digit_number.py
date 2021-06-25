from fastapi import Form
from pydantic.main import BaseModel


class TwoDigitNumber(BaseModel):
    number: int = Form(..., ge=10, le=99)
