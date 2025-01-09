from src.models.sqlite.entities.education import Escolaridade
from src.models.sqlite.interfaces.education import IEducationRepository

class EducationRepository(IEducationRepository):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
                
    def insert_education(self, user_id: int, nivel: str, instituicao: str, ano_conclusao: int, periodo_serie: str):
        with self.__db_connection as database:
            try:
                education = Escolaridade(
                    user_id=user_id,
                    nivel=nivel,
                    instituicao=instituicao,
                    ano_conclusao=ano_conclusao,
                    periodo_serie=periodo_serie
                )
                database.session.add(education)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
    
    def list_all_education(self):
        with self.__db_connection as database:
            educations = database.session.query(Escolaridade).all()
            return educations
    
    def delete_education(self, id: int):
        with self.__db_connection as database:
            education = database.session.query(Escolaridade).filter(Escolaridade.id == id).first()
            database.session.delete(education)
            database.session.commit()
