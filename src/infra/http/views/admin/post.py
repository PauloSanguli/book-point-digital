from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

from src.domain.entities import AdminProps

from src.infra.repositorys import RepositoryAdmin





post_admin = APIRouter(prefix="/book-school", tags=["admin"])


@post_admin.post("/login")
async def login_admin(props: AdminProps):
    response = RepositoryAdmin.login(props)
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=status.HTTP_201_CREATED
    )
