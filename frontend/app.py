from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

HTML_PAGE = """
<html>
  <head><title>Frontend</title></head>
  <body>
    <h1>Frontend Service</h1>
    <p>Backend says: {{ message }}</p>
  </body>
</html>
"""

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000/api/data")

@app.route("/")
def home():
    try:
        res = requests.get(BACKEND_URL)
        message = res.json().get("message", "No response")
    except Exception as e:
        print(f"Backend not available: {e}")
        message = "Backend not available"
    
    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))  
    app.run(host="0.0.0.0", port=port)
