import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class DBConnectionHandler:
    DB_URL = os.getenv('DB_URL')
    def __init__(self) -> None:
        self.__connection_string = self.DB_URL
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()
