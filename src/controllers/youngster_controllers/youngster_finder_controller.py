from src.controllers.interfaces.youngster_controllers.youngster_finder_controller import IYoungsterFinderController
from src.models.sqlite.repositories.youngster_repository import IYoungsterRepository
from src.models.sqlite.entities.users import Jovem

class YoungsterFinderController(IYoungsterFinderController):
    def __init__(self, youngster_repository: IYoungsterRepository):
        self.__youngster_repository = youngster_repository
        
    def find_by_id(self, id: int) -> Jovem:
        response = self.__youngster_repository.get_youngster_by_id(id)
        formated_response = self.__format_response(response)
        return formated_response
    
    def __format_response(self, jovem: Jovem) -> dict:
        return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": {
                    "id": jovem.id,
                    "nome": jovem.nome,
                    "email": jovem.email,
                    "senha": jovem.senha,
                    "cpf": jovem.cpf,
                    "telefone": jovem.telefone,
                    "ativo": jovem.ativo,
                    "tipo_usuario": jovem.tipo_usuario,
                    "rg": jovem.rg,
                    "data_nascimento": jovem.data_nascimento
                }
            }
        }