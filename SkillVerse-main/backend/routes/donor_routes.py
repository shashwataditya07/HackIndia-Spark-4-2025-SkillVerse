from flask import Blueprint, request, jsonify
from database.db import connect_db

donor_bp = Blueprint("donor_bp", __name__)

# Register a new donor
@donor_bp.route("/register_donor", methods=["POST"])
def register_donor():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO donors (name, email, blood_type, organ, location) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (data["name"], data["email"], data["blood_type"], data["organ"], data["location"]))

    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Donor registered successfully"}), 201

# Get all donors
@donor_bp.route("/get_donors", methods=["GET"])
def get_donors():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return jsonify(donors)
