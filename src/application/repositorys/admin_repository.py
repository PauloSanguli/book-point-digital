from abc import ABC, abstractmethod

from src.domain.entities import AdminProps

from typing import Type




class IRepositoryAdmin(ABC):
    @abstractmethod
    def login(admin: Type[AdminProps]) -> dict:
        """login for admin"""
        raise NotImplementedError("implement method login")
    
    @abstractmethod
    def get(id_admin: int) -> dict:
        """get datas admin"""
        raise NotImplementedError("implement method get")
