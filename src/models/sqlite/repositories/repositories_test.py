import pytest
from src.models.sqlite.settings.connections import db_connection_handler
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_youngster():
    repository = YoungsterRepository(db_connection_handler)
    print(f"repository: {repository}")
    repository.insert_youngster(
        "Pessoa",
        "estevan@gmail.com",
        "123456",
        "1234567890",
        "1234567890",
        True,
        "JOVEM",
        "1234567890",
        "2000-01-01"
    )

