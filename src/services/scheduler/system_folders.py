import os

from src.resources import PATH

import json

from pathlib import Path

from datetime import datetime





class CreateFolders:
    CURRENT_YEAR = str(datetime.utcnow().date().year)
    FULL_PATH = os.path.join(PATH, "json", "books")
    
    @classmethod
    def create_folders(cls) -> None:
        """create folders in current directory"""
        full_path = os.path.join(cls.FULL_PATH, cls.CURRENT_YEAR)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

            cls.__create_subfolders()
    
    @classmethod
    def __create_subfolders(cls) -> None:
        """create files in current directory"""
        constants = cls.__get_constants()
        for c in range(constants["folders"]["classroom"]):
            name_file = f"{c+1}"
            if len(name_file) == 1: name_file = "0"+name_file
            
            PATH_CLASSROOM_FOLDER = os.path.join(cls.FULL_PATH, cls.CURRENT_YEAR, name_file)
            
            os.makedirs(PATH_CLASSROOM_FOLDER)
            for item in constants["months"]:
                os.makedirs(os.path.join(PATH_CLASSROOM_FOLDER, item))

    @classmethod
    def __get_constants(cls) -> any:
        """get the names of folders and files from json file"""
        constants = Path(os.path.join(PATH, "json", "constants.json")).read_text()
        return json.loads(constants)

