from src.domain.usecases.interfaces.create_youngster_usecase import ICreateYoungsterUsecase
from src.application.dtos.youngster.youngster_dtos import YoungsterInputDTO

class YoungsterCreatorController:
    def __init__(self, create_youngster_usecase: ICreateYoungsterUsecase):
        self.__create_youngster_usecase = create_youngster_usecase

    def create_youngster(self, youngster_info: dict) -> dict:
        youngster_info = YoungsterInputDTO(**youngster_info)
        
        result = self.__create_youngster_usecase.create_youngster(youngster_info)
        
        return self.__format_response(result)
    
    def __format_response(self, result: dict) -> dict:
        return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": result
            }
        }