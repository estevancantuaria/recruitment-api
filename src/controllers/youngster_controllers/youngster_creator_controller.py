from typing import Dict
from src.controllers.interfaces.youngster_controllers.youngster_creator_controller import IYoungsterCreatorController
from src.models.sqlite.interfaces.youngster_repository import IYoungsterRepository


class YoungsterCreatorController(IYoungsterCreatorController):
    
    def __init__(self, youngster_repository: IYoungsterRepository) -> None:
        self.__youngster_repository = youngster_repository
        
    def create(self, youngster_info: Dict) -> Dict:
        
        nome = youngster_info['nome']
        email = youngster_info['email']
        senha = youngster_info['senha']
        cpf = youngster_info['cpf']
        telefone = youngster_info['telefone']
        ativo = youngster_info['ativo']
        tipo_usuario = youngster_info['tipo_usuario']
        rg = youngster_info['rg']
        data_nascimento = youngster_info['data_nascimento']
        
        self.__youngster_repository.insert_youngster(nome, email, senha, cpf, telefone, ativo, tipo_usuario, rg, data_nascimento)
        formatted_response = self.__format_response(youngster_info)
        
        return formatted_response
        
    def __format_response(self, youngster_info: Dict) -> Dict:
        return {
            "data": {
                "type": "youngster",
                "count": 1,
                "attributes": youngster_info
            }
        }