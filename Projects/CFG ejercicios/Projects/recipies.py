import requests
import os
from dotenv import load_dotenv #using enviroment variable to protect sensitive data



load_dotenv()
ID = os.getenv('ID')
KEY = os.getenv('KEY')
def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = ID
    app_key = KEY
    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']
def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()
run()
