from app import app, db
from models import Patient, Pharmacist, Prescription
import random

# import logging

# logging.basicConfig(level=logging.ERROR, filename='seed_errors.log')

# # Seed UserAuth records
# def seed_user_auth():
#     users = [
#         {"username": "john_doe", "password": "password123", "role": "patient"},
#         {"username": "jane_smith", "password": "password456", "role": "patient"},
#         {"username": "dr_brown", "password": "password789", "role": "pharmacist"},
#     ]
    
#     # Create UserAuth records and set passwords
#     for user in users:
#         user_auth = UserAuth(**user)
#         user_auth.set_password(user["password"])
#         db.session.add(user_auth)
    
#     db.session.commit()

# # Define user_auth_map at a higher scope
# user_auth_map = {user.username: user.id for user in UserAuth.query.all()}

#Seed Patient records
def seed_patients():
    patients = [
        {"name": "John Doe", "address": "123 Elm St", "insurance": "Medicare"},
        {"name": "Jane Smith", "address": "456 Oak St", "insurance": "Medicaid"},
        {"name": "Alice Johnson", "address": "789 Pine St", "insurance": "Blue Cross"},
        {"name": "Bob Williams", "address": "101 Maple Ave", "insurance": "UnitedHealthcare"},
        {"name": "Charlie Brown", "address": "234 Cedar Rd", "insurance": "Aetna"},
        {"name": "Diana White", "address": "567 Birch Blvd", "insurance": "Cigna"},
        {"name": "Edward Green", "address": "890 Willow Ln", "insurance": "Humana"},
        {"name": "Fiona Black", "address": "345 Spruce Ct", "insurance": "Kaiser Permanente"},
        {"name": "George King", "address": "678 Aspen Way", "insurance": "State Farm"},
    ]
    
    db.session.add_all([Patient(**p) for p in patients])
    db.session.commit()

# Seed Pharmacist records
def seed_pharmacists():
    pharmacists = [
        { "name": "Dr. Brown", "pharmacy": "RX Pharmacy"},
        { "name": "Dr. Emma Clark", "pharmacy": "HealthFirst Pharmacy" },
        { "name": "Dr. Liam Johnson", "pharmacy": "City Pharmacy" },
        { "name": "Dr. Ava Davis", "pharmacy": "Community Pharmacy" },
        { "name": "Dr. Sophia Lee", "pharmacy": "Wellness Pharmacy" },
        { "name": "Dr. Lucas Miller", "pharmacy": "RX Plus Pharmacy" },
        { "name": "Dr. Emily Brown", "pharmacy": "Health & Care Pharmacy" },
    ]
    
    db.session.add_all([Pharmacist(**p) for p in pharmacists])
    db.session.commit()

# Seed Prescription records
def seed_prescriptions():
    patients = Patient.query.all()  # Fetch existing patients
    pharmacists = Pharmacist.query.all()  # Fetch existing pharmacists
    
    # patient = patients  # Use the first patient
    # pharmacist = pharmacists  # Use the first pharmacist
    
    reference_drugs = [
    {
        "medication_name": "Aspirin",
        "dosage": "325mg",
        "medication_description": "A common pain reliever and blood thinner.",
        "instructions": "Take one tablet every 4-6 hours as needed for pain.",
        "status": "approved",
    },
    {
        "medication_name": "Ibuprofen",
        "dosage": "200mg",
        "medication_description": "Another pain reliever and fever reducer.",
        "instructions": "Take two tablets every 6-8 hours for pain relief.",
        "status": "approved",

    },
    {
        "medication_name": "Metformin",
        "dosage": "500mg",
        "medication_description": "Used to manage blood sugar levels in type 2 diabetes.",
        "instructions": "Take one tablet with breakfast and dinner.",
        "status": "approved",

    },
    {
        "medication_name": "Dulcolax",
        "dosage": "500mg",
        "medication_description": "Used to manage constipation.",
        "instructions": "Take one tablet before bed.",
        "status": "pending",
    },
    {
        "medication_name": "Zylotrin",
        "dosage": "150mg",
        "medication_description": "Helps improve speech patterns.",
        "instructions": "Take one tablet every morning with food.",
        "status": "pending",
    },
    {
        "medication_name": "Biolimb",
        "dosage": "75mg",
        "medication_description": "Helps you grow a third arm for those days when two just isn't enough.",
        "instructions": "Apply once daily to the shoulder area where a third arm is desired.",
        "status": "pending",
    },
    {
        "medication_name": "Synerbine",
        "dosage": "300mg",
        "medication_description": "Allegedly turns your hiccups into melodic burps. Results may vary.",
        "instructions": "Take one tablet with each meal to prevent hiccups.",
        "status": "approved",
    },
    {
        "medication_name": "Neurovance",
        "dosage": "500mg",
        "medication_description": "Enhances your ability to communicate with household appliances. Refrigerator not included.",
        "instructions": "Take one tablet before attempting communication with appliances.",
        "status": "pending",
    },
    {
        "medication_name": "Xylitol",
        "dosage": "250mg",
        "medication_description": "Temporarily grants you the power of invisibility, but only when no one is looking.",
        "instructions": "Take before venturing into areas where stealth is required.",
        "status": "approved",
    },
    {
        "medication_name": "Quanitrine",
        "dosage": "100mg",
        "medication_description": "Cures your fear of being trapped in a box full of hungry badgers. Disclaimer: May cause fear of being trapped in a box full of hungry badgers.",
        "instructions": "Take one tablet at the first sign of badger-related anxiety.",
        "status": "pending",
    },
    {
        "medication_name": "Enzymex",
        "dosage": "400mg",
        "medication_description": "Allows you to breathe underwater, but only if you're holding your breath.",
        "instructions": "Take before swimming or scuba diving. Results are not guaranteed.",
        "status": "rejected",
    },
    {
        "medication_name": "Vitasyn",
        "dosage": "200mg",
        "medication_description": "Helps you develop a green thumb, but only for your actual thumb. Other fingers remain unaffected.",
        "instructions": "Apply to the thumb daily for best results.",
        "status": "approved",
    },
    {
        "medication_name": "Neurofin",
        "dosage": "350mg",
        "medication_description": "Enhances your ability to count backwards from infinity. Side effects may include spontaneous time travel.",
        "instructions": "Take while attempting advanced mathematics or temporal experiments.",
        "status": "pending",
    },
    {
        "medication_name": "Biotrex",
        "dosage": "125mg",
        "medication_description": "Cures your fear of being trapped in a box full of hungry badgers, but only if you're already trapped in a box full of hungry badgers.",
        "instructions": "Take if you find yourself in a box with badgers. Not for preemptive use.",
        "status": "approved",
    },

    
]
    
    prescriptions = [
        Prescription(
            patient_id=random.choice(patients).id,  # Randomly select a patient
            pharmacist_id=random.choice(pharmacists).id,  # Randomly select a pharmacist
            medication_name=drug["medication_name"],
            dosage=drug["dosage"],
            instructions=drug["instructions"],
            medication_description=drug["medication_description"],
            status=drug["status"]
        )
        for drug in reference_drugs
    ]
    
    db.session.add_all(prescriptions)
    db.session.commit()

# Run the seeding functions within the application context
if __name__ == "__main__":
    with app.app_context():
         # Ensure valid UserAuth records
        seed_patients()  # Seed Patient records
        seed_pharmacists()  # Seed Pharmacist records
        seed_prescriptions()  # Seed Prescription records
