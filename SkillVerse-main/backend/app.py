from flask import Flask
from flask_cors import CORS
from routes.donor_routes import donor_bp
from routes.recipient_routes import recipient_bp
from routes.matching_routes import matching_bp
from database.db import create_tables

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Register blueprints
app.register_blueprint(donor_bp, url_prefix="/donors")
app.register_blueprint(recipient_bp, url_prefix="/recipients")
app.register_blueprint(matching_bp, url_prefix="/matching")

# Ensure tables are created on startup
create_tables()

@app.route("/", methods=["GET"])
def home():
    return {"message": "Organ Matching API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
