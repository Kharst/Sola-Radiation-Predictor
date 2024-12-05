🌞 Solar Energy Predictor


📖 Overview
The Solar Energy Predictor is a Flask-based web application powered by a Machine Learning model (Random Forest). It predicts solar radiation (kWh/m²) based on environmental features like solar irradiance, cloud cover, and more. This tool is ideal for exploring renewable energy potential or aiding solar energy projects.

⚡ Features
Accepts user inputs like latitude, longitude, and weather parameters.
Predicts solar radiation (kWh/m²) using a trained ML model.
Simple and interactive interface for ease of use.
REST API for predictions with JSON requests.


🛠️ Tech Stack
Python: Backend programming and model training.
Flask: Web framework for the app.
scikit-learn: Used to train the Random Forest model.
HTML & CSS: For a user-friendly front end.


🚀 How It Works
The user enters environmental data (like solar irradiance, cloud cover, etc.) through the form.
These inputs are processed by the Flask app and sent to the trained Random Forest model.
The model predicts solar radiation and displays the results.


📋 Input Features
The model uses the following inputs to make predictions:

Solar Irradiance 1
Solar Irradiance 2
Clear Sky Radiation
Cloud Cover
Precipitation
Wind Speed
Latitude
Longitude


📦 Installation
Clone this repository:

bash

git clone https://github.com/<your-username>/solar-energy-predictor.git  
Navigate to the project folder:

bash
cd solar-energy-predictor  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Run the app:

bash
python app.py  
Open your browser and go to:

arduino
http://127.0.0.1:5000  


📤 API Endpoint
You can also use the REST API to make predictions:

Endpoint: /predict
Method: POST
JSON Input Format:
json
Copy code
{  
    "features": {  
        "Solar_Irradiance_1": 800,  
        "Solar_Irradiance_2": 600,  
        "Clear_Sky_Radiation": 200,  
        "Precipitation": 5,  
        "Wind_Speed": 10,  
        "Latitude": -25.0,  
        "Cloud_Cover": 0.3,  
        "Longitude": 28.0  
    }  
}  


🖼️ Example Prediction
Input:

json
Copy code
{  
    "features": {  
        "Solar_Irradiance_1": 800,  
        "Solar_Irradiance_2": 600,  
        "Clear_Sky_Radiation": 200,  
        "Precipitation": 5,  
        "Wind_Speed": 10,  
        "Latitude": -25.0,  
        "Cloud_Cover": 0.3,  
        "Longitude": 28.0  
    }  
}  
Output:

json
Copy code
{  
    "Predicted Solar Radiation (kWh/m²)": 8.72  
}  


🤝 Contributing
Feel free to fork this repository, make updates, and submit pull requests.


📧 Contact
Author: Reuben Siwela

Email: reubensiwela@gmail.com
LinkedIn: Reuben Siwela


📜 License
This project is licensed under the MIT License.
