from ten_thousand.game_logic import GameLogic
from collections import Counter

dice_roller = None


def play(roller=None):
    """Main function for the app. Starts the game of Ten Thousand.
    
    Parameters:
    roller: function - A function to roll the dice. If None, GameLogic.roll_dice is used.
    
    Returns:
        string: displays the welcome message and prompts the user to start the game.
        It then calls start_game with the appropriate dice roller.
    """
    global dice_roller
    dice_roller = GameLogic.roll_dice if roller is None else roller
    
    if roller is None:
        roller = dice_roller
    welcome()
    response = input("> ")
    if response.lower() == "n":
        print("OK. Maybe another time")
    else:
        start_game()
        
def welcome():
    """Prints the welcome message for the game"""
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    
def roll_dice(dice_remaining):
    """
    Rolls the specified number of dice.
    
    Parameters:
    roller (function): The dice rolling function.
    dice_remaining (int): The number of dice to roll.
    
    Returns:
    tuple: The result of the dice roll.
    """
    global dice_roller
    print(f"Rolling {dice_remaining} dice...")
    return dice_roller(dice_remaining)

def do_round(round_num):
    """
    Play a round of the game

    Args:
        round_num: The current round number

    Returns:
        integer for number of points scored in the round
        -1 has special meaning for "quit"
    """
    print(f"Starting round {round_num}")
    dice_remaining = 6
    round_score = 0

    while True:
        dice_rolled = roll_dice(dice_remaining)
        # Check if all dice are scoring
        scorers = GameLogic.get_scorers(dice_rolled)
        if len(scorers) == 0:
            dice_str = format_roll(dice_rolled)
            zilch_message = zilch()  # Get the zilch message
            print(dice_str + zilch_message)  # Concatenate and print both messages
            return 0  # End the round with zero points

        dice_kept = get_dice_to_bank(dice_rolled)
        if dice_kept is None:  # Player chooses to quit
            return -1

        score = GameLogic.calculate_score(dice_kept)
        round_score += score
        dice_remaining -= len(dice_kept)
        
        if len(scorers) == len(dice_rolled):
            dice_remaining = 6  # Reset dice if all are scoring
        
        print(f"You have {round_score} unbanked points and {dice_remaining} dice remaining")

        if dice_remaining == 0:  # All dice used, refresh dice
            dice_remaining = 6

        action = handle_player_action()

        if action == 'b':  # Bank the points
            return round_score
        elif action == 'q':  # Quit
            return -1


def get_dice_to_bank(dice_rolled):
    """
    Prompts the player to choose which dice to keep from the roll.
    
    Parameters:
    dice_rolled (tuple): The dice that were rolled.

    Returns:
    tuple: The dice chosen to keep, or None if the player chooses to quit.
    """
    while True:
        # create list of strings that contain the rolled dice and concatenate them into single string separated by spaces
        dice_str = format_roll(dice_rolled)
        print(dice_str)
        print("Enter dice to keep, or (q)uit:")
        keep_response = input("> ").strip()

        if keep_response.lower() == "q":
            return None
        
        try:
            # Remove spaces and then convert each character to an integer
            dice_kept = tuple(int(die) for die in keep_response.replace(" ", ""))
            
            if GameLogic.validate_keepers(dice_rolled, dice_kept):
                return dice_kept
            else:
                print("Cheater!!! Or possibly made a typo...")
        except ValueError:
            print("Cheater!!! Or possibly made a typo...")

def format_roll(roll):
    """
    Converts given roll into display friendly string.

    Args:
        roll: e.g. (5, 1, 1, 4, 5, 5)

    Returns:
        string: e.g. "*** 5 1 1 4 5 5 ***"
    """
    return f"*** {' '.join([str(die) for die in roll])} ***"

            
def handle_player_action():
    """
    Gets the player's next action choice.

    Returns:
    str: The player's chosen action
    """
    print("(r)oll again, (b)ank your points or (q)uit:")
    return input("> ").lower()

def bank_points(total_score, score, round):
    """
    Handles the banking of the player's points.

    Parameters:
    total_score (int): The player's total score before banking.
    score (int): The score to be banked.
    round (int): The current round number.

    Returns:
    int: The player's new total score after banking.
    """
    total_score += score
    print(f"You banked {score} points in round {round}")
    print(f"Total score is {total_score} points")
    return total_score
        
def start_game():
    """
    Manages the rounds and overall game flow. This function controls the main game loop, including rolling dice, keeping score,
    and handling player decisions.

    Parameters:
    roller (function): The function used to roll dice.
    """
    total_score = 0
    round = 1
    dice_remaining = 6
    
    while True:
        round_score = do_round(round)

        if round_score == -1:  # Player quits
            print(f"Thanks for playing. You earned {total_score} points")
            break

        total_score = bank_points(total_score, round_score, round)
        round += 1

def zilch():
    return """
****************************************
**        Zilch!!! Round over         **
****************************************"""

if __name__ == "__main__":
    
    rolls = [
        (1, 2, 5, 1, 2, 1),
        (4, 4),
        (1, 1, 2, 5, 1, 6),
    ]
    
    def mock_roller(number_of_dice):
        return rolls.pop(0)
    play(roller=mock_roller)