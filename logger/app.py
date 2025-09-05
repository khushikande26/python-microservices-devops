from flask import Flask, request, jsonify

app = Flask(__name__)
LOG_FILE = "logs.txt"

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    with open(LOG_FILE, "a") as f:
        f.write(str(data) + "\n")
    return {"status": "logged"}, 200
    
@app.route("/log", methods=["GET"])
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        logs = []
    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
