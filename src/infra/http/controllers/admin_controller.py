from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.infra.models import engine, admin

from src.application.security import SecurityPWD

from src.domain.validators import validate
from src.domain.entities import Times

from fastapi import HTTPException

from src.domain.entities import AdminFields

from src.infra.handlers import HandlerJSON

from typing import Type





class AdminController:
    def alter_password(id_admin: str, password: str) -> None:
        """alter password"""
        PASSWORD_CHECK = validate(password)
        if not PASSWORD_CHECK:
            raise HTTPException(
                detail="invalid format of password",
                status_code=400
            )
        try:
            PASSWORD_HASHED = SecurityPWD.has_password(password)
            with Session(engine) as session:
                session.execute(admin.update().values({
                    "password": PASSWORD_HASHED
                }).where(and_(admin.c.id==id_admin)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="check the email",
                status_code=400
            )

    def edit_account(id_admin: int, admin_props: AdminFields) -> None:
        """change datas admin"""
        dic = admin_props.model_dump()
        model_formated = {}
        for _, key in enumerate(dic):
            if dic[key]:
                model_formated[key] = dic[key]
        try:
            with Session(engine) as session:
                session.execute(admin.update().values(model_formated).\
                    where(and_(admin.c.id==id_admin)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="account dont updated",
                status_code=400
            )


    def update_time(props: Type[Times]) -> None:
        """update time of an classroom"""
        try:
            handler = HandlerJSON("json")
            handler.update_times(props.classroom, props.turn, props.time)
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="time dont updated",
                status_code=200
            )
