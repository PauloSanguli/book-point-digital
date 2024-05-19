from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.repositorys import RepositorySetudent


get_student = APIRouter(prefix="/student", tags=["student"])


@get_student.get("/all/")
async def select_students():
    response = RepositorySetudent.get()
    
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=200
    )
