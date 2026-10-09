# Find Your Game

#### Video Demo:  <URL HERE>

#### Description:

Find Your Game is a web application in Flask made with the intent of searching and filtering games based on Steam library data. The application's main function revolves around allowing the user to give some searching criteria, like the amount of copies sold, Steam tags, and genres, and even to exclude undesired tags. This web application has a philosophy of allowing and even incentivizing exploration of its features since your base intent is for the discovery of unknown Steam games.

##

#### Packages and plugin:

jQuery - Needed for Select2 plugin

Select2 - Used for a much more user-friendly tag of multiple options

flask-paginate - Facilitate dynamic pagination of game.html

steamspypi - Database collection of steampy API

##

#### Files:

[layout.html](templates/layout.html) - This is the layout used for all html templates, it contains necessary details for all html pages like a basic navbar allowing the user a way of returning to the index.html page. It also contains links importing Bootstrap, jQuery, and the Select2 plugin, and a CSS style file. 

[index.html](templates/index.html) - Index.html is the main page of the application and has the important purpose of welcoming the user and its input, which afterwards is transferred to gamer.html.

This page contains, as already said, some input spaces for desired tags (minimal of 1 selected), genres (any amount, even none), excluded tags (any amount), and a range of amounts of copies/owners.

Steam tags are very comprehensive, ranging from farming sim to gore. Because of that, the user is expected to use it by your own discretion, acknowledging that the use of too many tags may cause the result of no games found, or if too few tags, may cause the contrary, a lot of games found. The use of tags is obligatory, and it's considered the main feature of the application's searching capabilities.

Steam genres are very much less comprehensive than tags; they're only limited to basic terms: Strategy, indie, casual, etc. Its use is optional.

Excluded tags are a way of searching for a range of games while excluding another undesired range of games, undesired ones. For example, the user might search for "diplomacy" tagged games that aren't World War II themed. In this case he should still use the diplomacy tag but at the same time insert "World War II" in the excluded tags category.

Range of copies/owners is intended to filter games by the number of copies sold or, if it's free, the number of owners. The overall range varies from 50 million copies to 0 copies, but because of the way steamspypi is designed, this was divided into some subranges. Just like excluded tags and genres, its use is entirely optional, and the search is trusted to the user's volition.

[games.html](templates/games.html) - Shows a list containing all games based on the filters applied by the user. The games are displayed from top to bottom on Steam widgets, which the user may click to be redirected to the game's official Steam page. An essential feature of this page is the dynamic pagination made possible by the flask-paginate library, it creates more pages according to the amount of games. In analysis, this html is quite simple as a browsing-scrolling page without a search bar. It was considered during the project to develop a search bar for specific games, but despite sounding useful at first, it doesn't correspond with the application intention, which is blind exploration. 

OBSERVATION: It's common, especially on a wide range of search, to show widgets not correctly loaded with an error message. In such cases, it is advised to click on the Steam logo on the right bottom corner just outside the widget to counter this error. This problem is from the Steam embedding system in the creation of a game widget. 

[app.py](app.py) - Python Flask application, central pillar of the project. It contains data for the index page, validates user input, and makes possible GET and POST methods across pages. Stores flask session data of the user for more friendly navigation and also functionality of the app (to save games data across index.html and gs.html). The user's input, for example, is saved even after being redirected to the games page.

[dropdown.js](static/dropdown.js) - Contains basic jQuery with the Select2 plugin responsible for making the select html tag of multiple-choice more like dropdown menus, much more user-friendly. Very important to the application since it's necessary to accept multiple tags as a list input.

[style.css](static/styles.css) - Main CSS stylesheet file. It has very basic CSS code and stylization, mostly colors, the size of things, and the positioning of elements.

[index.css](static/index.css)—A stylesheet made only for index.html because of needed changes in Select2 default style. Dedicated to fitting more in the website aesthetics of dark blue.
