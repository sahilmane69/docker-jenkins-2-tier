from flask import Blueprint, jsonify, request

api_bp = Blueprint("api", __name__)

# In-memory store — you'll swap this for a real DB later
_items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
]


@api_bp.route("/status")
def api_status():
    return jsonify({"api": "operational", "items_count": len(_items)})


@api_bp.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": _items})


@api_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in _items if i["id"] == item_id), None)
    if not item:
        # Always return proper HTTP status codes — CI test suites check these
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@api_bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    new_item = {"id": len(_items) + 1, "name": data["name"]}
    _items.append(new_item)
    return jsonify(new_item), 201