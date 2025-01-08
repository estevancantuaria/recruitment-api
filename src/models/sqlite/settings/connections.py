from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///database.db"
        self.__engine = create_engine(self.__connection_string)
        self.Session = sessionmaker(bind=self.__engine)

    def __enter__(self):
        self.session = self.Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get_engine(self):
        return self.__engine

db_connection_handler = DBConnectionHandler()
