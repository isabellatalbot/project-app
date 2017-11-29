import os

from flask import Flask, render_template

app = Flask("BasicApp")

@app.route("/")
def index():
    return render_template("index.html")

if 'PORT' in os.environ:
	app.run(host='0.0.0.0', port=int(os.environ[PORT]))
else:
	app.run(debug=True)