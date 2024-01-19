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
        dice_str = " ".join([str(die) for die in dice_rolled])
        print(f"*** {dice_str} ***")
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
        print(f"Starting round {round}")
        dice_rolled = roll_dice(dice_remaining)

        dice_kept = get_dice_to_bank(dice_rolled)
        if dice_kept is None:
            print(f"Thanks for playing. You earned {total_score} points")
            break

        score = GameLogic.calculate_score(dice_kept)
        dice_remaining -= len(dice_kept)
        print(f"You have {score} unbanked points and {dice_remaining} dice remaining")

        action = handle_player_action()
        
        if action == "b":
            total_score = bank_points(total_score, score, round)
            round += 1
            dice_remaining = 6
            # print(f"You banked {score} points in round {round}")
            # print(f"Total score is {total_score} points")
        elif action == "r":
            if dice_remaining == 0:
                dice_remaining = 6
        elif action == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break
        

if __name__ == "__main__":
    
    # rolls = [
    #     (2, 3, 1, 3, 4, 2),
    #     (4, 2, 4, 4, 6),
    #     (3, 2, 3, 2, 1, 4),
    # ]
    
    # def mock_roller(number_of_dice):
    #     return rolls.pop(0)
    play()