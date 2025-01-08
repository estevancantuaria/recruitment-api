import pytest
from src.models.sqlite.settings.connections import db_connection_handler
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository
from src.models.sqlite.repositories.address_repository import AddressRepository
from src.models.sqlite.repositories.education_respository import EducationRepository
from src.models.sqlite.entities.users import Jovem

@pytest.mark.skip(reason="interacao com o banco") 
def test_insert_youngster():
    repository = YoungsterRepository(db_connection_handler)
    print(f"repository: {repository}")
    repository.insert_youngster(
        "Paulo",
        "paulo@gmail.com",
        "123456",
        "1234567890",
        "1234567890",
        True,
        "JOVEM",
        "1234567890",
        "2000-01-01"
    )
@pytest.mark.skip(reason="interacao com o banco") 
def test_insert_address():
    repository = AddressRepository(db_connection_handler)
    repository.insert_address(
        4,
        "Rua Teste",
        "123",
        "Complemento Teste",
        "",
        "Cidade Palmas",
        "Estado TO",
        "77002018"
    )

@pytest.mark.skip(reason="interacao com o banco") 
def test_insert_education():
    repository = EducationRepository(db_connection_handler)
    repository.insert_education(5, "Ensino Fundamental", "Escola Teste", 2020, "1º ano")
    
@pytest.mark.skip(reason="interacao com o banco") 
def test_get_youngster_by_id():
    repository = YoungsterRepository(db_connection_handler)
    jovem = repository.get_youngster_by_id(5)
    assert jovem is not None
    


def test_update_youngster():
    repository = YoungsterRepository(db_connection_handler)
    update_data = {
        "id": 5,
        "nome": "Raquel",
        "data_nascimento": "1999-01-01"
    }
    repository.update_youngster(update_data)

# 
# def test_delete_youngster():
#     repository = YoungsterRepository(db_connection_handler)
#     repository.delete_youngster(5)


