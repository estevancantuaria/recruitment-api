from datetime import date
from src.domain.usecases.create_youngster_usecase import CreateYoungsterUsecase

class MockYoungsterRepository:
    def create_youngster(self, name: str, email: str, cpf: str, birth_date: date, cellphone: str, password: str, rg: str) -> None:
        pass
    
def test_create_youngster_usecase():
    youngster_repository = MockYoungsterRepository()
    create_youngster_usecase = CreateYoungsterUsecase(youngster_repository)
    
    youngster_info = {'name': 'John Doe', 'email': 'john.doe@example.com', 'cpf': '12345678900', 'birth_date': date(1990, 1, 1), 'cellphone': '1234567890', 'password': 'password', 'rg': '1234567890'}
    result = create_youngster_usecase.create_youngster(youngster_info)