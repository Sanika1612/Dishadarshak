from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests
import json
app = Flask(__name__, static_url_path='/static')


app = Flask(__name__)
env_file = os.path.join(app.root_path, '.env')
load_dotenv()

# Replace this with your Mapbox API key
mapbox_access_token = os.getenv('MAPBOX_API_KEY')

@app.route('/')
def navigate():
    return render_template('home.html')


@app.route('/get_directions', methods=['POST'])
def get_directions():
    start = request.form.get('start')  # Get the user's current location from the form
    destination = request.form.get('destination')  # Get the destination from the form

    # Make a directions request using the Mapbox Directions API
    url = f'https://api.mapbox.com/directions/v5/mapbox/walking/{start};{destination}'
    params = {
        'access_token': mapbox_access_token
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        directions_data = response.json()
        return render_template('directions.html', directions=directions_data)
    else:
        return "Error fetching directions"
    



@app.route('/index')
def index():
    # Render the index.html page
    return render_template('index.html', mapbox_access_token=mapbox_access_token)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
