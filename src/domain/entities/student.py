from pydantic import BaseModel




class StudentProps(BaseModel):
    name: str
    course: str
    grade: str
    classroom: int
    turn: str
    photo: str | None = None
    