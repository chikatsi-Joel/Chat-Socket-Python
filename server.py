from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "name" : "Joel",
        'age' : 23
    }
    return jsonify(data)


@app.route("/take", methods = ['GET'])
def take():
    data = request.form
    print(f'Name : {data['name']}')
    return 'ok'
    


app.run(host='127.0.0.1', port= 5000)  
