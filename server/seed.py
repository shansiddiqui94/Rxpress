from app import db  # Import your database instance
from app.models import Prescription  # Import your Prescription model

# Sample reference drugs (modify as needed)
reference_drugs = [
    {
        "medication_name": "Aspirin",
        "dosage": "325mg",
        "medication_description": "A common pain reliever and blood thinner.",
    },
    {
        "medication_name": "Ibuprofen",
        "dosage": "200mg",
        "medication_description": "Another pain reliever and fever reducer.",
    },
    {
        "medication_name": "Metformin",
        "dosage": "500mg",
        "medication_description": "Used to manage blood sugar levels in type 2 diabetes.",
    },
    {
        "medication_name": "Dulcolax",
        "dosage": "500mg",
        "medication_description": "Use to manage explosive farts, and constipation relief",
    },
        {
        "medication_name": "Zylotrin",
        "dosage": "150mg",
        "medication_description": "A medication that may or may not cure your inability to speak in reverse.",
    },
    {
        "medication_name": "Biotrex",
        "dosage": "75mg",
        "medication_description": "Helps you grow a third arm for those days when two just isn't enough.",
    },
    {
        "medication_name": "Synerbine",
        "dosage": "300mg",
        "medication_description": "Allegedly turns your hiccups into melodic burps. Results may vary.",
    },
    {
        "medication_name": "Neurovance",
        "dosage": "500mg",
        "medication_description": "Enhances your ability to communicate with household appliances. Refrigerator not included.",
    },
    {
        "medication_name": "Xylitol",
        "dosage": "250mg",
        "medication_description": "Temporarily grants you the power of invisibility, but only when no one is looking.",
    },
    {
        "medication_name": "Quanitrine",
        "dosage": "100mg",
        "medication_description": "Cures your fear of being trapped in a box full of hungry badgers. Disclaimer: May cause fear of being trapped in a box full of hungry badgers.",
    },
    {
        "medication_name": "Enzymex",
        "dosage": "400mg",
        "medication_description": "Allows you to breathe underwater, but only if you're holding your breath.",
    },
    {
        "medication_name": "Vitasyn",
        "dosage": "200mg",
        "medication_description": "Helps you develop a green thumb, but only for your actual thumb. Other fingers remain unaffected.",
    },
    {
        "medication_name": "Neurofin",
        "dosage": "350mg",
        "medication_description": "Enhances your ability to count backwards from infinity. Side effects may include spontaneous time travel.",
    },
    {
        "medication_name": "Biotrex",
        "dosage": "125mg",
        "medication_description": "Cures your fear of being trapped in a box full of hungry badgers, but only if you're already trapped in a box full of hungry badgers.",
    },

    
]

# Define the function to seed the database
def seed_prescriptions():
    """Seeds the database with the list of Prescription instances."""
    # Clear the existing data if needed
    # Be careful with this in production environments
    Prescription.query.delete()

    # Create Prescription instances from the reference_drugs list
    prescriptions = [Prescription(**drug_data) for drug_data in reference_drugs]

    # Add the Prescription instances to the session
    db.session.add_all(prescriptions)

    try:
        # Commit the session to save the new records
        db.session.commit()
    except Exception as e:
        # Rollback the transaction in case of an error
        db.session.rollback()
        print(f"Error seeding the database: {e}")

# Run the seeding function
if __name__ == "__main__":
    seed_prescriptions()