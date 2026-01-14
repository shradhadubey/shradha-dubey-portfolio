import os
import json
from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    # Look for profile.json in the same folder as app.py
    root_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(root_path, 'profile.json') # Removed 'data'
    
    with open(json_path, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    try:
        profile_data = load_data()
        return render_template('index.html', profile=profile_data)
    except Exception as e:
        print(f"Error: {e}")
        return "Check Logs", 500