from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Route 1: Welcome/Health Check endpoint (returns JSON)
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to my tiny Flask backend server!",
        "timestamp": datetime.now().isoformat()
    })

# Route 2: Information endpoint (returns JSON)
@app.route('/api/info')
def info():
    return jsonify({
        "name": "Abhishek Choudhary",
        "role": "Backend Developer Intern",
        "skills": ["Python", "Flask", "Git"],
        "active": True
    })

if __name__ == '__main__':
    # Start the server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
