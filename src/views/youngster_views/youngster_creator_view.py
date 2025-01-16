
from src.views.interfaces.view_interface import ViewInterface
from src.controllers.youngster_controllers.youngster_creator_controller import YoungsterCreatorController
from src.validators.youngster_creator_validator import youngster_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class YoungsterCreatorView(ViewInterface):
    def __init__(self, controller: YoungsterCreatorController):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        youngster_creator_validator(http_request)
        request = http_request.body
        response = self.__controller.create(request)
        return HttpResponse(body=response, status_code=201)