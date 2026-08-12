import steamspypi

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tags = request.form.get("tags")
        # Pull steam games informatiom 
        data_request = dict()
        data_request['request'] = 'tag'
        data_request['tag'] = tags
        data = steamspypi.download(data_request)
        games = list()

        for elements in data:
            for info in elements:
                games.append(info)

        return render_template("game.html", game=games)
    else:
        return render_template("index.html")

# Allows for seeing flask changes dinamically
# while using the python code debug method.
# DO NOT TOUCH
if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, debug=True)
