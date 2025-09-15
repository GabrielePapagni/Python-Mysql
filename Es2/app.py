from flask import Flask
from flask import send_file
import random
import json

app = Flask(__name__)

with open('pokemon.json', 'r') as f:
    data = json.load(f)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/all")
def all():
    return send_file('pokemon.json')

@app.route("/random")
def random_pokemon():
    random_pokemon = data['pokemon'][random.randrange(0, len(data['pokemon']))]
    print(random_pokemon)
    return random_pokemon

if __name__ == "__main__":
    app.run(debug=True)