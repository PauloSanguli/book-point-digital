from src.resources import PATH

from pathlib import Path

import json

import os




class HandlerJSON:
    def __init__(self, type, filename):
        self.__encode = json.dumps
        self.__decode = json.loads
        self.__path = os.path.join(PATH, type, filename)
    
    def read(self) -> dict:
        """read datas on json file"""
        text_json = Path(self.__path).read_text()
        return self.__decode(text_json)
