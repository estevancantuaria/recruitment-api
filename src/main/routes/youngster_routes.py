from fastapi import APIRouter, Depends
from src.application.controllers.youngster_creator_controller import YoungsterCreatorController
from src.main.factories.youngster_factory import make_youngster_creator_controller

router = APIRouter(prefix="/youngsters")

@router.post("/")
async def create_youngster(
    youngster_data: dict,
    controller: YoungsterCreatorController = Depends(make_youngster_creator_controller)
):
    try:
        result = controller.create_youngster(youngster_data)
        return result
    except Exception as e:
        return {"error": str(e)}