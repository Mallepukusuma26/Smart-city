"""
Application Entrypoint.
"""
import os
from app import create_app

env_name = os.getenv("FLASK_ENV", "development")
app = create_app(env_name)

if __name__ == "__main__":
    print("==========================================================================")
    print("   AI-POWERED SMART CITY OPERATIONS & MANAGEMENT PLATFORM (SERVER RUNNING) ")
    print("==========================================================================")
    print("   Citizen Portal : http://127.0.0.1:5000/citizen/dashboard.html")
    print("   Officer Portal : http://127.0.0.1:5000/officer/dashboard.html")
    print("   Admin Portal   : http://127.0.0.1:5000/admin/dashboard.html")
    print("==========================================================================")
    app.run(host="0.0.0.0", port=5000, debug=True)
