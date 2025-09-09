from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes.contact import contact_bp
    from .routes.projects import projects_bp

    app.register_blueprint(contact_bp, url_prefix="/api/contact")
    app.register_blueprint(projects_bp, url_prefix="/api/projects")

    return app
