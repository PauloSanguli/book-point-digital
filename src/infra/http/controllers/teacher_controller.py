from src.domain.entities import TeacherProps

from src.infra.models import engine, teachers, subjects

from sqlalchemy.orm import Session
from sqlalchemy import and_

from fastapi import HTTPException


class ControllerTeacher:
    @classmethod
    def delete(cls, id_teacher: int) -> None:
        """remove teacher from db"""
        cls.delete_subject(id_teacher)
        try:
            with Session(engine) as session:
                session.execute(teachers.delete().\
                    where(and_(teachers.c.id==id_teacher)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="teacher dont deleted",
                status_code=400
            )
    
    @classmethod
    def delete_subject(cls, id_teacher: int) -> None:
        """remove subjects form db"""
        try:
            with Session(engine) as session:
                session.execute(subjects.delete().\
                    where(and_(subjects.c.teacher_id==id_teacher)))
                session.commit()
        except Exception as error:
            print(error)
            
            raise HTTPException(
                detail="subject and teacher dont deleted",
                status_code=400
            )

    @classmethod
    def update(cls, teacher_props: TeacherProps, id_teacher: int) -> None:
        """update teacher fields"""
        try:
            dic = teacher_props.model_dump()
            model_formated = {}
            for index, key in enumerate(dic):
                if dic[key]:
                    model_formated[key] = dic[key]
                    
            with Session(engine) as session:
                session.execute(teachers.update().\
                    values(model_formated).\
                        where(and_(teachers.c.id==id_teacher)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="teacher fields dont updated",
                status_code=400
            )
    