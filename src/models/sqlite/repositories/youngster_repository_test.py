from unittest.mock import Mock, patch
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository
from src.models.sqlite.entities.users import Jovem
class MockConnection:
    def __init__(self) -> None:
        self.session = Mock()
    
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
    
    
    
  
    
    
    
    
