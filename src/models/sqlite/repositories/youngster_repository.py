from src.models.sqlite.entities.users import Jovem
from src.models.sqlite.interfaces.youngster_repository import IYoungsterRepository
from src.utils.convert_string_to_date import convert_string_to_date

class YoungsterRepository(IYoungsterRepository):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def insert_youngster(self, nome: str, email: str, senha: str, cpf: str, telefone: str, ativo: bool, tipo_usuario: str, rg: str, data_nascimento: str) -> None:
        
        converted_date = convert_string_to_date(data_nascimento)
        
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
    
    def update_youngster(self, update_data: dict) -> None:
        with self.__db_connection as database:
            try:
                youngster_to_update = database.session.query(Jovem).get(update_data['id'])
                updated_youngster = self.__update_youngster_attributes(youngster_to_update, update_data)
                database.session.commit()
                return updated_youngster
            except Exception as e:
                database.session.rollback()
                raise e
                
    def __update_youngster_attributes(self, youngster: Jovem, update_data: dict) -> None:
        for key, value in update_data.items():
            if hasattr(youngster, key):
                if key == 'data_nascimento':
                    value = convert_string_to_date(value)
                setattr(youngster, key, value)
        return youngster
        
