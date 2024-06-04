from src.services.scheduler import CreateBooks, CreateFolders

from datetime import datetime


if __name__=="__main__":
    folder_ = CreateFolders()
    folder_.create_folders()
    
    book_ = CreateBooks()
    # print(datetime.now().month)
    book_.map_folder()
