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

#  Get Drug by name
@app.route('/drugs', methods=['GET', 'POST'])
def drugs():
    if request.method == 'GET':
        try:
            name = request.args.get('name')
            if not name:
                return jsonify({'error': 'Missing name query parameter'}), 400 

            drugs = db.session.query(Drug).join(Prescription).filter(Drug.name == name).all()

            # Format results including prescriptions
            results = []
            for drug in drugs:
                drug_dict = drug.to_dict()
                drug_dict['prescriptions'] = [p.to_dict() for p in drug.prescriptions]
                results.append(drug_dict)

            return jsonify(results), 200 

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

#Patient search by name
@app.route('/patients/search', methods=['GET'])
def search_patients():
    # Retrieve the search term from the query parameters
    search_term = request.args.get('name')

    # Validate that a search term was provided
    if not search_term or search_term.strip() == '':
        return jsonify({"error": "Search term 'name' is required"}), 400

    try:
        # Perform a case-insensitive search for patients matching the search term
        patients = Patient.query.filter(Patient.name.ilike(f'%{search_term}%')).all()

        # If no matching patients are found, return a message indicating this
        if not patients:
            return jsonify({"message": f"No patients found matching the term '{search_term}'"}), 200

        # Convert the found patients to a list of dictionaries
        results = [patient.to_dict() for patient in patients]

        # Return the results as JSON with a success status code
        return jsonify(results), 200

    except ValueError as e:  
        print(f"Error while searching for patients: {str(e)}")

        return jsonify({"error": "An unexpected error occurred while searching for patients"}), 500



#Prescription Fetching by PatientID
@app.route('/patients/<int:patient_id>/prescriptions', methods=['GET'])
def get_prescriptions_by_patient(patient_id):
    patient = Patient.query.get(patient_id)

    if not patient:
        return jsonify({"error": f"Patient with ID {patient_id} not found"}), 404

    prescriptions = patient.prescriptions  # Access prescriptions through the relationship
    prescription_list = [pres.to_dict() for pres in prescriptions]

    return jsonify(prescription_list), 200






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
