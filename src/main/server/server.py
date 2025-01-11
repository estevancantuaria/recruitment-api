from flask import Flask
from src.models.sqlite.settings.connections import db_connection_handler

from src.main.routes.youngster_router import youngster_routes_bp

db_connection_handler

app = Flask(__name__)
app.register_blueprint(youngster_routes_bp)

if __name__ == "__main__":
    app.run(debug=True)