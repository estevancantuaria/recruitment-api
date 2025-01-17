from unittest.mock import Mock, patch
from unittest import mock
import pytest
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository
from src.models.sqlite.entities.users import Jovem
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.utils.convert_string_to_date import convert_string_to_date
class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Jovem)],
                    [Jovem(id=5,nome="Pessoa", email="estevan@gmail.com", senha="123456", cpf="1234567890",
                           telefone="1234567890", ativo=True, tipo_usuario="JOVEM", rg="12334444",
                           data_nascimento="2000-01-01")]
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
def test_insert_youngster():
    mock_connection = MockConnection()
    repository = YoungsterRepository(mock_connection)
    jovem = {
        "nome": "Pessoa",
        "email": "estevan@gmail.com",
        "senha": "123456",
        "cpf": "1234567890",
        "telefone": "1234567890",
        "ativo": True,
        "tipo_usuario": "JOVEM",
        "rg": "12334444",
        "data_nascimento": "2000-01-01"
    }
    
    # Act
    repository.insert_youngster(**jovem)

    # Assert
    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_get_youngster_by_id():
    mock_connection = MockConnection()
    repository = YoungsterRepository(mock_connection)
    
    jovem = repository.get_youngster_by_id(1)

    assert jovem is not None
    assert jovem.nome == "Pessoa"
    assert jovem.email == "estevan@gmail.com"
    
    mock_connection.session.query.assert_called_once()
    mock_connection.session.query.assert_called_with(Jovem)
    mock_connection.session.query().filter.assert_called_once()
    mock_connection.session.query().filter().one.assert_called_once()
    
def test_delete_youngster():
    mock_connection = MockConnection()
    repository = YoungsterRepository(mock_connection)
    repository.delete_youngster(1)
    
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    
def test_update_youngster():
    mock_connection = MockConnection()
    repository = YoungsterRepository(mock_connection) 
    
    update_data = {
        "id": 5,
        "nome": "Matheus",
        "data_nascimento": "1999-01-01"
    }
    result =repository.update_youngster(update_data)
    
    assert result.nome == "Matheus"
    
    converted_date = convert_string_to_date(update_data["data_nascimento"])
    
    assert result.data_nascimento == converted_date
    
    mock_connection.session.query.assert_called_once_with(Jovem)
    mock_connection.session.query().get.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    
    
  
    
    
    
    
