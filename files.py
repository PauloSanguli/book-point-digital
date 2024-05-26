from src.services.scheduler import CreateBooks


if __name__=="__main__":
    book_ = CreateBooks()
    book_.map_folder()