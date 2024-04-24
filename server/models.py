#Setting up Models
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


db = SQLAlchemy()
bcrypt = Bcrypt()

#Models 

class UserAuth(db.Model, SerializerMixin):
    __tablename__ = 'userAuth'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) # cannot be null Enusuring Unique username
    password = db.Column(db.String(100), nullable=False) # cannot be null storing password HASH
    role = db.Column(db.String(20), nullable=False) #Role: patient or pharamcist

    #Setting Password with bcyrpt
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')  # Hash and decode to store as a string

    #Checking password with bycrypt
    def check_password(self, password):
        return bycrypt.check_password_hash(self.password_hash, password) # verify the given password

#Patient Model
class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_auth.id'), nullable=False)      
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100)) # optional, add valadations for numbers
    insurance = db.Column(db.String(60)) # A drop-down menu of preExiting insurance, and other 

# Relationship with UserAuth
    user = db.relationship('UserAuth', backref='patient') #Backref to UserAuth

#Pharmacist Model
class Pharmacist(db.Model, SerializerMixin):
    __tablename__ = 'pharamcist'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeginKey('user_auth.id'), nullable=False) #add Foregin Key to user
    name = db.Column(db.String(100), nullable=False)
    pharmacy = db.Column(db.String(100), nullable=False)

    #Relationship with UserAuth
    user = db.realtionship('UserAuth', backref='pharmacist') #Backref to UserAuth

#Prescription Model
class Prescription(db.Model, SerializerMixin):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)  # Foreign Key to Patient
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('pharmacist.id'), nullable=False)  # Foreign Key to Pharmacist
    medication_name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(100), nullable=False)  # Using string to accommodate different dosage formats
    instructions = db.Column(db.String(255))  # Optional instructions
    status = db.Column(db.String(20), nullable=False)  # Status: "pending", "approved", etc.

    # Relationships with Patient and Pharmacist
    patient = db.relationship('Patient', backref='prescriptions')  # Backref to Patient
    pharmacist = db.relationship('Pharmacist', backref='prescriptions')  # Backref to Pharmacist


# Basket Model
class Basket(db.Model, SerializerMixin):
    __tablename__ = 'basket'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)  # Foreign Key to Patient
    prescription_id = db.Column(db.Integer, db.ForeignKey('prescription.id'), nullable=False)  # Foreign Key to Prescription
    quantity = db.Column(db.Integer, nullable=False, default=1)  # Quantity of medication
    status = db.Column(db.String(20), default='pending')  # Status: "pending", "approved", "ordered", etc.

    # Relationships with Patient and Prescription
    patient = db.relationship('Patient', backref='baskets')  # Backref to Patient
    prescription = db.relationship('Prescription', backref='baskets')  # Backref to Prescription
