from src.views.interfaces.view_interface import ViewInterface
from src.controllers.youngster_controllers.youngster_finder_controller import YoungsterFinderController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class YoungsterFinderView(ViewInterface):
    def __init__(self, controller: YoungsterFinderController):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body
        response = self.__controller.find_by_id(request["id"])
        return HttpResponse(body=response, status_code=200)