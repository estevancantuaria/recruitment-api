from src.controllers.interfaces.youngster_controllers.youngster_deleter_controller import IYoungsterDeleterController
from src.models.sqlite.repositories.youngster_repository import IYoungsterRepository

class YoungsterDeleterController(IYoungsterDeleterController):
    def __init__(self, youngster_repository: IYoungsterRepository):
        self.__youngster_repository = youngster_repository
        
    def delete_youngster(self, id: int) -> None:
        self.__youngster_repository.delete_youngster(id)
        return None