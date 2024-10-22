from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('solar_energy_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the HTML template for the form
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Solar Energy Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
        }
        h2 {
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        label {
            font-weight: bold;
            margin-top: 10px;
            display: block;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 8px;
            margin: 5px 0 20px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #f9f9f9;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Reuben's Solar Radiation Predictor </h2>
        <form action="/" method="POST">
            <label for="latitude">Latitude:</label>
            <input type="number" step="any" id="latitude" name="latitude" required>

            <label for="longitude">Longitude:</label>
            <input type="number" step="any" id="longitude" name="longitude" required>

            <label for="irradiance1">Solar Irradiance 1:</label>
            <input type="number" step="any" id="irradiance1" name="irradiance1" required>

            <label for="irradiance2">Solar Irradiance 2:</label>
            <input type="number" step="any" id="irradiance2" name="irradiance2" required>

            <label for="clear_sky_radiation">Clear Sky Radiation:</label>
            <input type="number" step="any" id="clear_sky_radiation" name="clear_sky_radiation" required>

            <label for="cloud_cover">Cloud Cover:</label>
            <input type="number" step="any" id="cloud_cover" name="cloud_cover" required>

            <label for="precipitation">Precipitation:</label>
            <input type="number" step="any" id="precipitation" name="precipitation" required>

            <label for="wind_speed">Wind Speed:</label>
            <input type="number" step="any" id="wind_speed" name="wind_speed" required>

            <input type="submit" value="Predict Solar Radiation">
        </form>

        {% if prediction %}
        <div class="result">
            <h3>Predicted Solar Radiation: {{ prediction }} kWh/m²</h3>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

# Define a route for the form (Home page)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the form data
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        irradiance1 = float(request.form['irradiance1'])
        irradiance2 = float(request.form['irradiance2'])
        clear_sky_radiation = float(request.form['clear_sky_radiation'])
        cloud_cover = float(request.form['cloud_cover'])
        precipitation = float(request.form['precipitation'])
        wind_speed = float(request.form['wind_speed'])

        # Create an array with the features in the correct order
        features = np.array([[latitude, longitude, irradiance1, irradiance2, clear_sky_radiation, cloud_cover, precipitation, wind_speed]])

        # Predict the solar radiation
        prediction = model.predict(features)[0]

        # Render the form again with the prediction displayed
        return render_template_string(html_template, prediction=prediction)

    return render_template_string(html_template)

# Define a route for JSON prediction (for API clients like Postman)
@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()  # Expecting JSON input
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]  # Predict using the loaded model
        return jsonify({'Predicted Solar Radiation (kWh/m²)': prediction})
    else:
        return jsonify({'error': 'Invalid Content-Type, please provide JSON'}), 415

if __name__ == '__main__':
    app.run(debug=True)
