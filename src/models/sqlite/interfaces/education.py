from src.models.sqlite.entities.education import Escolaridade
from abc import ABC, abstractmethod

class IEducationRepository(ABC):
    @abstractmethod
    def insert_education(self, user_id: int, nivel: str, instituicao: str, ano_conclusao: int, periodo_serie: str):
        pass