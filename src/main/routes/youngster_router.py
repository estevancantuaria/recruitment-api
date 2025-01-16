from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.youngster_creator_composer import create_youngster_composer

from src.errors.error_handle import handle_errors

youngster_routes_bp = Blueprint("youngster_routes", __name__)

@youngster_routes_bp.route("/youngster", methods=["POST"])
def create_youngster():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = create_youngster_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code
