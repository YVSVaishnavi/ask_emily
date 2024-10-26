from flask import Blueprint, jsonify, request
import requests
from models import User, Campground, db
from flask_jwt_extended import create_access_token

api_bp = Blueprint('api', __name__)

#replace with your actual keys
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
WAZE_API_KEY = 'YOUR_WAZE_API_KEY'
CAMP_API_KEY = 'YOUR_CAMP_API_KEY'
RVTAA_API_URL = 'https://api.rvtaa.com/v1/technicians'

@api_bp.route('/campgrounds', methods=['GET'])
def get_campgrounds():
    location = request.args.get('location')
    preferences = request.args.get('preferences')
    api_url = f"https://api.campgroundapi.com/v1/campgrounds?location={location}&preferences={preferences}&apikey={CAMP_API_KEY}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch campground data"}), 500

@api_bp.route('/route', methods=['POST'])
def calculate_route():
    data = request.json
    start = data['start']
    destination = data['destination']
    rig_size = data['rig_size']
    
    # Google Maps routing example
    route_api_url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(route_api_url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch route data"}), 500

@api_bp.route('/technicians', methods=['GET'])
def find_technicians():
    location = request.args.get('location')
    issue = request.args.get('issue')
    
    response = requests.get(f"{RVTAA_API_URL}?location={location}&issue={issue}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch technician data"}), 500

@api_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    
    if user and user.password == password: 
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    return jsonify({"msg": "Bad username or password"}), 401
