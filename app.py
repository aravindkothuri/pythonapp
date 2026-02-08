from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Python Application 🚀",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/api/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

