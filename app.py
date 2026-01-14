from flask import Flask, render_template
import json

app = Flask(__name__)

# This is required for Vercel to find the "app" object
app = app 

@app.route('/')
def index():
    # ... your existing logic ...
    return render_template('index.html', profile=profile_data)

# Only for local testing; Vercel ignores this
if __name__ == "__main__":
    app.run()