import os

from src.resources import PATH

import json

from pathlib import Path

from datetime import datetime



class CreateBooks:
    CURRENT_DATE = datetime.utcnow()
    FULL_PATH = os.path.join(PATH, "json")
    
    @classmethod
    def struture_file(cls) -> None:
        """create the struture of json file book"""
    
    @classmethod
    def map_folder(cls) -> None:
        """map folder to fetch all files"""
        FILES_CLASSROOM = os.listdir(os.path.join(cls.FULL_PATH, "times"))
        print(FILES_CLASSROOM)
        