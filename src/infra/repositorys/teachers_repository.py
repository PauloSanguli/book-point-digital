from typing import Type

from src.domain.entities import TeacherProps
from src.domain.entities import TeacherProps

from src.application.repositorys import IRepositoryTeacher

from src.infra.models import engine, teachers, subjects

from sqlalchemy.orm import Session
from sqlalchemy import and_, select

from fastapi import HTTPException





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
