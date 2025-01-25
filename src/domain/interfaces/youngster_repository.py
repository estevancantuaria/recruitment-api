from abc import ABC, abstractmethod
from datetime import date

class IYoungsterRepository(ABC):
    @abstractmethod
    def create_youngster(self, name: str, email: str, cpf: str, birth_date: date, cellphone: str, password: str, rg: str) -> None:
        raise NotImplementedError