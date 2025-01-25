from src.domain.models.users import Youngster
from src.infra.repositories.interfaces.youngster_repository import IYoungsterRepository
from datetime import date

class YoungsterRepository(IYoungsterRepository):
    
    def __init__(self, db_connection_handler):
        self.__db_connection = db_connection_handler
    
    def create_youngster(self, name: str, email: str, cpf: str, birth_date: date, cellphone: str, password: str, rg: str) -> None:
        with self.__db_connection as connection:
            try:
                data = Youngster(name=name, email=email, cpf=cpf, birth_date=birth_date, cellphone=cellphone, password=password, rg=rg)
                connection.session.add(data)
                connection.session.commit()
            except:
                connection.session.rollback()
                raise