from src.controllers.interfaces.youngster_controllers.youngster_update_controller import IYoungsterUpdateController
from src.models.sqlite.repositories.youngster_repository import IYoungsterRepository

class YoungsterUpdateController(IYoungsterUpdateController):
    def __init__(self, repository: IYoungsterRepository) -> None:
        self.__repository = repository
        
    def update_youngster(self, update_data: dict) -> None:
        response = self.__repository.update_youngster(update_data)
        formated_response = self.__format_response(response)
        return formated_response
        
    def __format_response(self, jovem: dict) -> dict:
        return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": jovem
            }
        }
