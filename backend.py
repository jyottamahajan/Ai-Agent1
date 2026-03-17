# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (list) for scholarships
scholarships_db = []

# GET endpoint - sab scholarships dekhne ke liye
@app.route("/api/scholarships", methods=["GET"])
def get_scholarships():
    return jsonify(scholarships_db), 200

# POST endpoint - scholarships add karne ke liye
@app.route("/api/scholarships", methods=["POST"])
def add_scholarship():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Invalid data"}), 400
    scholarships_db.append(data)
    return jsonify({"message": "Scholarship added"}), 201

if __name__ == "__main__":
    app.run(port=50001,debug=True)