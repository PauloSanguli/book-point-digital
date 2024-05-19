from typing import Type

from src.domain.entities.admin import AdminProps

from src.application.repositorys import IRepositoryAdmin

from src.infra.models import engine, admin

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import and_, select

from src.application.security import SecurityPWD
from src.infra.http.middleware import TokenHandler

from src.domain.validators import validate as validate_password

from fastapi import HTTPException




class RepositoryAdmin(IRepositoryAdmin):
    def login(admin_props: Type[AdminProps]) -> dict:
        """login for admin"""
        
        PASSWORD_AVAILABLE = not validate_password(admin_props.password)
        if PASSWORD_AVAILABLE:
            raise HTTPException(
                detail="invalid format of password",
                status_code=400
            )
        with Session(engine) as session:
            query = select(admin.c.password, admin.c.id).where(and_(admin.c.email==admin_props.email))
            datas = session.execute(query).fetchone()
        
            if not datas: 
                raise HTTPException(
                detail="email dont finded",
                status_code=404
            )
        
        PASSWORD_CHECK = SecurityPWD.\
            check_password_hashed(admin_props.password, datas[0])
        
        if PASSWORD_CHECK:
            return {
                "token": TokenHandler.create_token(datas[1])
            }
        raise HTTPException(
            detail="invalid password",
            status_code=400
        )
            
    def get(id_admin: int) -> dict:
        """get datas of admin"""
        with Session(engine) as session:
            query = select(
                admin.c.name,
                admin.c.email,
                admin.c.photo
            ).where(and_(admin.c.id==id_admin))
            datas = session.execute(query).fetchone()
        if not datas:
            raise HTTPException(
                detail="datas dont found",
                status_code=404
            )
        return {
            "name": datas[0],
            "email": datas[1],
            "photo": datas[2]
        }
