from src.domain.models.users import Youngster
from src.infra.repositories.interfaces.youngster_repository import IYoungsterRepository
from datetime import date
from sqlalchemy.exc import SQLAlchemyError
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
            
    def update_youngster(self, youngster_id: int, **kwargs) -> None:

        with self.__db_connection as connection:
            try:
                youngster = connection.session.get(Youngster, youngster_id)
                
                if not youngster:
                    raise ValueError(f"Youngster com ID {youngster_id} não encontrado")

                invalid_fields = [key for key in kwargs if not hasattr(youngster, key)]
                if invalid_fields:
                    raise ValueError(f"Atributos inválidos: {', '.join(invalid_fields)}")

                for key, value in kwargs.items():
                    setattr(youngster, key, value)

                connection.session.commit()

            except Exception as e:
                connection.session.rollback()
                raise e