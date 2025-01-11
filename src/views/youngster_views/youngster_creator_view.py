
from src.views.interfaces.view_interface import ViewInterface
from src.controllers.youngster_controllers.youngster_creator_controller import YoungsterCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class YoungsterCreatorView(ViewInterface):
    def __init__(self, controller: YoungsterCreatorController):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body
        response = self.__controller.create(request)
        print(response)
        return HttpResponse(body=response, status_code=201)