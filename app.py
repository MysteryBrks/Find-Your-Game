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
    genres_available = ("Adventure", "Action", "Strategy", "Indie","Casual", "Simulation",
                         "RPG", "Free to Play", "Early Acess", "Sports",
                           "Racing", "Massively Multiplayer")
    
    tags_available = ("2D", "3D", "Controller", "Relaxing", "Funny", "Singleplayer"
                       "Anime", "Multiple Endings", "Choices Matter", "Atmospheric",
                       "Story Rich", "Fantasy", "Multiplayer", "Cute", "Exploration",
                       "Pixel Graphics", "Combat", "First-Person", "Puzzle", "Stylized",
                       "Arcade", "PvE", "Horror", "Sci-fi", "Third Person", "Top-Down",
                       "Retro", "Family Friendly", "Violent", "Shooter", "Female Protagonist",
                       "Dark", "PvP", "Sexual Content", "Realistic", "Mystery", "Online Co-Op",
                       "Linear", "Open World", "Survival", "Physics", "Cartoony", "Visual Novel",
                       "Psychologial Horror", "Platformer", "Gore", "Roguelike", "Magic", "Roguelite",
                       "Sandbox", "Management", "Tactical", "Medieval", "Hand-drawn", "FPS",
                       "Immersive Sim", "Crafting", "Building", "Futuristic",
                       "Point & Click", "Dark Fantasy", "Emotional", "Procedural Generation", "Space",
                       "Difficult", "Romance", "Choose Your Own Adventure", "Nature", "Logic", 
                       "Survival Horror", "Hentai", "Base Building", "Hack and Slash", "Dating Sim",
                       "Bullet Hell", "Post-apocalyptic", "Side Scroller", "VR", "Dungeon Crawler",
                       "Walking Simulator", "Life Sim", "Economy", "Cinematic", "Card Game", "Tabletop",
                       "Dialogue Heavy", "Text-Based", "War", "Idler", "Psychologial", "Stealth", 
                       "Zombies", "JRPG", "LGBTQ+", "Local Co-Op", "Historical", "Thriller", "2.5D",
                       "Isometric", "Military", "Replay Value", "Turn-Based", "Demons", "Alien", 
                       "Cyberpunk", "Cozy", "Detective", "Robots", "Dystopian", "RTS", "CRPG", "Board Game",
                       "Souls-like", "Capitalism", "Cats", "Destruction", "Parkour", "Moddable",
                       "Metroidvania", "Party Game", "Cooking", "Farming Sim", "Competitive", "Rhythm",
                       "Fighting", "MMORPG", "Noir", "Colony Sim", "Space Sim", "Grand Strategy",
                       "Looter Shooter", "Narrative", "Classic", "Battle Royale", "Split Screen", "Fishing",
                       "World War II", "Gambling", "Dogs", "Hero Shooter", "Voxel", "Immersive",
                       "Time Travel", "Vampires", "Pirates", "Steampunk", "Political Sim", "Hunting",
                       "MOBA", "Diplomacy", "Western", "Cold War", "Naval Combat", "Escape Room",
                       "Villain Protagonist", "Werewolves", "World War I", "Outbreak Sim", "Dwarves",
                       "Spaceships", "Social Deduction", "Medical Sim", "Dice", "Vikings",
                       "Silent Protagonist", "Espionage", "Poker", "Tanks", "Minigames", "FMV")
    
    if request.method == "POST":
        session.clear()

        genres = request.form.getlist("genres")
        tags = request.form.getlist("tags")
        excludeds = request.form.getlist("excludeds")
        # User input validation
        if not tags:
            return redirect("/")

        # Pull steam games by genres
        data_request = dict()
        data_request["request"] = "genre"
        buffer= {}
        data = {}
        games = []

        if genres:
            # Takes the first genre selected
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

            data_request["request"] = "tag"
            for tag in tags:
                data_request["tag"] = tag
                buffer = steamspypi.download(data_request)
                data_buffer = data.copy()

                for key in data_buffer:
                    if key not in buffer:
                        data.pop(key, None)
        else:
            data_request["request"] = "tag"
            data_request["tag"] = tags[0]
            data = steamspypi.download(data_request)

            for tag in tags[1:]:
                data_request["tag"] = tag
                buffer = steamspypi.download(data_request)
                data_buffer = data.copy()

                for key in data_buffer:
                    if key not in buffer:
                        data.pop(key, None)

        if excludeds:
            for excluded in excludeds:
                data_request["tag"] = excluded
                buffer = steamspypi.download(data_request)
                data_buffer = data.copy()

                for key in data_buffer:
                    if key in buffer:
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


@app.route("/manual")
def manual():
    return render_template("manual.html")

# Allows for seeing flask changes dinamically
# while using the python code debug method.
# DO NOT TOUCH
if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, debug=True)
