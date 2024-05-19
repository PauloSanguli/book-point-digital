from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Depends

from typing import Annotated

from src.infra.http.middleware import JWTTokenExceptionHandler

from src.infra.repositorys import RepositoryAdmin as repository



get_admin = APIRouter(prefix="/admin", tags=["admin"])


@get_admin.get("/datas/")
async def datas_admin(account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)]):
    response = repository.get(account_logged["id"])
    
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=200
    )
