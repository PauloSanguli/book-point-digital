from src.resources import PATH

from fastapi import HTTPException

from pathlib import Path

import json

import os

from datetime import datetime



class HandlerJSON:
    def __init__(self, type, folder = "times"):
        self.__encode = json.dumps
        self.__decode = json.loads
        self.__path = os.path.join(PATH, type, folder)
    
    def read(self, filename: str) -> dict:
        """read datas on json file"""
        try:
            text_json = Path(os.path.join(self.__path, filename)).read_text()
            return self.__decode(text_json)
        except json.JSONDecodeError:
            print("error decoding")
            raise HTTPException(
                detail="error decoding json, file is empty",
                status_code=400
            )

    def read_all(self) -> list:
        """read all times"""
        files = os.listdir(self.__path)
        times = []
        
        for file in files:
            key_ = file[1:file.index(".")]
            times.append({
                f"{key_}": self.read(file)
            })
        return times

    
    def update_times(self, classroom: str, turn: str, updates: dict) -> None:
        """update times"""
        files = os.listdir(self.__path)
        
        for file in files:
            if classroom in file:
                old_times = self.read(file)
                old_times[f"{turn}"] = updates
                self.regist_datas(file, old_times)

    def regist_datas(self, filename: str, datas: any) -> None:
        """update file json"""
        path_file = os.path.join(self.__path, filename)
        with open(path_file, "w") as file:
            file.write(self.__encode(datas, indent=4))
            file.close()

    @staticmethod
    def count_books() -> int:
        """count number of books"""
        CURRENT_YEAR = str(datetime.utcnow().date().year)
        PATHBOOKNOW = os.path.join(
            PATH, "json", "books", CURRENT_YEAR
        )
        booksListed = os.listdir(PATHBOOKNOW)
        return len(booksListed)*2
        