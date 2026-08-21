import steamspypi

from flask import Flask, render_template, request, redirect, session
from flask_session import Session

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
        data_request['request'] = 'top100forever'
        
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
        page = request.args.get("page", 1, type=int)
        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page
        games = session.get("games")
        total_pages = (len(games) + per_page - 1) // per_page

        games = games[start:end]

        return render_template("game.html", games=games, page=page, total_pages=total_pages)


# Allows for seeing flask changes dinamically
# while using the python code debug method.
# DO NOT TOUCH
if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, debug=True)
