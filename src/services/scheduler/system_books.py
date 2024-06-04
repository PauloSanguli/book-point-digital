import os

from src.resources import PATH

import json

from pathlib import Path

from datetime import datetime

from src.infra.repositorys import RepositoryTeachers as repository



class CreateBooks:
    CURRENT_DATE = datetime.utcnow()
    FULL_PATH = os.path.join(PATH, "json")
    DAYS = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday"
    }

    
    @classmethod
    def map_folder(cls) -> None:
        """map folder to fetch all files"""
        PATH_CLASSROOM_FILES = os.path.join(cls.FULL_PATH, "times")
        FILES_CLASSROOM = os.listdir(PATH_CLASSROOM_FILES)
        for classroom_file in FILES_CLASSROOM:
            year = cls.CURRENT_DATE.year
            month = cls.CURRENT_DATE.month
            day = cls.CURRENT_DATE.weekday()+1
            dic = {
                "morning": [],
                "afternoon": []
            }
            classroom_number = classroom_file[1:classroom_file.index(".")]
            time_classroom = json.loads(Path(os.path.join(PATH_CLASSROOM_FILES, classroom_file)).\
                read_text())
            
            if month < 10: month = f"0{month}"
            
            file_path = cls.__filter_folders(
                classroom=classroom_number,
                year=year,
                month=month
            )
            for item in time_classroom:
                for time_item in time_classroom[item]:
                    TIME_TODAY = time_classroom[item][time_item]
                    if cls.DAYS[day]==time_item:
                        for key_ in TIME_TODAY:
                            result = repository.select_teacher((TIME_TODAY[key_]))
                    
                            dic[item].append({
                                "time": key_,
                                "subject": result[4],
                                "students": [],
                                "teacher": result[1],
                                "status": 0,
                                "id": result[0]
                            })
            cls.__write_book(file_path, dic)

    
    @classmethod
    def __filter_folders(cls, classroom: str, year: str, month: str, day: str = None) -> str:
        """find the current book"""
        month = cls.get_extense_month(month, str(year), classroom)
        
        PATH_TO_FILE_COMPLETE = os.path.\
            join(
                cls.FULL_PATH,
                "books",
                str(year),
                classroom,
                month,
                f"{datetime.utcnow().date()}.json"
            )
        with open(PATH_TO_FILE_COMPLETE, "w") as file:
            file.close()
        return PATH_TO_FILE_COMPLETE
    
    
    @classmethod
    def __write_book(cls, file_path: str, dic: dict) -> None:
        """regist book on json file"""
        with open(file_path, "a+") as file:
            file.writelines(json.dumps(dic, indent=3))
            file.close()


    @classmethod
    def get_extense_month(cls, month_number: str, year: str, classroom: str) -> str:
        """get month in extense"""
        path_classroom_folder = os.path.join(cls.FULL_PATH, "books", year, classroom)
        FETCH_MONTHS = os.listdir(path_classroom_folder)
        for month_ in FETCH_MONTHS:
            if month_number in month_: 
                return month_
