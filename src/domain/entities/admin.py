from pydantic import BaseModel
from pydantic import EmailStr



class AdminProps(BaseModel):
    email: EmailStr
    password: str
