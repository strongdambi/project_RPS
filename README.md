# project RPS

### Project discription
This project is a rock-paper-scissors game web application. Users can select rock, paper, or scissors to play against the computer. The results are saved in a database and users can view the game results with the count of wins, losses, and draws.


### Installation
* python -m venv vevn
* pip install Flask Flask-SQLAlchemy


### Skills
* Python 3.10
  * Flask
  * Flask-SQLAlchemy 3.1.1
  * SQLAlchemy 2.0.31
  * render_template
  * request
* HTML
  * Bootstrap
  * CSS
* DB
  * SQLite


### Main feature
1. Play game: Users can select one of the rock-paper-sissors and check the computer's choice and the game result.
2. Store result: Game result is stored in a SQLite database
3. Display result:
   * User's choice, computer's choice and the game result is displayed in a first alerts section.
   * The real time count of 'wins-draws-losses' is displayed in a second alerts section
   * History of game is diplayed in table under alerts sections.


### Project components
#### index.html
* Form: Contains buttons for Rock, Paper, and Scissors.
* Alerts: Display the user's choice, computer's choice, and the game result.
* Table: Shows the history of game results.

#### app.py
* Flask Application: The main Flask app is created and configured to use SQLite.
* Database Model: Defines the GameResult model to store the game results.
* Routes:
  * / (home): Handles GET and POST requests to play the game and display results.
* Game Logic: Implements the Rock-Paper-Scissors game logic and stores the results in the database.
* Database
  * GameResult: A table with columns for the game index, computer's choice, user's choice, and the result.
