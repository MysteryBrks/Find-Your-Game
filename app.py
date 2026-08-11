import steamspypi

from flask import Flask, render_template

app = Flask(__name__)

# Pull steam games informatiom 
data_request = dict()
data_request['request'] = 'tag'
data_request['tag'] = "Dystopian"

data = steamspypi.download(data_request)
print(data)


@app.route("/")
def index():
    return render_template("index.html")