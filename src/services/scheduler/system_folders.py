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

            cls.create_subfolders()
    
    @classmethod
    def create_subfolders(cls) -> None:
        """create files in current directory"""
        constants = cls.get_constants()
        for c in range(constants["folders"]["classroom"]):
            zero_left = ""
            if c<=9: zero_left = "0"
            NAME_FILE = f"{zero_left}{c+1}"
            
            PATH_CLASSROOM_FOLDER = os.path.join(cls.FULL_PATH, cls.CURRENT_YEAR, NAME_FILE)
            
            os.makedirs(PATH_CLASSROOM_FOLDER)
            for item in constants["months"]:
                os.makedirs(os.path.join(PATH_CLASSROOM_FOLDER, item))

    @classmethod
    def get_constants(cls) -> any:
        """get the names of folders and files from json file"""
        constants = Path(os.path.join(PATH, "json", "constants.json")).read_text()
        return json.loads(constants)

