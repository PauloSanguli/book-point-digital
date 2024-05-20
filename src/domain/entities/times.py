from pydantic import BaseModel





class Times(BaseModel):
    turn: str
    classroom: str
    time: dict
