from abc import ABC, abstractmethod
from typing import Dict

class IYoungsterCreatorController(ABC):
    @abstractmethod
    def create(self, youngster_info: Dict) -> None:
        pass
