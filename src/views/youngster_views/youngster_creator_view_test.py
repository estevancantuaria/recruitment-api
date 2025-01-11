from src.views.youngster_views.youngster_creator_view import YoungsterCreatorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockYoungsterController:
    def create(self, youngster_info: dict) -> dict:
        return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": youngster_info
            }
        }
    
def test_youngster_creator_view():
    controller = MockYoungsterController()
    view = YoungsterCreatorView(controller)
    
    http_request = HttpRequest(body={
        "nome": "Pessoa",
        "email": "estevan@gmail.com",
        "senha": "123456",
        "cpf": "1234567890",
        "telefone": "1234567890",
        "ativo": True,
        "tipo_usuario": "JOVEM",
        "rg": "12334444",
        "data_nascimento": "2000-01-01"
    })
    
    assert http_request.body == {
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
    
    response = view.handle(http_request)
    assert response is not None
    assert response.status_code == 201
    assert response.body is not None
    assert response.body["data"]["attributes"]["nome"] == "Pessoa"