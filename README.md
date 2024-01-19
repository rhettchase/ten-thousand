# LAB - Class 08

## Project: Ten Thousand v3

## Project Description

Ten Thousand Game App allows player to start and play the game. 

Features: It allows user to set aside dice each roll, “bank” current score or decide to roll again. The app keeps track of total score and the current round. It handles setting aside scoring dice and continuing turn with remaining dice. The app validates user input to handle when cheating occurs. It also allows users to continue rolling with 6 new dice when all dice have scored in the current turn. If a player rolls zilch (no points), the app scores this as a zero and ends the round.

### Author: Rhett Chase

### Links and Resources
<!-- - [back-end server url](http://xyz.com/) (when applicable)
- [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Rules of Game](https://en.wikipedia.org/wiki/Dice_10000)

### Setup

- `pip install pytest`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

-`python3 -m ten_thousand.game`

#### How to use your library (where applicable)

- `game_logic.py` uses the `random` and `Counter` libraries, which have been imported on the top of the script
- `game.py` imports the `GameLogic` class to utilize its methods

#### Tests

- Run tests by activating virtual environment and running `python -m pytest -k version_3` command in command line
