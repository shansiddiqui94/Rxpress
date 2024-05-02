# import os
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from models import Patient, Prescription, Basket, Drug, db

# # Set base directory and database URI
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# # Create Flask app
# app = Flask(__name__)

# # Configure Flask app
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")  # Secure key
# app.json.compact = False  # Optional setting to make JSON output more readable

# # Initialize SQLAlchemy, migrations, JWT, and Bcrypt
# db.init_app(app)
# migrate = Migrate(app, db)




# #Routes by Drugs 


# #GET all Drugs/POST new drugs
# @app.route('/drugs', methods=['GET', 'POST'])  # Fix the typo in "methods"
# def drugs():
#     if request.method == 'GET':
#         try:
#             drugs = Drug.query.all()  # Retrieve all drugs
#             all_drugs = [drug.to_dict() for drug in drugs]  # Serialize the results
#             return jsonify(all_drugs), 200  # Return the list as JSON
#         except Exception as e:
#             # Handle unexpected errors
#             return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

#     elif request.method == 'POST':
#         # Extract JSON data from the request body
#         data = request.get_json()
#         if not data:
#             return jsonify({"error": "No JSON data provided"}), 400

#         try:
#             # Validate required fields
#             if 'ndc_id' not in data or 'name' not in data:
#                 return jsonify({"error": "Fields 'ndc_id' and 'name' are required"}), 400

#             # Create a new Drug instance with the provided data
#             new_drug = Drug(
#                 ndc_id=data['ndc_id'],
#                 name=data['name'],
#                 description=data.get('description', ''),  # Optional field
#                 dosage_form=data.get('dosage_form', ''),  # Optional field
#                 strength=data.get('strength', '')  # Optional field
#             )

#             # Add and commit the new record to the database
#             db.session.add(new_drug)
#             db.session.commit()

#             return jsonify(new_drug.to_dict()), 201  # Return the created drug and HTTP status 201
#         except Exception as e:
#             # Handle unexpected errors
#             db.session.rollback()  # Roll back in case of error
#             return jsonify({"error": f"An error occurred while creating the drug: {str(e)}"}), 500


# #Get all Drugs by NDC_ID(national Drug Code)
# @app.route('/drugs/ndc/<ndc_id>', methods=['GET'])
# def get_drugs_by_ndc(ndc_id):
#     try:
#         # Query all drugs with the given NDC_ID
#         drugs = Drug.query.filter_by(ndc_id=ndc_id).all()

#         if not drugs:
#             # If no drugs are found with the given NDC_ID, return a 404 Not Found
#             return jsonify({"error": f"No drugs found with NDC_ID {ndc_id}"}), 404
        
#         # Serialize the result to JSON
#         all_drugs = [drug.to_dict() for drug in drugs]
#         return jsonify(all_drugs), 200  # Return the list as JSON with a 200 OK status

#     except Exception as e:
#         # Handle unexpected errors
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500



# #Delete Drugs by id

# def delete_drug(drug_id):
#     try:
#         # Retrieve the drug by ID
#         drug = Drug.query.get(drug_id)

#         if not drug:
#             # If no drug is found with the given ID, return a 404 error
#             return jsonify({"error": f"Drug with ID {drug_id} not found"}), 404
        
#         # Delete the drug from the database
#         db.session.delete(drug)
#         db.session.commit()  # Commit the deletion
        
#         return jsonify({"message": f"Drug with ID {drug_id} deleted successfully"}), 200

#     except Exception as e:
#         # Rollback in case of error
#         db.session.rollback()
#         return jsonify({"error": f"An error occurred while deleting the drug: {str(e)}"}), 500



# # Patient Routes

# # Patient by ID
# @app.route('/patient/<int:id>', methods=['GET'])
# def patient_byID(id):
#     pt = Patient.query.get(id)

#     if not pt:
#         return jsonify({'error': 'Prescription not found'}), 404
    
#     return jsonify(pt.to_dict()), 200

