"""
Automated System Health Checker & Code Integrity Verification.
Checks Python syntax, import errors, database startup, route registration, and static assets.
"""
import os
import sys

# Ensure backend path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend"))

def run_health_check():
    print("==========================================================================")
    print("               SMART CITY PLATFORM — SYSTEM HEALTH CHECK                  ")
    print("==========================================================================")
    
    passed_checks = 0
    failed_checks = 0

    def check(name, fn):
        nonlocal passed_checks, failed_checks
        try:
            print(f"[{'CHECKING':^10}] {name}...", end=" ")
            fn()
            print("[\033[92mPASSED\033[0m]")
            passed_checks += 1
        except Exception as e:
            print(f"[\033[91mFAILED\033[0m] -> {e}")
            failed_checks += 1

    # 1. Test Imports & Config
    def test_imports():
        from app.config import Config, Roles, DepartmentNames
        from app.security import hash_password, verify_password, generate_access_token
        assert Config.SECRET_KEY is not None

    check("Module Imports & Settings Configuration", test_imports)

    # 2. Test Flask Application Factory & Route Registration
    def test_app_factory():
        from app import create_app
        app = create_app("testing")
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        assert "/api/auth/login" in routes
        assert "/api/citizen/dashboard" in routes
        assert "/api/officer/dashboard" in routes
        assert "/api/admin/dashboard" in routes
        assert "/api/services/traffic/overview" in routes

    check("Flask App Factory & REST API Route Registration", test_app_factory)

    # 3. Test Database Connection & Models
    def test_database():
        from app import create_app
        from app.models import db, User, Role, Department, Complaint, TrafficRecord
        app = create_app("testing")
        with app.app_context():
            db.create_all()
            user_count = User.query.count()
            assert user_count >= 0

    check("SQLite Database Connection & ORM Schema Creation", test_database)

    # 4. Test ML Model Loading & Prediction Engine
    def test_ml_models():
        from app.ml.pipelines import MLInferenceEngine
        res = MLInferenceEngine.predict_traffic(400, 35.0, 1)
        assert "predicted_congestion_index" in res

    check("Local AI/ML Model Artifact Loading & Inference", test_ml_models)

    # 5. Check Static Frontend File Integrity
    def test_frontend_files():
        root = os.path.dirname(os.path.dirname(__file__))
        required_views = [
            "frontend/auth/login.html",
            "frontend/auth/register.html",
            "frontend/citizen/dashboard.html",
            "frontend/citizen/complaints.html",
            "frontend/officer/dashboard.html",
            "frontend/admin/dashboard.html",
            "frontend/admin/ai.html",
            "frontend/css/main.css",
            "frontend/js/api.js",
            "frontend/js/auth.js",
        ]
        for v in required_views:
            path = os.path.join(root, v)
            assert os.path.exists(path), f"Missing required file: {v}"

    check("Frontend Templates & Static Assets Verification", test_frontend_files)

    print("==========================================================================")
    print(f"Health Check Summary: {passed_checks} PASSED, {failed_checks} FAILED")
    print("==========================================================================")
    return failed_checks == 0

if __name__ == "__main__":
    success = run_health_check()
    sys.exit(0 if success else 1)
