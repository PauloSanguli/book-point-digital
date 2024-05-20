from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Depends

from src.infra.http.controllers import AdminController as controller

from src.infra.http.middleware import JWTTokenExceptionHandler

from src.domain.entities import AdminFields
from src.domain.entities import Times

from typing import Annotated




patch_admin = APIRouter(prefix="/admin", tags=["admin"])

@patch_admin.patch("/alter-password/")
async def alter_password(id_admin: int, password: str):
    controller.alter_password(id_admin, password)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "password altered"
        }),
        status_code=status.HTTP_200_OK
    )

@patch_admin.patch("/edit-account/")
def edit_account(account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)], props: AdminFields):
    controller.edit_account(account_logged["id"], props)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "account adited"
        })
    )

@patch_admin.patch("/time")
def update_time(props: Times):
    controller.update_time(props)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "time updated"
        }),
        status_code=200
    )
