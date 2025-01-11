from abc import ABC, abstractmethod
from src.models.sqlite.entities.users import Jovem

class IYoungsterFinderController(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Jovem:
        pass