# # Patient/rx
# @app.route('/patient/prescriptions', methods=['GET'])
# def patient_prescriptions():
#     # Without jwt_required, you need another way to determine the current user
#     # Simplified: returns all prescriptions (adjust logic as needed)
#     prescriptions = Prescription.query.all()
#     serialized_prescriptions = [p.to_dict() for p in prescriptions]
#     return jsonify(serialized_prescriptions), 200


# @app.route('/patient/info', methods=['GET', 'PATCH'])
# def patient_info():
#     # Without authentication, you might need to find another way to get the current patient
#     # Simplified: fetches the first patient (modify logic as required)
#     patient = Patient.query.first()  # Simplified logic
    
#     if not patient:
#         return jsonify({'error': 'Patient not found'}), 404
    
#     if request.method == 'GET':
#         return jsonify(patient.to_dict()), 200
    
#     elif request.method == 'PATCH':
#         data = request.get_json()
#         patient.name = data.get("name", patient.name)
#         patient.address = data.get("address", patient.address)
#         patient.insurance = data.get("insurance", patient.insurance)
#         db.session.commit()
        
#         return jsonify(patient.to_dict()), 200


# # Prescription Routes
# @app.route('/prescriptions', methods=['GET', 'POST'])
# def prescriptions():
#     if request.method == 'GET':
#         try:
#             prescriptions = Prescription.query.all()  # No filtering by user
#             serialized_prescriptions = [p.to_dict() for p in prescriptions]
#             return jsonify(serialized_prescriptions), 200
#         except ValueError as e:
#             return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    
#     elif request.method == 'POST':
#         data = request.get_json()
        
#         try:
#             new_prescription = Prescription(
#                 medication_name=data.get("medication_name"),
#                 dosage=data.get("dosage"),
#                 instructions=data.get("instructions"),
#                 pharmacist_id=data.get("pharmacist_id"),  # You might need to adjust this
#             )
#             db.session.add(new_prescription)
#             db.session.commit()
            
#             return jsonify(new_prescription.to_dict()), 201
#         except Exception as e:
#             return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# @app.route('/prescriptions/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
# def prescription_by_id(id):
#     if request.method == 'GET':
#         prescription = Prescription.query.get(id)
        
#         if not prescription:
#             return jsonify({'error': 'Prescription not found'}), 404
        
#         return jsonify(prescription.to_dict()), 200
    
#     elif request.method == 'PATCH':
#         data = request.get_json()
        
#         try:
#             prescription = Prescription.query.get(id)
#             prescription.medication_name = data.get("medication_name", prescription.medication_name)
#             prescription.dosage = data.get("dosage", prescription.dosage)
#             prescription.instructions = data.get("instructions", prescription.instructions)
            
#             db.session.commit()
            
#             return jsonify(prescription.to_dict()), 200
#         except Exception as e:
#             return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
    
#     elif request.method == 'DELETE':
#         prescription = Prescription.query.get(id)
        
#         if not prescription:
#             return jsonify({'error': 'Prescription not found'}), 404
        
#         db.session.delete(prescription)
#         db.session.commit()
        
#         return jsonify({'message': 'Prescription deleted successfully'}), 200
    
#  #updating Rx status 
# @app.route('/prescriptions/update_status', methods=['PATCH'])
# def update_prescription_status():
#     # Get medication_name and status from the request JSON
#     data = request.get_json()
#     medication_name = data.get("medication_name")
#     new_status = data.get("status")

#     if not medication_name or not new_status:
#         return jsonify({"error": "Medication name and status are required"}), 400

#     # Find the prescription by medication name
#     prescription = Prescription.query.filter_by(medication_name=medication_name).first()

#     if not prescription:
#         return jsonify({"error": f"Prescription with medication name '{medication_name}' not found"}), 404
    
#     # Update the prescription's status
#     prescription.status = new_status
    
#     # Commit the changes to the database
#     db.session.commit()
    
#     return jsonify(prescription.to_dict()), 200



# # Basket Routes
# @app.route('/basket', methods=['POST', 'GET'])
# def basket():
#     if request.method == 'GET':
#         basket_items = Basket.query.all()  # You might want to adjust this to fetch by patient ID
#         serialized_items = [item.to_dict() for item in basket_items]
#         return jsonify(serialized_items), 200
    
#     elif request.method == 'POST':
#         data = request.get_json()
        
