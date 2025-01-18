from src.views.http_types.http_request import HttpRequest
from src.views.youngster_views.youngster_finder_view import YoungsterFinderView

class MockYoungsterFinderController:
    def find_by_id(self, id:int) -> dict:
         return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": {
                    "id": 2,
                    "nome": "Estevan",
                    "email": "estevan@gmail.com",
                    "senha": "123456",
                    "cpf": "1234567890",
                    "telefone": "1234567890",
                    "ativo": True,
                    "tipo_usuario": "JOVEM",
                    "rg": "12334444",
                    "data_nascimento": "2000-01-01"
                }
            }
        }

def test_youngster_finder_view():
    controller = MockYoungsterFinderController()
    view = YoungsterFinderView(controller)
    
    http_request = HttpRequest(body={
        "id": 2
    })
    
    response = view.handle(http_request)
    response_controller = controller.find_by_id(2)
    assert response.body == response_controller
    
    
    
    
    
    
