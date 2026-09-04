"""
Authentication and User Registration Service.
"""
from datetime import datetime
from ..models import db, User, Role, UserRole, Citizen, Officer, Department
from ..security.password import hash_password, verify_password, validate_password_strength
from ..security.tokens import generate_access_token
from ..config.constants import Roles

class AuthService:
    @staticmethod
    def register_citizen(username, email, password, full_name, phone_number=None, address=None, city_zone="Central Zone", emergency_contact=None, occupation=None):
        # 1. Check existing
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return False, "Username or Email already registered.", None

        # 2. Validate password strength
        valid, msg = validate_password_strength(password)
        if not valid:
            return False, msg, None

        # 3. Create User
        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            city_zone=city_zone,
            is_active=True,
            is_verified=True,
        )
        db.session.add(user)
        db.session.flush()

        # 4. Assign CITIZEN Role
        citizen_role = Role.query.filter_by(name=Roles.CITIZEN).first()
        if citizen_role:
            ur = UserRole(user_id=user.id, role_id=citizen_role.id)
            db.session.add(ur)

        # 5. Create Citizen Profile
        card_id = f"CTZ-{user.id:06d}"
        citizen_profile = Citizen(
            user_id=user.id,
            citizen_card_id=card_id,
            emergency_contact=emergency_contact,
            occupation=occupation,
        )
        db.session.add(citizen_profile)
        db.session.commit()

        token = generate_access_token(user.id, user.username, user.roles)
        return True, "Citizen registration successful.", {"user": user.to_dict(include_profile=True), "token": token}

    @staticmethod
    def register_officer(username, email, password, full_name, badge_number, designation, department_id=None, phone_number=None, assigned_zone="Central Zone"):
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return False, "Username or Email already registered.", None

        if Officer.query.filter_by(badge_number=badge_number).first():
            return False, "Badge number already exists.", None

        valid, msg = validate_password_strength(password)
        if not valid:
            return False, msg, None

        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            full_name=full_name,
            phone_number=phone_number,
            city_zone=assigned_zone,
            is_active=True,
            is_verified=True,
        )
        db.session.add(user)
        db.session.flush()

        officer_role = Role.query.filter_by(name=Roles.OFFICER).first()
        if officer_role:
            ur = UserRole(user_id=user.id, role_id=officer_role.id)
            db.session.add(ur)

        officer_profile = Officer(
            user_id=user.id,
            department_id=department_id,
            badge_number=badge_number,
            designation=designation,
            assigned_zone=assigned_zone,
        )
        db.session.add(officer_profile)
        db.session.commit()

        token = generate_access_token(user.id, user.username, user.roles)
        return True, "Officer registration successful.", {"user": user.to_dict(include_profile=True), "token": token}

    @staticmethod
    def authenticate_user(login_identifier, password):
        """Authenticate user by username or email, return user dict and JWT token."""
        user = User.query.filter((User.username == login_identifier) | (User.email == login_identifier)).first()
        if not user or not user.check_password(password):
            return False, "Invalid credentials.", None

        if not user.is_active:
            return False, "Account disabled. Please contact administrator.", None

        user.last_login = datetime.utcnow()
        db.session.commit()

        token = generate_access_token(user.id, user.username, user.roles)
        
        # Determine redirect path based on role
        redirect_path = "/citizen/dashboard"
        if user.is_admin():
            redirect_path = "/admin/dashboard"
        elif user.is_officer():
            redirect_path = "/officer/dashboard"

        return True, "Login successful.", {
            "token": token,
            "redirect_url": redirect_path,
            "user": user.to_dict(include_profile=True)
        }
