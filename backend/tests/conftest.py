"""
Pytest Test Fixtures and Application Harness.
"""
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app

from app.models import db, User, Role, UserRole, Citizen, Officer, Department
from app.security.password import hash_password
from app.config.constants import Roles, DepartmentNames

@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        
        # Create Roles
        c_role = Role(name=Roles.CITIZEN)
        o_role = Role(name=Roles.OFFICER)
        a_role = Role(name=Roles.ADMIN)
        db.session.add_all([c_role, o_role, a_role])
        db.session.flush()

        # Create Dept
        dept = Department(name=DepartmentNames.TRAFFIC, code="TRF")
        db.session.add(dept)
        db.session.flush()

        # Create Citizen User
        cit = User(username="test_citizen", email="cit@test.com", password_hash=hash_password("Pass123!"), full_name="Test Citizen")
        db.session.add(cit)
        db.session.flush()
        db.session.add(UserRole(user_id=cit.id, role_id=c_role.id))

        # Create Officer User
        off = User(username="test_officer", email="off@test.com", password_hash=hash_password("Pass123!"), full_name="Test Officer")
        db.session.add(off)
        db.session.flush()
        db.session.add(UserRole(user_id=off.id, role_id=o_role.id))
        db.session.add(Officer(user_id=off.id, department_id=dept.id, badge_number="TEST-001", designation="Inspector"))

        # Create Admin User
        adm = User(username="test_admin", email="adm@test.com", password_hash=hash_password("Pass123!"), full_name="Test Admin")
        db.session.add(adm)
        db.session.flush()
        db.session.add(UserRole(user_id=adm.id, role_id=a_role.id))

        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
