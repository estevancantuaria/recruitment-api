from src.domain.usecases.interfaces.create_youngster_usecase import ICreateYoungsterUsecase
from src.infra.repositories.interfaces.youngster_repository import IYoungsterRepository

class CreateYoungsterUsecase(ICreateYoungsterUsecase):
    def __init__(self, youngster_repository: IYoungsterRepository):
        self.__youngster_repository = youngster_repository

    def create_youngster(self, youngster_info: dict) -> dict:
        name = youngster_info['name']
        email = youngster_info['email']
        cpf = youngster_info['cpf']
        birth_date = youngster_info['birth_date']
        cellphone = youngster_info['cellphone']
        password = youngster_info['password']
        rg = youngster_info['rg']
        
        self.__youngster_repository.create_youngster(name, email, cpf, birth_date, cellphone, password, rg)
        
        return youngster_info