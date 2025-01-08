from abc import ABC, abstractmethod

class IAddressRepository(ABC):
    @abstractmethod
    def insert_address(self, user_id: int, rua: str, numero: str, complemento: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        pass