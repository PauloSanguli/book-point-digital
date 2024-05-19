from pydantic import BaseModel




class TeacherProps(BaseModel):
    name: str
    turn: str
    subject: str
    photo: str | None = None
