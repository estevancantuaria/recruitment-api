from abc import ABC, abstractmethod
from datetime import date

class ICreateYoungsterUsecase(ABC):
    @abstractmethod
    def create_youngster(self, youngster_info: dict) -> dict:
        pass