from flask import Flask

app = Flask(__name__)  # Flask("main.py")

@app.route("/") #/ - ishodišna ruta; 127.0.0.1:5000 - localhost
#flask radi na principu da definiramo URL rutu, na kojoj se onda poziva nekakva funkcija
def hello_world():
    return "<p>Hello world</p>"