from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.infra.repositories.youngster_repository import YoungsterRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass

def test_create_youngster():
    mock_connection = MockConnection()
    repository = YoungsterRepository(mock_connection)
    
    youngster = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "cpf": "12345678900",
        "birth_date": "1990-01-01",
        "cellphone": "1234567890",
        "password": "password",
        "rg": "123456789"
    }
    
    repository.create_youngster(youngster["name"], youngster["email"], youngster["cpf"], youngster["birth_date"], youngster["cellphone"], youngster["password"], youngster["rg"])