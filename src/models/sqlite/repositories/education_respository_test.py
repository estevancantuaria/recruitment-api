from src.models.sqlite.repositories.education_respository import EducationRepository
from src.models.sqlite.entities.education import Escolaridade
from unittest.mock import Mock
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock



class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Escolaridade)],
                    [
                        Escolaridade(
                            user_id=1,
                            nivel="Ensino Fundamental",
                            instituicao="Escola Teste",
                            ano_conclusao=2020,
                            periodo_serie="1º ano"
                        )
                    ]
                )
            ]
        )

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
    
def test_list_all_education():
    mock_connection = MockConnection()
    repository = EducationRepository(mock_connection)
    
    educations = repository.list_all_education()
    
    mock_connection.session.query.assert_called_once_with(Escolaridade)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert educations[0].nivel == "Ensino Fundamental"
    
def test_delete_education():
    mock_connection = MockConnection()
    repository = EducationRepository(mock_connection)
    repository.delete_education(1)
    
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    