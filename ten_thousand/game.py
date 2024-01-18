from ten_thousand.game_logic import GameLogic

def play(roller=None):
    """Main function for the app. Starts the game of Ten Thousand.
    
    Parameters:
    roller: function - A function to roll the dice. If None, GameLogic.roll_dice is used.
    
    Returns:
    displays the welcome message and prompts the user to start the game.
    It then calls start_game with the appropriate dice roller.
    """
    if roller is None:
        roller = GameLogic.roll_dice
    welcome()
    response = input("> ")
    if response.lower() == "n":
        print("OK. Maybe another time")
    else:
        start_game(roller)
        
def welcome():
    """Prints the welcome message for the game"""
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    
def roll_dice(roller, dice_remaining):
    """
    Rolls the specified number of dice.
    
    Parameters:
    roller (function): The dice rolling function.
    dice_remaining (int): The number of dice to roll.
    
    Returns:
    tuple: The result of the dice roll.
    """
    print(f"Rolling {dice_remaining} dice...")
    return roller(dice_remaining)

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
            # converts each character in player input into integer and then forms a tuple out of those integers
            dice_kept = tuple(int(die) for die in keep_response)
            # checks whether each die in dice_kept was actually part of the dice_rolled
            if not all(die in dice_rolled for die in dice_kept):
                print("Invalid input. Please enter only the dice that were rolled.")
                continue
            return dice_kept
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            
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
        
def start_game(roller):
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
        dice_rolled = roll_dice(roller, dice_remaining)

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
        elif action == "r":
            if dice_remaining == 0:
                dice_remaining = 6
        elif action == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break
        

if __name__ == "__main__":
    play()