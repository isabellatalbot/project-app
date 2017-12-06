import os
import requests
from flask import Flask, render_template
id = "84600bca7507293656495e8972aec659"
app = Flask("BasicApp")

@app.route("/")
def index():
    payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':id}

    response = query_weather(payload)
    json_response = jsonify(response)
    return render_template("index.html", response=json_response)

def query_weather(payload):
	endpoint = 'http://api.openweathermap.org/data/2.5/weather'
	response = requests.get(endpoint, payload)
	return response

def jsonify(response):
	json_response = response.json()
	return json_response


#print(json_response['main']['temp'])
#print(json_response['name'])
#print(json_response['weather'][0]['main'])

if 'PORT' in os.environ:
	app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
	app.run(debug=True)