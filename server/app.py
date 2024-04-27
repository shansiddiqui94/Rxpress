from flask import Flask, jsonify
import os
from flask_migrate import Migrate;
from models import db

from models import UserAuth, Patient, Pharmacist, Prescription, Basket

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)



@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    # check that user exists
    user = UserAuth.query.filter(UserAuth.username == json_data.get('username')).first()
    if not user:
        return {'error': 'user not found'}, 404
    
    # check the user's password
    if not user.authenticate(json_data.get('password')):
        return {'error': 'login failed'}, 401
    
    # store a cookie in the browser
    session['user_id'] = user.id

    # return a response
    return user.to_dict(), 200

# logout
@app.route('/logout', methods=['DELETE'])
def logout():
    # delete the user_id cookie
    session.pop('user_id', None)
    return {}, 204

#signup
@app.route('/signup', method=['POST'])
def signup():
    #get JSON data
    json_data = request.get_json()

    user = UserAuth.query.filter(UserAuth.username == json_data.get('username')).first()

    if user:
        return {'error': 'User Already Exists'}, 400

    #create a new user
    new_user = UserAuth(
        username=json_data.get('username'),
        password=json_data.get('password'),
    )

    #add to DB
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict(), 201

#Check session (is user currently logged in?)
@app.route('/check_session', methods=['GET']) 
def check_session():
    #get user id from browser cookie
    user_id = session.get('user_id')
    # query the db to make sure that user id is valid
    user = UserAuth.query.filter(UserAuth.id == user_id).first()
     # if the user isn't valid, send error
    if not user:
        return {'error': 'unauthorized'}, 401
    else:
        return user.to_dict(), 200

# Prescription Routes: 
@app.route('/prescriptions', methods=['GET'])
def get_rx():
    try:
        # Fetch all prescriptions
        prescriptions = Prescription.query.all()

        # Serialize the prescriptions, applying rules to exclude certain fields
        serialized_prescriptions = [
            prescription.to_dict(rules=['-patient_id', '-pharmacist_id', '-status'])
            for prescription in prescriptions
        ]

        return jsonify(serialized_prescriptions), 200

    except ValueError as ve:
        # Handle specific ValueError
        return jsonify({"error": f"Value error: {str(ve)}"}), 400


@app.route('/prescriptions/<int:id>', methods=['GET'])









if __name__ == "__main__": #starting server 
    app.run(port=5555, debug=True)