#         try:
#             new_basket_item = Basket(
#                 patient_id=data.get("patient_id"),
#                 prescription_id=data.get("prescription_id"),
#                 quantity=data.get("quantity", 1),  # Default quantity
#             )
#             db.session.add(new_basket_item)
#             db.session.commit()
            
#             return jsonify(new_basket_item.to_dict()), 201
#         except Exception as e:
#             return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# @app.route('/basket/<int:id>', methods=['DELETE', 'PATCH'])
# def basket_by_id(id):
#     if request.method == 'DELETE':
#         basket_item = Basket.query.get(id)
        
#         if not basket_item:
#             return jsonify({'error': 'Basket item not found'}), 404
        
#         db.session.delete(basket_item)
#         db.session.commit()
        
#         return jsonify({'message': 'Basket item removed successfully'}), 200
    
#     elif request.method == 'PATCH':
#         data = request.get_json()
        
#         try:
#             basket_item = Basket.query.get(id)
#             basket_item.status = data.get("status", basket_item.status)
#             basket_item.quantity = data.get("quantity", basket_item.quantity)
            
#             db.session.commit()
            
#             return jsonify(basket_item.to_dict()), 200
#         except Exception as e:
#             return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500



# # Start the Flask server
# if __name__ == "__main__":
#     app.run(port=5555, debug=True)



# Second Routes versions: 






import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError  
from flask_migrate import Migrate
from flask_cors import CORS
from models import Patient, Prescription, Drug, Pharmacist, Basket, db

# Set base directory and database URI
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Create Flask app
app = Flask(__name__)


CORS(app, resources={r"*": {"origins": "*"}})

# Configure Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")
app.json.compact = False  # Optional setting for more readable JSON output

# Initialize SQLAlchemy and migrations
db.init_app(app)
migrate = Migrate(app, db)

# Drug Routes

@app.route('/drugs', methods=['GET', 'POST'])
def drugs():
    if request.method == 'GET':
        try:
            drugs = Drug.query.all()  # Retrieve all drugs
            all_drugs = [drug.to_dict() for drug in drugs]
            return jsonify(all_drugs), 200  # Return all drugs
        except ValueError as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'ndc_id' not in data or 'name' not in data:
            return jsonify({"error": "Fields 'ndc_id' and 'name' are required"}), 400

        try:
            new_drug = Drug(
                ndc_id=data['ndc_id'],
                name=data['name'],
                description=data.get('description', ''),  # Optional field
                dosage_form=data.get('dosage_form', ''),  # Optional field
                strength=data.get('strength', '')
            )

            db.session.add(new_drug)
            db.session.commit()

            return jsonify(new_drug.to_dict()), 201  # Return the created drug and HTTP status 201
        except ValueError as e:
            db.session.rollback()
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/drugs/ndc/<ndc_id>', methods=['GET'])
def get_drugs_by_ndc(ndc_id):
    try:
        drugs = Drug.query.filter_by(ndc_id=ndc_id).all()

        if not drugs:
            return jsonify({"error": f"No drugs found with NDC_ID {ndc_id}"}), 404
        
        all_drugs = [drug.to_dict() for drug in drugs]
        return jsonify(all_drugs), 200

    except ValueError as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

#Route for Get by ID + Delete by ID
@app.route('/drugs/<int:id>', methods=['GET', 'DELETE'])
def drug_by_id(id):
    if request.method == 'GET':
        drug = Drug.query.get(id)  # Retrieve the drug by ID

        if not drug:
            return jsonify({"error": f"Drug with ID {id} not found"}), 404
        
        return jsonify(drug.to_dict()), 200  # Return drug details as JSON

    elif request.method == 'DELETE':
        try:
            drug = Drug.query.get(id)  # Retrieve the drug by ID

            if not drug:
                return jsonify({"error": f"Drug with ID {id} not found"}), 404
            
            db.session.delete(drug)  # Delete the drug
            db.session.commit()
            
            return jsonify({"message": f"Drug with ID {id} deleted successfully"}), 200

        except ValueError as e:
            db.session.rollback()
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    else:
        return jsonify({"error": "Unsupported method"}), 405  # Handle unsupported methods



