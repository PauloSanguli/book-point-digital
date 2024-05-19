from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.http.controllers import ControllerTeacher as controller



delete_teacher = APIRouter(prefix="/teacher", tags=["teacher"])



@delete_teacher.delete("/delete/")
async def del_teacher(id_teacher: int):
    controller.delete(id_teacher)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "teacher deleted"
        })
    )
