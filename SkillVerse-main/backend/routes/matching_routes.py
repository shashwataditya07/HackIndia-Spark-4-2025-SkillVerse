from flask import Blueprint, jsonify
from database.db import connect_db
from models.organ_matching import ai_match_donor

matching_bp = Blueprint("matching_bp", __name__)

@matching_bp.route("/match", methods=["GET"])
def match_donors():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    cursor.execute("SELECT * FROM recipients")
    recipients = cursor.fetchall()

    matched_data = []
    for donor in donors:
        matches = ai_match_donor({
            "blood_type": donor[2], "organ": donor[3]
        }, recipients)

        if matches:
            matched_data.append({"donor": donor, "matches": matches})

    cursor.close()
    conn.close()
    
    return jsonify(matched_data)
