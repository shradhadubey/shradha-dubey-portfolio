import json
import os
from datetime import datetime

def validate_data():
    try:
        with open('profile.json', 'r') as f:
            data = json.load(f)
        
        # Simple quality checks
        required_keys = ['name', 'role', 'experience']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing key: {key}")
        
        # Log the success
        with open('data_health_log.txt', 'a') as log:
            log.write(f"Health Check PASSED at {datetime.now()}\n")
        print("Data is healthy!")
        
    except Exception as e:
        print(f"Data Quality Error: {e}")
        exit(1)

if __name__ == "__main__":
    validate_data()