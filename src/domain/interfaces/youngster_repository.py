from abc import ABC, abstractmethod
from datetime import date
from src.domain.models.users import Youngster

class IYoungsterRepository(ABC):
    @abstractmethod
    def create_youngster(self, name: str, email: str, cpf: str, birth_date: date, cellphone: str, password: str, rg: str) -> Youngster:
        raise NotImplementedError