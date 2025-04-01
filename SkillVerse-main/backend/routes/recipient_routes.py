from flask import Blueprint, request, jsonify
from database.db import connect_db

recipient_bp = Blueprint("recipient_bp", __name__)

# Register a new recipient
@recipient_bp.route("/register_recipient", methods=["POST"])
def register_recipient():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO recipients (name, email, blood_type, organ, location) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (data["name"], data["email"], data["blood_type"], data["organ"], data["location"]))

    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Recipient registered successfully"}), 201

# Get all recipients
@recipient_bp.route("/get_recipients", methods=["GET"])
def get_recipients():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipients")
    recipients = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return jsonify(recipients)
