from unittest.mock import Mock, patch
from src.models.sqlite.repositories.address_repository import AddressRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.address import Address

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Address)],
                    [Address(user_id=1, rua="Rua Teste", numero="123", complemento="Complemento Teste", bairro="Bairro Teste", cidade="Cidade Teste", estado="Estado Teste", cep="1234567890")]
                )
            ]
        )
    
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

def test_delete_address():
    mock_connection = MockConnection()
    repository = AddressRepository(mock_connection)
    repository.delete_address(1)
    
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_get_address_by_user_id():
    mock_connection = MockConnection()
    repository = AddressRepository(mock_connection)
    address = repository.get_address_by_user_id(1)
    assert address is not None
    assert address.user_id == 1
