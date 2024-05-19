from pydantic import BaseModel
from pydantic import EmailStr



class AdminProps(BaseModel):
    email: EmailStr
    password: str

class AdminFields(BaseModel):
    email: EmailStr | None
    name: str | None
    photo: str | None
