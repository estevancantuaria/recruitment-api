from src.models.sqlite.settings.connections import db_connection_handler
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository
from src.controllers.youngster_controllers.youngster_creator_controller import YoungsterCreatorController
from src.views.youngster_views.youngster_creator_view import YoungsterCreatorView

def create_youngster_composer():
    connection = db_connection_handler
    respository = YoungsterRepository(connection)
    controller = YoungsterCreatorController(respository)
    view = YoungsterCreatorView(controller)
    
    return view