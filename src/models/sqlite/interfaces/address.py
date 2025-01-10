from abc import ABC, abstractmethod
from src.models.sqlite.entities.address import Address
class IAddressRepository(ABC):
    @abstractmethod
    def insert_address(self, user_id: int, rua: str, numero: str, complemento: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        pass
    
    @abstractmethod
    def get_address_by_user_id(self, user_id: int) -> Address:
        pass
    
    @abstractmethod
    def delete_address(self, user_id: int) -> None:
        pass