from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Zip Code Finder"

zip_codes = {
    "New York": "10001",
    "Los Angeles": "90001",
    "Chicago": "60601"
}

@app.route('/zipcode', methods=['GET'])
def get_zip_code():
    city = request.args.get('city')
    zip_code = zip_codes.get(city, None)
    if not zip_code:
        return f"Zip code for {city} not found"

    result = f"Zip code for {city} is {zip_code}\n"

    weather_response = requests.get(f'http://zip_converter:8000/weather?zip={zip_code}')

    result += f"Result returned from zip_converter: {weather_response.text}"
    return result


    
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
