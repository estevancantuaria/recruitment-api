import pytest
from src.infra.database.connection import db_connection_handler
from src.infra.repositories.youngster_repository import YoungsterRepository

db_connection_handler.connect_to_db()

# @pytest.mark.skip(reason="interacao com o banco")
# def test_create_youngster():
#     repo = YoungsterRepository(db_connection_handler)
#     repo.create_youngster("John Doe", "john.doe@example.com", "1234567890", "1990-01-01", "1234567890", "password", "1234567890")
    
def test_update_youngster():
    repo = YoungsterRepository(db_connection_handler)
    repo.update_youngster(1, name="Estevan", email="teste2@mail.com")