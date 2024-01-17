# LAB - Class 06

## Project: Ten Thousand v1

## Project Description

Defines a `GameLogic` class that handles calculating score for dice roll. This includes several methods: `calculate_score` and `roll_dice` static method. The `roll_dice` method returns a tuple with random values between 1 and 6. The `calculate_score` method returns an integer representing the roll's score according to rules of game

The code was generated with the assistance of AI to generate code blocks.

[Prompt Documentation](./prompt.md)

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

#### Tests

- Run tests by activating virtual environment and running `pytest` command in command line
- To run tests specifically for `roll_dice`, run `pytest tests/version_1/test_roll_dice` in command line
- To run the tests specifically for `calculate_score`, run `pytest tests/version_1/test_calculate_score.py` in command line
