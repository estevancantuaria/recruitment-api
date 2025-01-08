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
    
    def get_youngster_by_id(self, id: int) -> Jovem:
        with self.__db_connection as database:
            try:
                jovem = (
                    database.session.query(Jovem)
                    .filter(Jovem.id == id)
                    .one()
                )
                return jovem
            except Exception as e:
                raise e
            
    def delete_youngster(self, id: int) -> None:
        with self.__db_connection as database:
            try:
                jovem = database.session.query(Jovem).filter(Jovem.id == id).one()
                database.session.delete(jovem)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update_youngster(self, id: int, nome: str, email: str, senha: str, cpf: str, telefone: str, ativo: bool, tipo_usuario: str, rg: str, data_nascimento: str) -> None:
        converted_date = self.__convert_to_date(data_nascimento)
        with self.__db_connection as database:
            try:
                youngster_to_update = database.session.query(Jovem).filter(Jovem.id == id).one()
                youngster_to_update.nome = nome
                youngster_to_update.email = email
                youngster_to_update.senha = senha
                youngster_to_update.cpf = cpf
                youngster_to_update.telefone = telefone
                youngster_to_update.ativo = ativo
                youngster_to_update.tipo_usuario = tipo_usuario
                youngster_to_update.rg = rg
                youngster_to_update.data_nascimento = converted_date
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
            
    def __convert_to_date(self, data_nascimento: str) -> datetime:
        return datetime.strptime(data_nascimento, "%Y-%m-%d").date()
