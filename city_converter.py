from flask import Flask, request

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
    if zip_code:
        return f"Zip code for {city} is {zip_code}"
    else:
        return f"Zip code for {city} not found"
        
if __name__ == '__main__':
    app.run(debug=True)
