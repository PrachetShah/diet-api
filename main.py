import requests
from flask import Flask
import time
import os

url = "https://api.spoonacular.com/mealplanner/generate"

API_KEY = os.environ.get("API_KEY")

params = {
    "timeFrame":"day",
    "diet":"vegetarian",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
response = response.json()

app = Flask(__name__)

@app.route('/')
def api():
    time.sleep(5)
    return response

if __name__ == '__main__':
    app.run()