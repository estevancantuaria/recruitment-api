from unittest.mock import Mock, patch
from src.models.sqlite.repositories.address_repository import AddressRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = Mock()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
def test_insert_address():
    mock_connection = MockConnection()
    repository = AddressRepository(mock_connection)
    address = {
        "user_id": 1,
        "rua": "Rua Teste",
        "numero": "123",
        "complemento": "Complemento Teste",
        "bairro": "",
        "cidade": "Cidade Teste",
        "estado": "Estado Teste",
        "cep": "1234567890"
    }
    repository.insert_address(**address)
    
    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    mock_connection.session.rollback.assert_not_called()
    
