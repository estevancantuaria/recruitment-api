from abc import ABC, abstractmethod

class IYoungsterUpdateController(ABC):
    @abstractmethod
    def update_youngster(self, update_data: dict) -> None:
        pass
