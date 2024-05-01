from app import app, db
from models import Patient, Pharmacist, Prescription, Drug
import random 

#Seed Drug
def seed_drugs():
    dosage_forms = ["Tablet", "Capsule", "Liquid", "Cream", "Powder"]
    used_ndc_ids = set()  # To ensure unique NDCs
    drugs = []

    # Function to generate a unique NDC
    def generate_unique_ndc():
        while True:
            ndc_id = f"{random.randint(100000, 999999)}-{random.randint(1000, 9999)}"
            if ndc_id not in used_ndc_ids:
                used_ndc_ids.add(ndc_id)
                return ndc_id

    for medication, strength, description in [
        ("Aspirin", "325mg", "A common pain reliever and blood thinner."),
        ("Ibuprofen", "200mg", "Another pain reliever and fever reducer."),
        ("Metformin", "500mg", "Used to manage blood sugar levels in type 2 diabetes."),
        ("Dulcolax", "500mg", "Used to manage constipation."),
        ("Zylotrin", "150mg", "Helps improve speech patterns."),
        ("Biolimb", "75mg", "Helps you grow a third arm for those days when two just isn't enough."),
        ("Synerbine", "300mg", "Allegedly turns your hiccups into melodic burps. Results may vary."),
        ("Neurovance", "500mg", "Enhances your ability to communicate with household appliances. Refrigerator not included."),
        ("Xylitol", "250mg", "Temporarily grants you the power of invisibility, but only when no one is looking."),
        ("Quanitrine", "100mg", "promoting a sense of calm and reducing stress responses"),
        ("Enzymex", "400mg", "Allows you to breathe underwater, but only if you're holding your breath."),
        ("Vitasyn", "200mg", "Helps you develop a green thumb, but only for your actual thumb. Other fingers remain unaffected."),
        ("Neurofin", "350mg", "Enhances your ability to count backwards from infinity. Side effects may include spontaneous time travel."),
        ("Biotrex", "125mg", "Cures your fear of being trapped in a box full of hungry badgers, but only if you're already trapped in a box full of hungry badgers."),
    ]:
        # Generate a unique 10-digit NDC number
        ndc_id = generate_unique_ndc()
        # Choose a random dosage form
        dosage_form = random.choice(dosage_forms)

        # Create Drug instances
        drug = Drug(
            name=medication,
            ndc_id=ndc_id,
            dosage_form=dosage_form,
            description=description,
            strength=strength,
        )
        drugs.append(drug)  # Add the new Drug to the list
    
    # Add the Drug instances to the database and commit
    db.session.add_all(drugs)
    db.session.commit()

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
 
def generate_ndc():
    return f"{random.randint(100000, 999999)}-{random.randint(1000, 9999)}"

