from fastapi import FastAPI
from src.main.routes.youngster_routes import router as youngster_router
from src.infra.database.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(youngster_router)