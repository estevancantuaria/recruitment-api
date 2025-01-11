import pytest
from src.controllers.youngster_controllers.youngster_deleter_controller import YoungsterDeleterController

def test_delete_youngster(mocker):
    mocked_youngster_repository = mocker.Mock()
    youngster_deleter_controller = YoungsterDeleterController(mocked_youngster_repository)
    youngster_deleter_controller.delete_youngster(1)
    
    mocked_youngster_repository.delete_youngster.assert_called_once_with(1)
