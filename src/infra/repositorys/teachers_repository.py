from typing import Type

from src.domain.entities import TeacherProps
from src.domain.entities import TeacherProps

from src.application.repositorys import IRepositoryTeacher

from src.infra.models import engine, teachers, subjects

from sqlalchemy.orm import Session
from sqlalchemy import and_, select

from fastapi import HTTPException

from src.infra.http.responses.responses import Response





class RepositoryTeachers(IRepositoryTeacher):
    def create(teacher_props: type[TeacherProps]) -> dict:
        """regist techers on db"""
        try:
            with Session(engine) as session:
                id_teacher = session.execute(teachers.insert().values({
                    "name": teacher_props.name,
                    "turn": teacher_props.turn,
                    "photo": teacher_props.photo
                }).returning(teachers.c.id)).fetchone()[0]
                print(id_teacher)
                
                session.commit()
        except Exception as error:
            print(error)
            raise HTTPException(
                detail="teacher dont registed",
                status_code=400
            )
        RepositoryTeachers.regist_subject(teacher_props.subject, id_teacher)
            
    def regist_subject(subject: str, id_teacher: int) -> None:
        """regist subject of an teacher on db"""    
        try:
            with Session(engine) as session:
                session.execute(subjects.insert().values({
                    "subject": subject,
                    "teacher_id": id_teacher
                }))
                session.commit()
        except Exception as error:
            print(error)
            raise NotImplementedError(
                detail="error recording subjects",
                status_code=400
            )

    def get() -> list:
        """select teachers from db"""
        with Session(engine) as session:
            query = select(
                teachers.c.id,
                teachers.c.name,
                teachers.c.turn,
                teachers.c.photo,
                subjects.c.subject).select_from(
                    teachers.join(
                        subjects, teachers.c.id==subjects.c.teacher_id
                    )
                )
            results = session.execute(query).fetchall()
        return Response.get_teachers(results)
    
    def select_teacher(name: str) -> type[list]:
        """select teacher by the name"""
        with Session(engine) as session:
            teacher_finded = session.execute(select(teachers, subjects.c.subject).select_from(
                teachers.join(subjects, teachers.c.id==subjects.c.teacher_id)    
            ).\
            where(and_(teachers.c.name.like(name)))).fetchone()
        return teacher_finded
