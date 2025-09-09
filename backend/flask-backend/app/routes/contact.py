from flask import Blueprint, request, jsonify

contact_bp = Blueprint('contact', __name__)

@contact_bp.route("/", methods=["POST"])
def handle_contact():
    data = request.get_json()
    name = data.get("full_name")
    email = data.get("email")
    message = data.get("message")

    print(f"Message from {name} ({email}): {message}")

    return jsonify({"message": "Thanks for contacting us!"}), 200
