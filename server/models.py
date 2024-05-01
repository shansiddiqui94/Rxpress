# Import necessary modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

# Patient Model
class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    insurance = db.Column(db.String(60))

    # Relationship with Prescription model (one-to-many)
    prescriptions = db.relationship("Prescription", back_populates='patient')
    serialize_rules = ['-prescriptions.patient']

# Pharmacist Model
class Pharmacist(db.Model, SerializerMixin):
    __tablename__ = 'pharmacist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pharmacy = db.Column(db.String(100), nullable=False)

    # Relationship with Prescription model (one-to-many)
    prescriptions = db.relationship("Prescription", back_populates='pharmacist')
    serialize_rules = ['-prescriptions.pharmacist']

# Drug Model
class Drug(db.Model, SerializerMixin):
    __tablename__ = 'drug'

    id = db.Column(db.Integer, primary_key=True)
    ndc_id = db.Column(db.String(10), nullable=False)  # NDC identifier with uniqueness constraint, no two rows of ndc are the same
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    dosage_form = db.Column(db.String(50))  # e.g., tablet, capsule, liquid
    strength = db.Column(db.String(50))  # e.g., 10mg, 500mg/mL)

    # Relationship with Prescription model (one-to-many)
    prescriptions = db.relationship("Prescription", back_populates='drug')
    serialize_rules = ['-prescriptions.drug']

# Prescription Model
class Prescription(db.Model, SerializerMixin):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'), nullable=False)
    instructions = db.Column(db.String(255))
    # Add a field for the date the prescription was created
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Add a field for the status (e.g., pending, approved, rejected)
    status = db.Column(db.String(50), default='pending')

    patient = db.relationship("Patient")
    drug = db.relationship("Drug")
    pharmacist = db.relationship("Pharmacist")
    serialize_rules = ['-patient.prescriptions', '-drug.prescriptions', '-pharmacist.prescriptions']

# Basket Model (Optional)
class Basket(db.Model, SerializerMixin):
    __tablename__ = 'basket'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    prescription_id = db.Column(db.Integer, db.ForeignKey('prescription.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    # Add a field for the status (e.g., added, removed, submitted)
    status = db.Column(db.String(20), default='added')
    # Consider adding a timestamp for when the prescription was added to the basket

    patient = db.relationship("Patient")
    prescription = db.relationship("Prescription")
    serialize_rules = ['-patient.baskets', '-prescription.basket']