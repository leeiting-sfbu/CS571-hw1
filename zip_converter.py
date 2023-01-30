from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Weather Finder"

weather_info = {
    "10001": "Cloudy, 5 degree Celsius",
    "90001": "Sunny, 7 degree Celsius",
    "60601": "Snow, -10 degree Celsius"
}

@app.route('/weather', methods=['GET'])
def get_zip_code():
    zip_code = request.args.get('zip')
    weather = weather_info.get(zip_code, None)
    if weather:
        return f"Weather for {zip_code} is {weather}"
    else:
        return f"Weather for {zip_code} not found"

if __name__ == '__main__':
    app.run(debug=True)
