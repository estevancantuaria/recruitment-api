from src.controllers.youngster_controllers.youngster_creator_controller import YoungsterCreatorController

class MockYoungsterRepository:
    def insert_youngster(self, nome: str, email: str, senha: str, cpf: str, telefone: str, ativo: bool, tipo_usuario: str, rg: str, data_nascimento: str) -> None:
        return None

def test_create_youngster():
    mock_youngster_repository = MockYoungsterRepository()
    youngster_creator_controller = YoungsterCreatorController(mock_youngster_repository)
    youngster_info = {
        "nome": "John Doe",
        "email": "john.doe@example.com",
        "senha": "password",
        "cpf": "1234567890",
        "telefone": "1234567890",
        "ativo": True,
        "tipo_usuario": "jovem",
        "rg": "1234567890",
        "data_nascimento": "1990-01-01"
    }
    
    response = youngster_creator_controller.create(youngster_info)
    
    assert response == {
        "data": {
            "type": "youngster",
            "count": 1,
            "attributes": youngster_info
        }
    }
    
    assert response['data']['attributes']['nome'] == youngster_info['nome']