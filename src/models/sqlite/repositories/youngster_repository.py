from datetime import datetime
from src.models.sqlite.entities.users import Jovem, User
from src.models.sqlite.interfaces.youngster_repository import IYoungsterRepository

class YoungsterRepository(IYoungsterRepository):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def insert_youngster(self, nome: str, email: str, senha: str, cpf: str, telefone: str, ativo: bool, tipo_usuario: str, rg: str, data_nascimento: str) -> None:
        
        converted_date = self.__convert_to_date(data_nascimento)
        
        with self.__db_connection as database:
            try:
                user_data = Jovem(
                    nome=nome,
                    email=email,
                    senha=senha,
                    cpf=cpf,
                    telefone=telefone,
                    ativo=ativo,
                    tipo_usuario=tipo_usuario,
                    rg=rg,
                    data_nascimento=converted_date
                )
            
                database.session.add(user_data)
                database.session.commit()
                
            except Exception as e:
                database.session.rollback()
                raise e
        
    def __convert_to_date(self, data_nascimento: str) -> datetime:
        return datetime.strptime(data_nascimento, "%Y-%m-%d").date()
