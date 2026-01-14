import os
import json
from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    # Find the path to profile.json in the same folder as this app.py
    root_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(root_path, 'profile.json')
    
    with open(json_path, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    try:
        # STEP 1: Define the variable by calling the function
        profile_data = load_data() 
        
        # STEP 2: Now pass it to the template
        return render_template('index.html', profile=profile_data)
        
    except Exception as e:
        print(f"Error loading profile: {e}")
        return f"Internal Server Error: {e}", 500

# Required for Vercel
app = app