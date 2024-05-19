from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.http.controllers import ControllerStudent as controller



delete_student = APIRouter(prefix="/student", tags=["student"])


@delete_student.delete("/delete/")
async def del_student(id_student: int):
    controller.delete(id_student)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "studnet deleted"
        }),
        status_code=200
    )
