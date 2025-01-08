from abc import ABC, abstractmethod
from src.models.sqlite.entities.users import Jovem

class IYoungsterRepository(ABC):
    @abstractmethod
    def insert_youngster(self, name: str, email: str, senha: str, cpf: str, telefone: str, ativo: bool, tipo_usuario: str, rg: str, data_nascimento: str) -> None:
        pass
    
    @abstractmethod
    def delete_youngster(self, id: int) -> None:
        pass
    
    @abstractmethod
    def get_youngster_by_id(self, id: int) -> Jovem:
        pass