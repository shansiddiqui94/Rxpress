# # Import necessary modules
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
# from datetime import datetime

# # Initialize SQLAlchemy
# db = SQLAlchemy()

# #Patient Model

# class Patient(db.Model):
#     __tablename__ = 'patient'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)  # Patient name
#     address = db.Column(db.String(255))  # Patient address
#     insurance = db.Column(db.String(100))  # Insurance type or company

#      # Define the `to_dict()` method to convert the object to a dictionary
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "address": self.address,
#             "insurance": self.insurance
#         }
#     # Serialize_rules
#     prescriptions = db.relationship('Prescription', back_populates='patient')  # Relationship
#     serialize_rules = ('-prescriptions',)  # Exclude prescriptions during serialization of Patient


# # Pharmacist model
# class Pharmacist(db.Model):
#     __tablename__ = 'pharmacist'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)  # Pharmacist name
#     pharmacy = db.Column(db.String(100))  # Pharmacy name or affiliation
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "pharmacy_name": self.pharmacy,
#         }




# #Drug Model NEW:


# class Drug(db.Model):
#     __tablename__ = 'drug'

#     id = db.Column(db.Integer, primary_key=True)  # Primary key
#     ndc_id = db.Column(db.String(10), nullable=False, unique=True)  # Unique NDC identifier
#     name = db.Column(db.String(100), nullable=False)  # Drug name
#     description = db.Column(db.String(255))  # Description
#     dosage_form = db.Column(db.String(50))  # Form (tablet, capsule, etc.)
#     strength = db.Column(db.String(50))  # Drug strength
    
#     # Relationship with Prescription model (one-to-many), but excluded from serialization
#     prescriptions = db.relationship(
#         "Prescription",
#         back_populates="drug",
#         lazy=True,  # Ensure the relationship is not eagerly loaded
#     )

#     # Custom `to_dict()` method that does not include the `prescriptions` relationship
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'ndc_id': self.ndc_id,
#             'name': self.name,
#             'description': self.description,
#             'dosage_form': self.dosage_form,
#             'strength': self.strength,
#         }


# # Prescription Model 
# class Prescription(db.Model):
#     __tablename__ = 'prescription'

#     id = db.Column(db.Integer, primary_key=True)
#     drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))  # Foreign key to Drug
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))  # Correct reference
#     pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'))  # Foreign key to Pharmacist
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of prescription
#     instructions = db.Column(db.String(255))  # Instructions for use
#     status = db.Column(db.String(50), default='pending')  # Status of prescription

#     # Relationships to link Prescription with other models
#     drug = db.relationship('Drug', back_populates='prescriptions')  # Link to Drug
#     patient = db.relationship('Patient')  # Link to Patient
#     pharmacist = db.relationship('Pharmacist')  # Link to Pharmacist 

#     # Define to_dict() Method
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "drug_id": self.drug_id,
#             "patient_id": self.patient_id,
#             "pharmacist_id": self.pharmacist_id,
#             "created_at": self.created_at,
#             "instructions": self.instructions,
#             "status": self.status,
#             # Include related data from relationships, if desired
#             "drug": self.drug.name if self.drug else None,
#             "patient": {
#                 "id": self.patient.id,
#                 "name": self.patient.name,
#             } if self.patient else None,
#             "pharmacist": {
#                 "id": self.pharmacist.id,
#                 "name": self.pharmacist.name,
#             } if self.pharmacist else None,
#         }

#     # serialize_rules
#     patient = db.relationship('Patient', back_populates='prescriptions')   # Relationship
#     serialize_rules = ('-patient',)  # Exclude patient during serialization of Prescription
# #----------------------------------------------------------------------------------------

# # Basket Model (Optional)
# class Basket(db.Model, SerializerMixin):
#     __tablename__ = 'basket'

#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
#     prescription_id = db.Column(db.Integer, db.ForeignKey('prescription.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False, default=1)
#     # Add a field for the status (e.g., added, removed, submitted)
#     status = db.Column(db.String(20), default='added')
#     # Consider adding a timestamp for when the prescription was added to the basket

#     patient = db.relationship("Patient")
#     prescription = db.relationship("Prescription")
#     serialize_rules = ['-patient.baskets', '-prescription.basket']


# Rewritten Model:
# Import necessary modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

# Patient Model
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

    prescriptions = db.relationship('Prescription', back_populates='patient')  # Relationship

# Pharmacist model
class Pharmacist(db.Model):
    __tablename__ = 'pharmacist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Pharmacist name
    pharmacy = db.Column(db.String(100))  # Pharmacy name or affiliation

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "pharmacy_name": self.pharmacy,
        }

# Drug Model
class Drug(db.Model):
    __tablename__ = 'drug'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    ndc_id = db.Column(db.String(10), nullable=False, unique=True)  # Unique NDC identifier
    name = db.Column(db.String(100), nullable=False)  # Drug name
    description = db.Column(db.String(255))  # Description
    dosage_form = db.Column(db.String(50))  # Form (tablet, capsule, etc.)
    strength = db.Column(db.String(50))  # Drug strength

    prescriptions = db.relationship('Prescription', back_populates='drug')  # Relationship

    def to_dict(self):
        return {
            'id': self.id,
            'ndc_id': self.ndc_id,
            'name': self.name,
            'description': self.description,
            'dosage_form': self.dosage_form,
            'strength': self.strength,
        }

# Prescription Model 
class Prescription(db.Model):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drug.id'))  # Foreign key to Drug
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))  # Foreign key to Patient
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'))  # Foreign key to Pharmacist
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of prescription
    instructions = db.Column(db.String(255))  # Instructions for use
    status = db.Column(db.String(50), default='pending')  # Status of prescription

    drug = db.relationship('Drug', back_populates='prescriptions')  # Link to Drug
    patient = db.relationship('Patient', back_populates='prescriptions')  # Link to Patient
    pharmacist = db.relationship('Pharmacist')  # Link to Pharmacist 

    def to_dict(self):
        return {
            "id": self.id,
            "drug_id": self.drug_id,
            "patient_id": self.patient_id,
            "pharmacist_id": self.pharmacist_id,
            "created_at": self.created_at,
            "instructions": self.instructions,
            "status": self.status,
            "drug": self.drug.to_dict(),
            "patient": self.patient.to_dict(),
            "pharmacist": self.pharmacist.to_dict(),
        }


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