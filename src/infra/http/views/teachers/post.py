from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.domain.entities import TeacherProps

from src.infra.repositorys import RepositoryTeachers

from src.infra.http.controllers import ControllerTeacher as controller



post_teacher = APIRouter(prefix="/teacher", tags=["teacher"])

@post_teacher.post("/create")
async def create_teacher(props: TeacherProps):
    RepositoryTeachers.create(props)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "teacher reisted"
        }),
        status_code=status.HTTP_201_CREATED
    )

@post_teacher.post("/update")
def update_teacher(props: TeacherProps, id_teacher: int):
    controller.update(props, id_teacher)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "teacher fields updated"
        }),
        status_code=200
    )
