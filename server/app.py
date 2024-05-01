import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Patient, Prescription, Basket, db

# Set base directory and database URI
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Create Flask app
app = Flask(__name__)

# Configure Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")  # Secure key
app.json.compact = False  # Optional setting to make JSON output more readable

# Initialize SQLAlchemy, migrations, JWT, and Bcrypt
db.init_app(app)
migrate = Migrate(app, db)



# User Authentication Routes
# @app.route('/login', methods=['POST'])
# def login():
#     json_data = request.get_json()
#     user = UserAuth.query.filter_by(username=json_data.get('username')).first()

#     if not user:
#         return jsonify({'error': 'User not found'}), 404
    
#     if not user.check_password(json_data.get('password')):
#         return jsonify({'error': 'Incorrect password'}), 401
    
#     user_info = {
#         'id': user.id,
#         'username': user.username,
#         'role': user.role,
#     }
#     token = create_access_token(identity=user_info)
#     return jsonify({'access_token': token}), 200


# @app.route('/login', methods=['POST'])
# def login():
#     json_data = request.get_json()
#     username = json_data.get('username')
#     password = json_data.get('password')

#     user = UserAuth.query.filter_by(username=username).first()

#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     # Check if the password is correct
#     if not user.check_password(password):
#         return jsonify({'error': 'Incorrect password'}), 401
    
#     token = create_access_token(identity={'id': user.id, 'username': user.username, 'role': user.role})

#     return jsonify({'access_token': token}), 200



# @app.route('/signup', methods=['POST'])
# def signup():
#     json_data = request.get_json()
#     existing_user = UserAuth.query.filter_by(username=json_data.get('username')).first()

#     if existing_user:
#         return jsonify({'error': 'Username already taken'}), 400
    
#     new_user = UserAuth(
#         username=json_data.get('username'),
#         role=json_data.get('role', 'patient'),  # Default role is 'patient'
#     )
#     new_user.set_password(json_data.get('password'))

#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user.to_dict()), 201


# @app.route('/check_session', methods=['GET'])
# @jwt_required()
# def check_session():
#     current_user = get_jwt_identity()

#     if not current_user:
#         return jsonify({'error': 'Unauthorized'}), 401
    
#     return jsonify(current_user), 200


# # Pharmacist Routes
# @app.route('/pharmacist/prescriptions', methods=['GET'])
# @jwt_required()
# @role_required('pharmacist')
# def pharmacist_prescriptions():
#     prescriptions = Prescription.query.all()
#     serialized_prescriptions = [p.to_dict() for p in prescriptions]
#     return jsonify(serialized_prescriptions), 200


# @app.route('/pharmacist/patients', methods=['GET'])
# @jwt_required()
# @role_required('pharmacist')
# def pharmacist_patients():
#     patients = Patient.query.all()  # Modify if pharmacists should only see their own patients
#     serialized_patients = [p.to_dict() for p in patients]
#     return jsonify(serialized_patients), 200



#Routes by Drugs 

#Get all Drugs

#Get all Drugs by ID

#Post new Drugs 

#Delete Drugs by id





# Patient Routes 
# Patient by ID
@app.route('/patient/<int:id>', methods=['GET'])
def patient_byID(id):
    pt = Patient.query.get(id)

    if not pt:
        return jsonify({'error': 'Prescription not found'}), 404
    
    return jsonify(pt.to_dict()), 200

# Patient Routes
@app.route('/patient/prescriptions', methods=['GET'])
def patient_prescriptions():
    # Without jwt_required, you need another way to determine the current user
    # Simplified: returns all prescriptions (adjust logic as needed)
    prescriptions = Prescription.query.all()
    serialized_prescriptions = [p.to_dict() for p in prescriptions]
    return jsonify(serialized_prescriptions), 200


@app.route('/patient/info', methods=['GET', 'PATCH'])
def patient_info():
    # Without authentication, you might need to find another way to get the current patient
    # Simplified: fetches the first patient (modify logic as required)
    patient = Patient.query.first()  # Simplified logic
    
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    
    if request.method == 'GET':
        return jsonify(patient.to_dict()), 200
    
    elif request.method == 'PATCH':
        data = request.get_json()
        patient.name = data.get("name", patient.name)
        patient.address = data.get("address", patient.address)
        patient.insurance = data.get("insurance", patient.insurance)
        db.session.commit()
        
        return jsonify(patient.to_dict()), 200


