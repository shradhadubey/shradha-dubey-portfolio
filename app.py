import os
import json
import profile
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
    
@app.route("/services")
def services():
    return render_template("services.html", profile=profile)

@app.route("/hire")
def hire():
    return render_template("hire.html", profile=profile)

import sqlite3
from flask import request, redirect, url_for

@app.route("/inquiry", methods=["POST"])
def inquiry():
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            company TEXT,
            project TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO leads (name, email, company, project)
        VALUES (?, ?, ?, ?)
    """, (
        request.form["name"],
        request.form["email"],
        request.form.get("company"),
        request.form["project"]
    ))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

# Required for Vercel
app = app