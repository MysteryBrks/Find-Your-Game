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
    genres_available = ("Adventure", "Action", "Strategy")
    tags_available = ("2D", "3D", "Controller", "Relaxing", "Funny",
                       "Anime", "Multiple Endings", "Choices Matter")
    
    if request.method == "POST":
        session.clear()

        genres = request.form.getlist("genres")
        # Pull steam games by genres
        data_request = dict()
        data_request["request"] = "genre"
        buffer= {}
        data = {}
        games = []

        # Takes the firt genre selected
        data_request["genre"] = genres[0]
        data = steamspypi.download(data_request)
        # Proceeds to compare to every other genre,
        # if appid isn't in ALL selected genres, it's
        # removed from data.
        for genre in genres[1:]:    
            data_request["genre"] = genre
            buffer = steamspypi.download(data_request)
            data_buffer = data.copy()

            for key in data_buffer: 
                if key not in buffer:
                    data.pop(key, None)

        data_request.clear()
        # Pulls steam games by tags
        tags = request.form.getlist("tags")
        data_request["request"] = "tag"

        for tag in tags:
             data_request["tag"] = tag
             buffer = steamspypi.download(data_request)
             data_buffer = data.copy()

             for key in data_buffer:
                  if key not in buffer:
                       data.pop(key, None)

        for game in data:
             games.append(game)

        # Store the data globally on session
        session["games"] = games

        return redirect("/game")
    else:
        return render_template("index.html", genres=genres_available, tags=tags_available)


@app.route("/game")
def game():
        # Distribute games with pagination system, improved perfomace.
        search=False
        games = session.get("games")

        page = request.args.get(get_page_parameter(),type=int, default=1)
        per_page = 15

        start = (page - 1) * per_page
        end = start + per_page
        pagination = Pagination(page=page, per_page=per_page, total=len(games),
                                 search=search, record_name="games")
        games= games[start:end]

        return render_template("game.html", games=games, pagination=pagination)


# Allows for seeing flask changes dinamically
# while using the python code debug method.
# DO NOT TOUCH
if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, debug=True)
