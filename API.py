from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Você Conectou a primeira rota da api, Continue !!")
    return "<p>Hello, World !</p>"



