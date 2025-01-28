# Crop Yield Prediction and Irrigation Optimization

## Project Description

This project leverages **Deep Learning** techniques to predict crop yields and optimize irrigation based on environmental variables and historical data. The approach aims to provide accurate insights to support decision-making in agribusiness, promoting more efficient and sustainable agricultural practices.

## Objectives

- **Crop Yield Prediction:** Anticipate agricultural productivity based on environmental and historical factors.
- **Irrigation Optimization:** Provide recommendations for efficient water usage, ensuring optimal crop growth and resource conservation.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** TensorFlow, Keras, Pandas, NumPy, Scikit-learn
- **Web Development:** Flask for creating RESTful APIs
- **Serialization Tools:** Joblib for serializing models and scalers

## Repository Structure

- `app.py`: Main script implementing the Flask API to serve the prediction model.
- `client.py`: Example script to consume the API and retrieve predictions.
- `dataset.csv`: Dataset used to train the model.
- `data_dictionary.xlsx`: Detailed dictionary of the variables in the dataset.
- `model.ipynb`: Jupyter Notebook containing the process for developing and training the Deep Learning model.
- `model_dsa.keras`: Serialized file of the trained model.
- `scaler.joblib`: Data scaler object to ensure consistency in predictions.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LucasBoden-da/Agribusiness.git
   cd Agribusiness
   ```

2. **Install Dependencies:**

   Make sure you have Python installed. Then, install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API:**

   Start the Flask server to make the prediction API available:

   ```bash
   python app.py
   ```

   The API will be available at `http://127.0.0.1:5000/`.

4. **Retrieve Predictions:**

   Use the `client.py` script or tools like Postman to send requests to the API and obtain crop yield predictions and irrigation recommendations.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For more information or collaboration inquiries:

- **Author:** Lucas Boden
- **Email:** lucashippertt@hotmail.com
- **LinkedIn:** [https://www.linkedin.com/in/lucas-stuart/](https://www.linkedin.com/in/lucas-stuart/) 