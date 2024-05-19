from abc import ABC, abstractmethod

from src.domain.entities import TeacherProps as model

from typing import Type



class IRepositoryTeacher(ABC):
    @abstractmethod
    def create(teacher: Type[model]) -> dict:
        """regist  on db"""
        raise NotImplementedError("implement method create")
    
    @abstractmethod
    def get() -> list:
        """get all teachers from db"""
        raise NotImplementedError("implement mehtod get")

    @abstractmethod
    def regist_subject(subject: str, id_teacher: int) -> None:
        """regist subject on db"""
        raise NotImplementedError("implement method regist_subject")
