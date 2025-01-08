from src.models.sqlite.repositories.education_respository import EducationRepository
from unittest.mock import Mock


class MockConnection:
    def __init__(self) -> None:
        self.session = Mock()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_insert_education():
    mock_connection = MockConnection()
    repository = EducationRepository(mock_connection)
    
    repository.insert_education(1, "Ensino Fundamental", "Escola Teste", 2020, "1º ano")
    
    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    mock_connection.session.rollback.assert_not_called()
    
    