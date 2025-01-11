from src.controllers.youngster_controllers.youngster_update_controller import YoungsterUpdateController


class MockYoungsterRepository:
    def update_youngster(self, update_data: dict) -> None:
        return update_data

def test_update_youngster():
    jovem = {
        "id": 1,
        "nome": "Matheus",
        "data_nascimento": "1999-01-01"
    }
    
    repository = MockYoungsterRepository()
    controller = YoungsterUpdateController(repository)
    response = controller.update_youngster(jovem)
    
    assert response["data"]["attributes"]["nome"] == jovem["nome"]
    assert response["data"]["attributes"]["data_nascimento"] == jovem["data_nascimento"]