# Patient Routes

# CREATE - Add a new patient
@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if not all(key in data for key in ["name", "address", "insurance"]):
        return jsonify({"error": "Fields 'name', 'address', 'insurance' are required"}), 400
    
    try:
        new_patient = Patient(
            name=data['name'],
            address=data['address'],
            insurance=data['insurance']
        )
        
        db.session.add(new_patient)  # Add new patient to the database
        db.session.commit()

        return jsonify(new_patient.to_dict()), 201  # Return the created patient and status code 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Patient with similar details already exists"}), 409  # Conflict error if patient exists

    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# READ - Get a specific patient by ID
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient_by_id(id):
    patient = Patient.query.get(id)  # Retrieve the patient by ID
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    return jsonify(patient.to_dict()), 200  # Return patient data


# READ - Get all patients
@app.route('/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()  # Retrieve all patients
    
    patients_list = [patient.to_dict() for patient in patients]  # Convert to dictionary list
    
    return jsonify(patients_list), 200  # Return all patients


# UPDATE - Update a specific patient by ID
@app.route('/patients/<int:id>', methods=['PATCH'])
def update_patient(id):
    patient = Patient.query.get(id)
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update patient fields if provided in the PATCH data
    patient.name = data.get("name", patient.name)
    patient.address = data.get("address", patient.address)
    patient.insurance = data.get("insurance", patient.insurance)
    
    db.session.commit()
    
    return jsonify(patient.to_dict()), 200  # Return updated patient data


# DELETE - Delete a specific patient by ID
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)
    
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    
    try:
        db.session.delete(patient)  # Delete the patient
        db.session.commit()
        
        return jsonify({"message": f"Patient with ID {id} deleted successfully"}), 200
    
    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Pharmacist Routes

@app.route('/pharmacists', methods=['GET'])
def get_all_pharmacists():
    try:
        pharmacists = Pharmacist.query.all()  # Retrieve all pharmacists
        all_pharmacists = [pharm.to_dict() for pharm in pharmacists]
        return jsonify(all_pharmacists), 200  # Return all pharmacists as JSON

    except ValueError as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/pharmacists/<int:id>', methods=['GET'])
def get_pharmacist_by_id(id):
    pharmacist = Pharmacist.query.get(id)  # Retrieve the pharmacist by ID

    if not pharmacist:
        return jsonify({"error": "Pharmacist not found"}), 404
    
    return jsonify(pharmacist.to_dict()), 200

# Create a new pharmacist
@app.route('/pharmacists', methods=['POST'])
def create_pharmacist():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Check for required fields
    if 'name' not in data or 'pharmacy' not in data:
        return jsonify({"error": "Fields 'name' and 'pharmacy' are required"}), 400

    try:
        new_pharmacist = Pharmacist(
            name=data['name'],
            pharmacy=data['pharmacy']
        )
        
        db.session.add(new_pharmacist)  # Add the new pharmacist to the database
        db.session.commit()

        return jsonify(new_pharmacist.to_dict()), 201  # Return the created pharmacist and status code 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Pharmacist with similar details already exists"}), 409  # Conflict if duplicate

    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Delete a pharmacist by ID
@app.route('/pharmacists/<int:id>', methods=['DELETE'])
def delete_pharmacist(id):
    pharmacist = Pharmacist.query.get(id)  # Retrieve pharmacist by ID
    
    if not pharmacist:
        return jsonify({"error": "Pharmacist not found"}), 404
    
    try:
        db.session.delete(pharmacist)  # Delete the pharmacist
        db.session.commit()

        return jsonify({"message": f"Pharmacist with ID {id} deleted successfully"}), 200

    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Prescription Routes

