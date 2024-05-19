from abc import ABC, abstractmethod

from src.domain.entities import StudentProps as model

from typing import Type



class IRepositoryStudent(ABC):
    @abstractmethod
    def create(student: type[model]) -> dict:
        """regist student on db"""
        raise NotImplementedError("implement method create")
    
    @abstractmethod
    def get() -> list:
        """get all students from db"""
        raise NotImplementedError("implement mehtod get")
