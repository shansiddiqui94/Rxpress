import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_bcrypt import Bcrypt
from models import UserAuth, Patient, Pharmacist, Prescription, Basket, db  # Only import db once
from functools import wraps

# Set base directory and database URI
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Create Flask app
app = Flask(__name__)

# Configure Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")  # Secure key
app.json.compact = False  # Optional, depends on your preference

# Initialize SQLAlchemy and migrations
db.init_app(app)
migrate = Migrate(app, db)  # Migration support

# Initialize JWT and Bcrypt
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Role-based decorator to enforce specific role-based actions
def role_required(role):
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user.get('role') != role:
                return jsonify({'error': 'Forbidden: Incorrect role'}), 403
            return func(*args, **kwargs)
        return wrapped
    return wrapper


# User Authentication Routes
@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    # Check that user exists
    user = UserAuth.query.filter_by(username=json_data.get('username')).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Check the user's password
    if not user.check_password(json_data.get('password')):
        return jsonify({'error': 'Incorrect password'}), 401
    
    # Create a JWT token with user information, including the role
    user_info = {
        'id': user.id,
        'username': user.username,
        'role': user.role,
    }
    token = create_access_token(identity=user_info)

    # Return the JWT token to the client
    return jsonify({'access_token': token}), 200


@app.route('/signup', methods=['POST'])
def signup():
    json_data = request.get_json()

    # Check if the username already exists
    existing_user = UserAuth.query.filter_by(username=json_data.get('username')).first()
    if existing_user:
        return jsonify({'error': 'Username already taken'}), 400
    
    # Create a new user with the specified role
    new_user = UserAuth(
        username=json_data.get('username'),
        role=json_data.get('role', 'patient'),  # Default role is 'patient'
    )
    new_user.set_password(json_data.get('password'))

    # Add to the database and commit
    db.session.add(new_user)
    db.session.commit()

    # Return the new user's information
    return jsonify(new_user.to_dict()), 201


@app.route('/check_session', methods=['GET'])
@jwt_required()  # Ensure the user is authenticated
def check_session():
    # Get the current user information from the JWT token
    current_user = get_jwt_identity()

    # If there's no valid user, return unauthorized
    if not current_user:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Return user information, including role
    return jsonify(current_user), 200


# Route for pharmacists to manage prescriptions
@app.route('/pharmacist/prescriptions', methods=['GET'])
@jwt_required()  # User must be authenticated
@role_required('pharmacist')  # User must have the 'pharmacist' role
def pharmacist_prescriptions():
    prescriptions = Prescription.query.all()
    serialized_prescriptions = [
        p.to_dict() for p in prescriptions
    ]
    return jsonify(serialized_prescriptions), 200


# Route for patients to view their prescriptions
@app.route('/patient/prescriptions', methods=['GET'])
@jwt_required()  # User must be authenticated
@role_required('patient')  # User must have the 'patient' role
def patient_prescriptions():
    current_user = get_jwt_identity()
    prescriptions = Prescription.query.filter_by(patient_id=current_user['id']).all()
    serialized_prescriptions = [
        p.to_dict() for p in prescriptions
    ]
    return jsonify(serialized_prescriptions), 200


@app.route('/prescriptions', methods=['GET', 'POST'])
@jwt_required()  # User must be authenticated
def prescriptions():
    if request.method == 'GET':
        try:
            prescriptions = Prescription.query.all()
            serialized_prescriptions = [
                p.to_dict() for p in prescriptions
            ]
            return jsonify(serialized_prescriptions), 200
        
        except ValueError as ve:
            return jsonify({"error": f"Value error: {str(ve)}"}), 400
        
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    elif request.method == 'POST':
        current_user = get_jwt_identity()
        if current_user.get('role') != 'pharmacist':
            return jsonify({'error': 'Forbidden: Only pharmacists can create prescriptions'}), 403
        
        data = request.get_json()
        try:
            new_prescription = Prescription(
                medication_name=data.get("medication_name"),
                dosage=data.get("dosage"),
                instructions=data.get("instructions"),
                pharmacist_id=current_user['id']  # Current pharmacist ID
            )
            db.session.add(new_prescription)
            db.session.commit()
            
            return jsonify(new_prescription.to_dict()), 201
        
        except ValueError as ve:
            return jsonify({"error": f"Value error: {str(ve)}"}), 400
        
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/prescriptions/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt_required()  # User must be authenticated
def prescription_by_id(id):
    if request.method == 'GET':
        try:
            prescription = Prescription.query.get(id)
            if not prescription:
                return jsonify({'error': 'Prescription not found'}), 404
            
            return jsonify(prescription.to_dict()), 200
        
        except ValueError as ve:
            return jsonify({'error': f'Value error: {str(ve)}'}), 400
        
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
    
    elif request.method == 'PATCH':
        current_user = get_jwt_identity()
        if current_user.get('role') != 'pharmacist':
            return jsonify({'error': 'Forbidden: Only pharmacists can update prescriptions'}), 403

        data = request.get_json()
        try:
            prescription = Prescription.query.get(id)
            if not prescription:
                return jsonify({'error': 'Prescription not found'}), 404
            
            # Update prescription details based on input data
            prescription.medication_name = data.get("medication_name", prescription.medication_name)
            prescription.dosage = data.get("dosage", prescription.dosage)
            prescription.instructions = data.get("instructions", prescription.instructions)

            db.session.commit()

            return jsonify(prescription.to_dict()), 200
        
        except ValueError as ve:
            return jsonify({'error': f'Value error: {str(ve)}'}), 400
        
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
    
    elif request.method == 'DELETE':
        current_user = get_jwt_identity()
        if current_user.get('role') != 'pharmacist':
            return jsonify({'error': 'Forbidden: Only pharmacists can delete prescriptions'}), 403

        try:
            prescription = Prescription.query.get(id)
            if not prescription:
                return jsonify({'error': 'Prescription not found'}), 404
            
            db.session.delete(prescription)
            db.session.commit()

            return jsonify({'message': 'Prescription deleted successfully'}), 200
        
        except ValueError as ve:
            return jsonify({'error': f'Value error: {str(ve)}'}), 400
        
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


# Start the Flask server
if __name__ == "__main__":
    app.run(port=5555, debug=True)
