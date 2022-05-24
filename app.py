from flask import Flask
from data import jokes
import random

app = Flask(__name__)



@app.get("/")
def tell_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
