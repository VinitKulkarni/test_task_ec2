from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import pymongo

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.usersDB
collection = db['users-collection']

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid data"}), 400

    collection.insert_one({
        "username": data["username"],
        "password": data["password"]
    })

    return jsonify({"message": "User data stored successfully"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
