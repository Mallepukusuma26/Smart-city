"""
Flask Application Factory for Smart City Operations Platform.
"""
import os
from flask import Flask, send_from_directory, redirect, jsonify, session
from flask_cors import CORS

from .config import config_by_name, setup_logging
from .models import db
from .middleware import init_auth_middleware, init_audit_middleware, init_rate_limiter, init_error_handlers
from .routes import auth_bp, citizen_bp, officer_bp, admin_bp, service_bp, EXPANDED_BLUEPRINTS

def create_app(config_name="default"):
    app = Flask(__name__, static_folder=None, template_folder=None)
    
    # 1. Load Configuration
    config_obj = config_by_name.get(config_name, config_by_name["default"])
    app.config.from_object(config_obj)
    
    # 2. Setup Logging
    setup_logging(app, app.config.get("LOG_LEVEL", "INFO"))
    
    # 3. Enable CORS
    CORS(app, supports_credentials=True)
    
    # 4. Initialize Database
    db.init_app(app)
    
    # 5. Initialize Middlewares & Error Handlers
    init_auth_middleware(app)
    init_audit_middleware(app)
    init_rate_limiter(app)
    init_error_handlers(app)
    
    # 6. Register API Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(citizen_bp)
    app.register_blueprint(officer_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(service_bp)
    for bp in EXPANDED_BLUEPRINTS:
        app.register_blueprint(bp)

    
    # 7. Serve Static Frontend Files & Portals
    frontend_dir = os.path.join(app.root_path, "..", "..", "frontend")

    @app.route("/")
    def index():
        return redirect("/auth/login")

    @app.route("/auth/<path:filename>")
    def serve_auth(filename):
        return send_from_directory(os.path.join(frontend_dir, "auth"), filename)

    @app.route("/citizen/<path:filename>")
    def serve_citizen(filename):
        return send_from_directory(os.path.join(frontend_dir, "citizen"), filename)

    @app.route("/officer/<path:filename>")
    def serve_officer(filename):
        return send_from_directory(os.path.join(frontend_dir, "officer"), filename)

    @app.route("/admin/<path:filename>")
    def serve_admin(filename):
        return send_from_directory(os.path.join(frontend_dir, "admin"), filename)

    @app.route("/css/<path:filename>")
    def serve_css(filename):
        return send_from_directory(os.path.join(frontend_dir, "css"), filename)

    @app.route("/js/<path:filename>")
    def serve_js(filename):
        return send_from_directory(os.path.join(frontend_dir, "js"), filename)

    @app.route("/assets/<path:filename>")
    def serve_assets(filename):
        return send_from_directory(os.path.join(frontend_dir, "assets"), filename)

    # Root health check endpoint
    @app.route("/api/health", methods=["GET"])
    def api_health():
        return jsonify({
            "status": "UP",
            "system": "AI-Powered Smart City Operations Platform",
            "version": "1.0.0",
            "database": "CONNECTED"
        }), 200

    with app.app_context():
        db.create_all()

    return app
