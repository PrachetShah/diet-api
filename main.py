import requests
from flask import Flask
import time
import os

API_KEY = os.environ.get("API_KEY")


app = Flask(__name__)

@app.route('/')
def api():
    url = "https://api.spoonacular.com/mealplanner/generate"
    params = {
    "timeFrame":"day",
    "diet":"vegetarian",
    "apiKey": API_KEY
}

    response = requests.get(url, params=params)
    meals = response.json()
    # meals = {"meals":[{"id":715477,"imageType":"jpg","readyInMinutes":45,"servings":6,"sourceUrl":"https://spoonacular.com/the-best-lemon-bars-715477","title":"The BEST Lemon Bars"},{"id":558901,"imageType":"jpg","readyInMinutes":15,"servings":4,"sourceUrl":"https://www.fifteenspatulas.com/sesame-soba-noodles/","title":"Sesame Soba Noodles"},{"id":384435,"imageType":"jpg","readyInMinutes":40,"servings":12,"sourceUrl":"http://www.tasteofhome.com/Recipes/overnight-french-toast-2","title":"Overnight French Toast"}],"nutrients":{"calories":1845.82,"carbohydrates":298.28,"fat":57.83,"protein":46.34}}
    IDs = []
    for meal in meals["meals"]:
        id = meal["id"]
        IDs.append(id)
    
    summary = []
    for id in IDs:
        response = requests.get(f"https://api.spoonacular.com/recipes/{id}/summary?apiKey=349b154cdf38413c952e2d9bf96c41ff")
        response = response.json()
        summary.append(response)

    output = {"meals":meals, "summary":summary}
    return output

if __name__ == '__main__':
    app.run()