# Prescription Routes
@app.route('/prescriptions', methods=['GET', 'POST'])
def prescriptions():
    if request.method == 'GET':
        try:
            prescriptions = Prescription.query.all()  # No filtering by user
            serialized_prescriptions = [p.to_dict() for p in prescriptions]
            return jsonify(serialized_prescriptions), 200
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    
    elif request.method == 'POST':
        data = request.get_json()
        
        try:
            new_prescription = Prescription(
                medication_name=data.get("medication_name"),
                dosage=data.get("dosage"),
                instructions=data.get("instructions"),
                pharmacist_id=data.get("pharmacist_id"),  # You might need to adjust this
            )
            db.session.add(new_prescription)
            db.session.commit()
            
            return jsonify(new_prescription.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/prescriptions/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def prescription_by_id(id):
    if request.method == 'GET':
        prescription = Prescription.query.get(id)
        
        if not prescription:
            return jsonify({'error': 'Prescription not found'}), 404
        
        return jsonify(prescription.to_dict()), 200
    
    elif request.method == 'PATCH':
        data = request.get_json()
        
        try:
            prescription = Prescription.query.get(id)
            prescription.medication_name = data.get("medication_name", prescription.medication_name)
            prescription.dosage = data.get("dosage", prescription.dosage)
            prescription.instructions = data.get("instructions", prescription.instructions)
            
            db.session.commit()
            
            return jsonify(prescription.to_dict()), 200
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
    
    elif request.method == 'DELETE':
        prescription = Prescription.query.get(id)
        
        if not prescription:
            return jsonify({'error': 'Prescription not found'}), 404
        
        db.session.delete(prescription)
        db.session.commit()
        
        return jsonify({'message': 'Prescription deleted successfully'}), 200
    
 #updating Rx status 
@app.route('/prescriptions/update_status', methods=['PATCH'])
def update_prescription_status():
    # Get medication_name and status from the request JSON
    data = request.get_json()
    medication_name = data.get("medication_name")
    new_status = data.get("status")

    if not medication_name or not new_status:
        return jsonify({"error": "Medication name and status are required"}), 400

    # Find the prescription by medication name
    prescription = Prescription.query.filter_by(medication_name=medication_name).first()

    if not prescription:
        return jsonify({"error": f"Prescription with medication name '{medication_name}' not found"}), 404
    
    # Update the prescription's status
    prescription.status = new_status
    
    # Commit the changes to the database
    db.session.commit()
    
    return jsonify(prescription.to_dict()), 200



# Basket Routes
@app.route('/basket', methods=['POST', 'GET'])
def basket():
    if request.method == 'GET':
        basket_items = Basket.query.all()  # You might want to adjust this to fetch by patient ID
        serialized_items = [item.to_dict() for item in basket_items]
        return jsonify(serialized_items), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        try:
            new_basket_item = Basket(
                patient_id=data.get("patient_id"),
                prescription_id=data.get("prescription_id"),
                quantity=data.get("quantity", 1),  # Default quantity
            )
            db.session.add(new_basket_item)
            db.session.commit()
            
            return jsonify(new_basket_item.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/basket/<int:id>', methods=['DELETE', 'PATCH'])
def basket_by_id(id):
    if request.method == 'DELETE':
        basket_item = Basket.query.get(id)
        
        if not basket_item:
            return jsonify({'error': 'Basket item not found'}), 404
        
        db.session.delete(basket_item)
        db.session.commit()
        
        return jsonify({'message': 'Basket item removed successfully'}), 200
    
    elif request.method == 'PATCH':
        data = request.get_json()
        
        try:
            basket_item = Basket.query.get(id)
            basket_item.status = data.get("status", basket_item.status)
            basket_item.quantity = data.get("quantity", basket_item.quantity)
            
            db.session.commit()
            
            return jsonify(basket_item.to_dict()), 200
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500



# Start the Flask server
if __name__ == "__main__":
    app.run(port=5555, debug=True)