@app.route('/prescriptions', methods=['GET', 'POST'])
def get_or_create_prescriptions():
    if request.method == 'GET':
        try:
            prescriptions = Prescription.query.all()  # Retrieve all prescriptions
            
            all_prescriptions = []
            for pres in prescriptions:
                # Construct the response with related data
                pres_data = {
                    "id": pres.id,
                    "created_at": pres.created_at,
                    "instructions": pres.instructions,
                    "status": pres.status,
                    "drug": {
                        "id": pres.drug.id,
                        "name": pres.drug.name,
                        "description": pres.drug.description,
                        "strength": pres.drug.strength,
                        "dosage_form": pres.drug.dosage_form
                    },
                    "patient": {
                        "id": pres.patient.id,
                        "name": pres.patient.name,
                        "address": pres.patient.address,
                        "insurance": pres.patient.insurance
                    },
                    "pharmacist": {
                        "id": pres.pharmacist.id,
                        "name": pres.pharmacist.name,
                        "pharmacy": pres.pharmacist.pharmacy
                    }
                }
                all_prescriptions.append(pres_data)

            return jsonify(all_prescriptions), 200  # Return all prescription data with related info

        except ValueError as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
    elif request.method == 'POST':
        data = request.get_json()

        if not data or not all(key in data for key in ["drug_id", "patient_id", "pharmacist_id"]):
            return jsonify({"error": "Fields 'drug_id', 'patient_id', 'pharmacist_id' are required"}), 400
        
        try:
            new_prescription = Prescription(
                drug_id=data["drug_id"],
                patient_id=data["patient_id"],
                pharmacist_id=data["pharmacist_id"],
                instructions=data.get("instructions", ""),
                status=data.get("status", "pending")
            )

            db.session.add(new_prescription)
            db.session.commit()

            return jsonify(new_prescription.to_dict()), 201  # Return the created prescription

        except ValueError as e:
            db.session.rollback()
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/prescriptions/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def prescription_by_id(id):
    if request.method == 'GET':
        prescription = Prescription.query.get(id)  # Retrieve the prescription by ID
        
        if not prescription:
            return jsonify({"error": "Prescription not found"}), 404
        
        return jsonify(prescription.to_dict()), 200
    
    elif request.method == 'PATCH':
        data = request.get_json()

        try:
            prescription = Prescription.query.get(id)  # Retrieve the prescription by ID
            if not prescription:
                return jsonify({"error": "Prescription not found"}), 404
            
            prescription.drug_id = data.get("drug_id", prescription.drug_id)
            prescription.patient_id = data.get("patient_id", prescription.patient_id)
            prescription.instructions = data.get("instructions", prescription.instructions)
            
            db.session.commit()
            
            return jsonify(prescription.to_dict()), 200  # Return the updated prescription

        except ValueError as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    
    elif request.method == 'DELETE':
        try:
            prescription = Prescription.query.get(id)  # Retrieve the prescription by ID
            
            if not prescription:
                return jsonify({"error": "Prescription not found"}), 404
            
            db.session.delete(prescription)
            db.session.commit()  # Commit the deletion
            
            return jsonify({"message": "Prescription deleted successfully"}), 200
        
        except ValueError as e:
            db.session.rollback()
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Basket Routes

@app.route('/basket', methods=['GET', 'POST'])
def basket():
    if request.method == 'GET':
        basket_items = Basket.query.all()  # Get all basket items
        serialized_items = [item.to_dict() for item in basket_items]
        return jsonify(serialized_items), 200
    
    elif request.method == 'POST':
        data = request.get_json()

        if not data or not all(key in data for key in ["patient_id", "prescription_id"]):
            return jsonify({"error": "Fields 'patient_id' and 'prescription_id' are required"}), 400
        
        try:
            new_basket_item = Basket(
                patient_id=data["patient_id"],
                prescription_id=data["prescription_id"],
                quantity=data.get("quantity", 1),  # Default quantity
            )
            
            db.session.add(new_basket_item)
            db.session.commit()

            return jsonify(new_basket_item.to_dict()), 201

        except ValueError as e:
            db.session.rollback()
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/basket/<int:id>', methods=['DELETE'])
def delete_basket_item(id):
    try:
        basket_item = Basket.query.get(id)

        if not basket_item:
            return jsonify({"error": "Basket item not found"}), 404
        
        db.session.delete(basket_item)
        db.session.commit()  # Commit the deletion
        
        return jsonify({"message": "Basket item deleted successfully"}), 200

    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Start the Flask server
if __name__=="__main__":
    app.run(port=5555, debug=True)
