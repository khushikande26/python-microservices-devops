from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

LOGGER_URL = os.getenv("LOGGER_URL", "http://127.0.0.1:5002/log")

@app.route("/api/data", methods=["GET"])
def get_data():
   
    response = {"message": "Hello from Backend"}

    try:
        requests.post(LOGGER_URL, json={"endpoint": "/api/data"})
    except Exception as e:
        print(f"Logger service not available: {e}")

    return jsonify(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000")) 
    app.run(host="0.0.0.0", port=port)
