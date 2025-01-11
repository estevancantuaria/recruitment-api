from abc import ABC, abstractmethod 

class IYoungsterDeleterController(ABC):
    
    @abstractmethod
    def delete_youngster(self, id: int) -> None:
        pass