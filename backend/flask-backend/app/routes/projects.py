from flask import Blueprint, jsonify
from app.data.projects import PROJECTS

projects_bp = Blueprint('projects', __name__)

@projects_bp.route("/", methods=["GET"])
def get_projects():
    return jsonify(PROJECTS)
