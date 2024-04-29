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

    prescriptions = db.relationship("Prescription", back_populates="patient")
    serialize_rules = ["-prescriptions.patient"]

# Pharmacist Model
class Pharmacist(db.Model, SerializerMixin):
    __tablename__ = 'pharmacist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pharmacy = db.Column(db.String(100), nullable=False)

    prescriptions = db.relationship("Prescription", back_populates="pharmacist")
    serialize_rules = ["-prescriptions.pharmacist"]

# Prescription Model
class Prescription(db.Model, SerializerMixin):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'), nullable=False)
    medication_name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.String(255))
    medication_description = db.Column(db.String(255))
    status = db.Column(db.String(20), nullable=False)

    patient = db.relationship("Patient", back_populates="prescriptions")
    pharmacist = db.relationship("Pharmacist", back_populates="prescriptions")
    serialize_rules = ["-patient.prescriptions", "-pharmacist.prescriptions"]

# Basket Model
class Basket(db.Model, SerializerMixin):
    __tablename__ = 'basket'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    prescription_id = db.Column(db.Integer, db.ForeignKey('prescription.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(20), default='pending')

    # patient = db.relationship("Patient", back_populates="baskets")
