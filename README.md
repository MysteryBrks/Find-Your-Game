# Find Your Game
#### Video Demo:  <URL HERE>
#### Description:
Find Your Game is a web application in flask made with the intent of searching and filtering games based on Steam library data. The application's main function envolves around allowing the user giving some searching criteria like the amount of copies sold, Steam tags, genres, and it's even possible to exclude undesired tags.

**Packages and plugin:**
*jQuery* - Needed for Select2 plugin
*Select2* - Used for a much more user friendly <select> tag of multiple options
*flask-paginate* - Facilitate dynamic pagination of game.html
*steamspypi* - Database collection of steampy API

<ins>layout.html</ins> - This is the layout used for all html templates, it contains necessary details for all html page like a basic navbar for returning to the index.html page 

<ins>index.html</ins> - Index.html is the main page of the application, has the important purpose of welcoming the user and it's input, wich afterwards is transfered to gamer.html.
This page cointains as already said, some input spaces for desired tags (minimal of 1 selected), genres (any amount, even none), excluded tags (any amount) and a range of amount of copies/owners.

Steam **tags** are very comprehensive, ranging from _farming sim_ to _gore_. Because of that, the user is expected to use it by your own discretion, acknowledging the use of too many tags may cause the result of no games found, or if too few tags may cause the contrary, a lot of games found. The use of tags is obligatory and it's considered the main feature of the application searching capabilities.

Steam **genres** are very much less comprehensive than tags, it's only limited to basic terms: Strategy, indie, casual and a few others... It's use is optional 
