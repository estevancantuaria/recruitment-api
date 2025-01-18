from src.models.sqlite.settings.connections import db_connection_handler
from src.models.sqlite.repositories.youngster_repository import YoungsterRepository
from src.controllers.youngster_controllers.youngster_finder_controller import YoungsterFinderController
from src.views.youngster_views.youngster_finder_view import YoungsterFinderView

def youngster_finder_composer():
    connection = db_connection_handler
    repository = YoungsterRepository(connection)
    controller = YoungsterFinderController(repository)
    view = YoungsterFinderView(controller)
    
    return view