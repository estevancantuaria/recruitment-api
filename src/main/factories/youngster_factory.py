from src.application.controllers.youngster_creator_controller import YoungsterCreatorController
from src.domain.usecases.create_youngster_usecase import CreateYoungsterUsecase
from src.infra.repositories.youngster_repository import YoungsterRepository
from src.infra.database.connection import db_connection_handler

def make_youngster_creator_controller() -> YoungsterCreatorController:
    # Instancia o repositório
    youngster_repository = YoungsterRepository(db_connection_handler)
    
    # Cria o caso de uso injetando o repositório
    create_youngster_usecase = CreateYoungsterUsecase(youngster_repository)
    
    # Cria o controller injetando o caso de uso
    controller = YoungsterCreatorController(create_youngster_usecase)
    
    return controller