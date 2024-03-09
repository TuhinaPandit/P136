from flask import Flask, jsonify, request
from data import data

#data.py has the data of planets
#initialising app 
app = Flask(__name__)

#home screen
@app.route("/")
def home ():
    return jsonify({
        "data" : data, #assigned data to key
        "message" : "success"
    })

#stars
@app.route("/")
def stars ():
    star_name = request.args.get("name") #getting name of star from url 
    star_data = next(item for item in data if item["name"] == star_name) 
    return jsonify({
        "data" : star_data,
        "message" : "success"
    })
app.run()
