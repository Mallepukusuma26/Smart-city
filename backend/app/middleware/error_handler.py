"""
Global Exception Handlers and Error Responses.
"""
from flask import jsonify, request, render_template

def init_error_handlers(app):
    @app.errorhandler(400)
    def bad_request_error(e):
        if request.is_json or request.path.startswith("/api/"):
            return jsonify({"error": "Bad Request. Invalid parameters or syntax.", "code": 400}), 400
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(401)
    def unauthorized_error(e):
        if request.is_json or request.path.startswith("/api/"):
            return jsonify({"error": "Unauthorized. Authentication credentials missing or invalid.", "code": 401}), 401
        return jsonify({"error": "Unauthorized"}), 401

    @app.errorhandler(403)
    def forbidden_error(e):
        if request.is_json or request.path.startswith("/api/"):
            return jsonify({"error": "Forbidden. You do not have permission to access this resource.", "code": 403}), 403
        return jsonify({"error": "Forbidden"}), 403

    @app.errorhandler(404)
    def not_found_error(e):
        if request.is_json or request.path.startswith("/api/"):
            return jsonify({"error": "Resource Not Found.", "code": 404}), 404
        return jsonify({"error": "Page Not Found"}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        if request.is_json or request.path.startswith("/api/"):
            return jsonify({"error": "Internal Server Error. Please contact system administrator.", "code": 500}), 500
        return jsonify({"error": "Internal Server Error"}), 500
