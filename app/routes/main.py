from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return jsonify({
        "message": "Flask DevOps App is running!",
        "endpoints": {
            "health": "/health",
            "readiness": "/ready",
            "api_items": "/api/items",
            "api_status": "/api/status"
        }
    })
