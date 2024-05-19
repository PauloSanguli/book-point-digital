from src.domain.entities import StudentProps

from src.infra.models import student, engine

from sqlalchemy.orm import Session
from sqlalchemy import and_

from fastapi import HTTPException


class ControllerStudent:
    def delete(id_student: int) -> None:
        """remove student from db"""
        try:
            with Session(engine) as session:
                session.execute(student.delete().\
                    where(and_(student.c.id==id_student)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="student dont deleted",
                status_code=400
            )
    
    def update(student_props: StudentProps, id_student: int) -> None:
        """update student fields"""
        try:
            dic = student_props.model_dump()
            model_formated = {}
            for index, key in enumerate(dic):
                if dic[key]:
                    model_formated[key] = dic[key]
                
            with Session(engine) as session:
                session.execute(student.update().\
                    values(model_formated).\
                        where(and_(student.c.id==id_student)))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="student fields dont updated",
                status_code=400
            )
    