from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Depends

from typing import Annotated

from src.infra.http.middleware import JWTTokenExceptionHandler

from src.infra.repositorys import RepositoryAdmin as repository

from src.infra.http.controllers import AdminController as controller

from src.infra.handlers import HandlerJSON



get_admin = APIRouter(prefix="/admin", tags=["admin"])


@get_admin.get("/datas/")
async def datas_admin(account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)]):
    response = repository.get(account_logged["id"])
    
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=200
    )
    
@get_admin.get("/times/")
async def get_times():
    handler = HandlerJSON("json")
    response = handler.read_all()
    
    return JSONResponse(
        content=jsonable_encoder(response)
    )
