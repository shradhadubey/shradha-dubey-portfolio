import json
import os
from flask import Flask, render_template

app = Flask(__name__)

def load_profile():
    # Ensures data.json is found on Render's file system
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'data.json')
    with open(file_path, 'r') as f:
        return json.load(f)

@app.route('/')
def home():
    data = load_profile()
    return render_template('index.html', profile=data)

# No changes needed to the if __name__ block