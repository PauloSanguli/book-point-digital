from typing import Type

from src.domain.entities import StudentProps as model
from src.domain.entities import StudentProps

from src.application.repositorys import IRepositoryStudent

from src.infra.models import engine, student

from sqlalchemy.orm import Session
from sqlalchemy import and_, select

from fastapi import HTTPException

from src.infra.http.responses.responses import Response



class RepositorySetudent(IRepositoryStudent):
    def create(student_props: StudentProps) -> dict:
        """regist student on db"""
        try:
            with Session(engine) as session:
                session.execute(student.insert().values(student_props.model_dump()))
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="student dont registed",
                status_code=400
            )
    
    def get() -> list:
        """select students from db"""
        with Session(engine) as session:
            query = select(
                student.c.id,
                student.c.name,
                student.c.grade,
                student.c.course,
                student.c.classroom,
                student.c.turn,
                student.c.photo)
            results = session.execute(query).fetchall()
        return Response.get_students(results)
            
