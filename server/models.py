# Import necessary modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

#Patient Model
# class Patient(db.Model, SerializerMixin):
#     __tablename__ = 'patient'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(100))
#     insurance = db.Column(db.String(60))

#     # Relationship with Prescription model (one-to-many)
#     prescriptions = db.relationship("Prescription", back_populates='patient')
#     serialize_rules = ['-prescriptions.patient']
# #----------------------------------------------------------------------------------------
# New patient model:

class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Patient name
    address = db.Column(db.String(255))  # Patient address
    insurance = db.Column(db.String(100))  # Insurance type or company
    
     # Define the `to_dict()` method to convert the object to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "insurance": self.insurance
        }


#----------------------------------------------------------------------------------------
# New Pharmacist model
class Pharmacist(db.Model):
    __tablename__ = 'pharmacist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Pharmacist name
    pharmacy = db.Column(db.String(100))  # Pharmacy name or affiliation


#----------------------------------------------------------------------------------------

#Pharmacist Model

# class Pharmacist(db.Model, SerializerMixin):
#     __tablename__ = 'pharmacist'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     pharmacy = db.Column(db.String(100), nullable=False)

#     # Relationship with Prescription model (one-to-many)
#     prescriptions = db.relationship("Prescription", back_populates='pharmacist')
#     serialize_rules = ['-prescriptions.pharmacist']

#----------------------------------------------------------------------------------------
#Drug Model NEW:


class Drug(db.Model):
    __tablename__ = 'drug'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    ndc_id = db.Column(db.String(10), nullable=False, unique=True)  # Unique NDC identifier
    name = db.Column(db.String(100), nullable=False)  # Drug name
    description = db.Column(db.String(255))  # Description
    dosage_form = db.Column(db.String(50))  # Form (tablet, capsule, etc.)
    strength = db.Column(db.String(50))  # Drug strength
    
    # Relationship with Prescription model (one-to-many), but excluded from serialization
    prescriptions = db.relationship(
        "Prescription",
        back_populates="drug",
        lazy=True,  # Ensure the relationship is not eagerly loaded
    )

    # Custom `to_dict()` method that does not include the `prescriptions` relationship
    def to_dict(self):
        return {
            'id': self.id,
            'ndc_id': self.ndc_id,
            'name': self.name,
            'description': self.description,
            'dosage_form': self.dosage_form,
            'strength': self.strength,
        }



#----------------------------------------------------------------------------------------

#Drug Model
# class Drug(db.Model, SerializerMixin):
#     __tablename__ = 'drug'

#     id = db.Column(db.Integer, primary_key=True)
#     ndc_id = db.Column(db.String(10), nullable=False)  # NDC identifier with uniqueness constraint, no two rows of ndc are the same
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(255))
#     dosage_form = db.Column(db.String(50))  # e.g., tablet, capsule, liquid
#     strength = db.Column(db.String(50))  # e.g., 10mg, 500mg/mL)

#     # Relationship with Prescription model (one-to-many)
#     prescriptions = db.relationship("Prescription", back_populates='drug')
#     serialize_rules = ['-prescriptions.drug']


#----------------------------------------------------------------------------------------
# Prescription Model nEW:
class Prescription(db.Model):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))  # Foreign key to Drug
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))  # Foreign key to Patient
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'))  # Foreign key to Pharmacist
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of prescription
    instructions = db.Column(db.String(255))  # Instructions for use
    status = db.Column(db.String(50), default='pending')  # Status of prescription

    # Relationships to link Prescription with other models
    drug = db.relationship('Drug', back_populates='prescriptions')  # Link to Drug
    patient = db.relationship('Patient')  # Link to Patient
    pharmacist = db.relationship('Pharmacist')  # Link to Pharmacist

#----------------------------------------------------------------------------------------

# Prescription Model
# class Prescription(db.Model, SerializerMixin):
#     __tablename__ = 'prescription'

#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
#     drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
#     pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'), nullable=False)
#     instructions = db.Column(db.String(255))
#     # Add a field for the date the prescription was created
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     # Add a field for the status (e.g., pending, approved, rejected)
#     status = db.Column(db.String(50), default='pending')

#     patient = db.relationship("Patient")
#     drug = db.relationship("Drug")
#     pharmacist = db.relationship("Pharmacist")
#     serialize_rules = ['-patient.prescriptions', '-drug.prescriptions', '-pharmacist.prescriptions']

#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------


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