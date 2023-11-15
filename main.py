from flask import Flask
from flask.json import jsonify
app = Flask(__name__)  # Flask("main.py")

dict_primjer = {
    "ime": "Marko",
    "Prezime": "Markic",
    "Email" : "marko@asd"
}

@app.route("/") #/ - ishodišna ruta; 127.0.0.1:5000 - localhost
#flask radi na principu da definiramo URL rutu, na kojoj se onda poziva nekakva funkcija
@app.route("/")
def home():
    return "<h1><a href='/about'>Home page</a></h1>"

@app.route("/about")
def about():
    return "<p>About page</p>"

@app.route("/user/<username>")
def user(username):
    return f"<h3>User page for: {username}</h3>"

@app.route("/json")
def json():
    dict_primjer = {
        "ime": "Marko",
        "Prezime": "Markic",
        "Email" : "marko@asd"
    }

    return jsonify (dict_primjer)


@app.route("/json/<key>")
def jason_value(key):
    return dict_primjer.get(key, "unknown key")