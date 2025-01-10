from typing import Dict
from abc import ABC, abstractmethod

class YoungsterCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, jovem_info: Dict) -> Dict:
        pass
