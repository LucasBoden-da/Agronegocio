# Building API for Deep Learning Model Deployment
# API

# Imports
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import joblib
import traceback
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
import warnings
warnings.filterwarnings('ignore')

# Load the model and scaler with error handling
try:
    final_model = tf.keras.models.load_model('model.keras')
    final_scaler = joblib.load('scaler.joblib')
except Exception as e:
    print("Error loading the model or scaler:", e)
    traceback.print_exc()
    final_model = None
    final_scaler = None

# Create the app
app = Flask(__name__)

# Create the prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Attempt to execute the code block
    try:

        # Get the data from the request as JSON
        data = request.get_json(force=True)

        # Check if data was provided
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Check if the model and scaler are loaded correctly
        if not final_model or not final_scaler:
            return jsonify({"error": "Model or scaler not loaded correctly"}), 500

        # Prepare the input data as a NumPy array
        data = np.array([list(d.values()) for d in data])

        # Scale the input data
        data_scaled = final_scaler.transform(data)

        # Perform the prediction using the model
        prediction = final_model.predict(data_scaled)

        # Convert the prediction to list format
        prediction_as_list = prediction.flatten().tolist()

        # Return the prediction as JSON
        return jsonify(soil_moisture_prediction=prediction_as_list)

    # Catch any exception during prediction
    except Exception as e:
        
        # Print the error to the console
        print("Error during prediction:", e)
        
        # Print the traceback to the console
        traceback.print_exc()
        
        # Return an error as JSON
        return jsonify({"error": "Error during prediction", "message": str(e)}), 500

# Main block and app execution
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print("Error starting the server:", e)
        traceback.print_exc()