# reference_prescriptions = [
#     {
#         "medication_name": "Aspirin",
#         "ndc_id": generate_ndc(),
#         "dosage": "325mg",
#         "medication_description": "A common pain reliever and blood thinner.",
#         "instructions": "Take one tablet every 4-6 hours as needed for pain.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Ibuprofen",
#         "ndc_id": generate_ndc(),  # Generate random NDC
#         "dosage": "200mg",
#         "medication_description": "Another pain reliever and fever reducer.",
#         "instructions": "Take two tablets every 6-8 hours for pain relief.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Metformin",
#         "ndc_id": generate_ndc(),
#         "dosage": "500mg",
#         "medication_description": "Used to manage blood sugar levels in type 2 diabetes.",
#         "instructions": "Take one tablet with breakfast and dinner.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Dulcolax",
#         "ndc_id": generate_ndc(),
#         "dosage": "500mg",
#         "medication_description": "Used to manage constipation.",
#         "instructions": "Take one tablet before bed.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Zylotrin",
#         "ndc_id": generate_ndc(),
#         "dosage": "150mg",
#         "medication_description": "Helps improve speech patterns.",
#         "instructions": "Take one tablet every morning with food.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Biolimb",
#         "ndc_id": generate_ndc(),
#         "dosage": "75mg",
#         "medication_description": "Helps you grow a third arm for those days when two just isn't enough.",
#         "instructions": "Apply once daily to the shoulder area where a third arm is desired.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Synerbine",
#         "ndc_id": generate_ndc(),
#         "dosage": "300mg",
#         "medication_description": "Allegedly turns your hiccups into melodic burps. Results may vary.",
#         "instructions": "Take one tablet with each meal to prevent hiccups.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Neurovance",
#         "ndc_id": generate_ndc(),
#         "dosage": "500mg",
#         "medication_description": "Enhances your ability to communicate with household appliances. Refrigerator not included.",
#         "instructions": "Take one tablet before attempting communication with appliances.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Xylitol",
#         "ndc_id": generate_ndc(),
#         "dosage": "250mg",
#         "medication_description": "Temporarily grants you the power of invisibility, but only when no one is looking.",
#         "instructions": "Take before venturing into areas where stealth is required.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Quanitrine",
#         "ndc_id": generate_ndc(),
#         "dosage": "100mg",
#         "medication_description": "Cures your fear of being trapped in a box full of hungry badgers. Disclaimer: May cause fear of being trapped in a box full of hungry badgers.",
#         "instructions": "Take one tablet at the first sign of badger-related anxiety.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Enzymex",
#         "ndc_id": generate_ndc(),
#         "dosage": "400mg",
#         "medication_description": "Allows you to breathe underwater, but only if you're holding your breath.",
#         "instructions": "Take before swimming or scuba diving. Results are not guaranteed.",
#         "status": "rejected",
#     },
#     {
#         "medication_name": "Vitasyn",
#         "ndc_id": generate_ndc(),
#         "dosage": "200mg",
#         "medication_description": "Helps you develop a green thumb, but only for your actual thumb. Other fingers remain unaffected.",
#         "instructions": "Apply to the thumb daily for best results.",
#         "status": "approved",
#     },
#     {
#         "medication_name": "Neurofin",
#         "ndc_id": generate_ndc(),
#         "dosage": "350mg",
#         "medication_description": "Enhances your ability to count backwards from infinity. Side effects may include spontaneous time travel.",
#         "instructions": "Take while attempting advanced mathematics or temporal experiments.",
#         "status": "pending",
#     },
#     {
#         "medication_name": "Biotrex",
#         "ndc_id": generate_ndc(),
#         "dosage": "125mg",
#         "medication_description": "Cures your fear of being trapped in a box full of hungry badgers, but only if you're already trapped in a box full of hungry badgers.",
#         "instructions": "Take if you find yourself in a box with badgers. Not for preemptive use.",
#         "status": "approved",
#     },
# ]

def seed_prescriptions():
    # Fetch the existing data from the database
    patients = Patient.query.all()  # Fetch existing patients
    pharmacists = Pharmacist.query.all()  # Fetch existing pharmacists
    drugs = Drug.query.all()  # Fetch existing drugs
    
    prescriptions = [
        Prescription(
            patient_id=random.choice(patients).id,  # Randomly select a patient
            pharmacist_id=random.choice(pharmacists).id,  # Randomly select a pharmacist
            drug_id=random.choice(drugs).id,  # Correctly reference Drug ID
            instructions=f"Take {random.choice(drugs).strength} as directed on the label.",  # Custom instructions
            status="pending"  # Example status
        )
        for _ in range(10)  # Number of prescriptions to create
    ]

    db.session.add_all(prescriptions)  # Add all Prescription instances to the database
    db.session.commit()

# Run the seeding functions within the application context
if __name__ == "__main__":
    with app.app_context():
        seed_patients()  # Seed Patient records
        seed_pharmacists()  # Seed Pharmacist records
        # Seed Drug records before seeding Prescriptions
        seed_drugs()  # Seed Drug records
        seed_prescriptions()  # Seed Prescription records
