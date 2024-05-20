from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.repositorys import RepositoryTeachers as repository



get_teacher = APIRouter(prefix="/teacher", tags=["teacher"])

@get_teacher.get("/all/")
def select_teachers():
    response = repository.get()
    
    return JSONResponse(
        content=jsonable_encoder(response)
    )    

