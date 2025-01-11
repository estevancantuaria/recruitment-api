from datetime import datetime
from src.models.sqlite.entities.users import Jovem
from src.controllers.youngster_controllers.youngster_finder_controller import YoungsterFinderController

class MockYoungsterRepository:
    def get_youngster_by_id(self, id: int) -> Jovem:
        return Jovem(id=1, nome="John Doe", email="john.doe@example.com", senha="password", cpf="1234567890", telefone="1234567890", ativo=True, tipo_usuario="jovem", rg="1234567890", data_nascimento="2000-01-01")

def test_find_youngster_by_id():
    mock_youngster_repository = MockYoungsterRepository()
    youngster_finder_controller = YoungsterFinderController(mock_youngster_repository)
    
    response = youngster_finder_controller.find_by_id(1)
    
    expected_response = {
        "data": {
            "type": "youngster",
            "count": 1,
            "attributes": {
                "id": 1,
                "nome": "John Doe",
                "email": "john.doe@example.com",
                "senha": "password",
                "cpf": "1234567890",
                "telefone": "1234567890",
                "ativo": True,
                "tipo_usuario": "jovem",
                "rg": "1234567890",
                "data_nascimento": "2000-01-01"
            }
        }
    }
    
    assert response == expected_response


