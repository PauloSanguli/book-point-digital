from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.domain.entities import StudentProps

from src.infra.repositorys import RepositorySetudent

from src.infra.http.controllers import ControllerStudent as controller



post_student = APIRouter(prefix="/student", tags=["student"])

@post_student.post("/create")
async def create_student(props: StudentProps):
    RepositorySetudent.create(props)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "student reisted"
        }),
        status_code=status.HTTP_201_CREATED
    )

@post_student.post("/update")
def update_student(props: StudentProps, id_student: int):
    controller.update(props, id_student)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "student fields updated"
        }),
        status_code=status.HTTP_200_OK
    )
