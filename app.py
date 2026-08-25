import steamspypi

from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session.clear()

        genre = request.form.get("genre")
        # Pull steam games informatiom 
        data_request = dict()
        data_request["request"] = "genre"
        data_request["genre"] = genre
        
        data = steamspypi.download(data_request)
        buffer_dict = {}
        games = []

        # Get name of games with request tag
        for element in data:
            buffer_dict.update(data[element])

            games.append(buffer_dict.copy())

        # Store the data goblally on session
        session["games"] = games

        return redirect("/game")
    else:
        return render_template("index.html")


@app.route("/game")
def game():
        # Distribute games with pagination system, improved perfomace.
        search=False
        games = session.get("games")

        page = request.args.get(get_page_parameter(),type=int, default=1)
        per_page = 10

        start = (page - 1) * per_page
        end = start + per_page
        pagination = Pagination(page=page, per_page=per_page, total=len(games), search=search, record_name="games")
        games= games[start:end]

        return render_template("game.html", games=games, pagination=pagination)


# Allows for seeing flask changes dinamically
# while using the python code debug method.
# DO NOT TOUCH
if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, debug=True)
