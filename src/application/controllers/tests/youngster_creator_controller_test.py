from src.application.controllers.youngster_creator_controller import YoungsterCreatorController
from unittest.mock import Mock

def test_create_youngster_controller():
    create_youngster_usecase = Mock()
    controller = YoungsterCreatorController(create_youngster_usecase)
    
    create_youngster_usecase.create_youngster.return_value = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "cpf": "12345678900",
        "birth_date": "1990-01-01",
        "cellphone": "1234567890",
        "rg": "1234567890"
    }
    
    result = controller.create_youngster({
        "name": "John Doe",
        "email": "john.doe@example.com",
        "cpf": "12345678900",
        "birth_date": "1990-01-01",
        "cellphone": "1234567890",
        "password": "senha123",
        "rg": "1234567890"
    })
    
    assert result == {
        "data": {
            "type": "youngster",
            "count": 1,
            "attributes": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "cpf": "12345678900",
                "birth_date": "1990-01-01",
                "cellphone": "1234567890",
                "rg": "1234567890"
            }
        }
    }