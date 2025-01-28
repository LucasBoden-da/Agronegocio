# Building API for Deep Learning Model Deployment
# Client

# Imports
import requests
import json

# API URL
url = 'http://127.0.0.1:5000/predict'

# Data to be sent as JSON
data = [
    {
        "vegetation_index": 354, 
        "soil_capacity": 684, 
        "co2_concentration": 3736.3, 
        "nutrient_level": 914.09, 
        "fertilizer_index": 849.78, 
        "root_depth": 412.37, 
        "solar_radiation": 889, 
        "precipitation": 49.81, 
        "growth_stage": 154.92254, 
        "yield_history": 245.3
    }
]

# Headers to define the content type as JSON
headers = {'Content-Type': 'application/json'}

# Makes the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Checks if the request was successful
if response.status_code == 200:
    print("\nAPI Response:", response.json())
    print("\n")
else:
    print("Request error:", response.status_code, response.text)