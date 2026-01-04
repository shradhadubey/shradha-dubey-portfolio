import json
from flask import Flask, render_template

app = Flask(__name__)

def load_profile():
    with open('data.json', 'r') as f:
        return json.load(f)

@app.route('/')
def home():
    data = load_profile()
    return render_template('index.html', profile=data)

if __name__ == '__main__':
    app.run(debug=True)