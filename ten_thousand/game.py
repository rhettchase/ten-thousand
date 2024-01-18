from ten_thousand.game_logic import GameLogic

def play(roller=None):
    if roller is None:
        roller = GameLogic.roll_dice
    welcome()
    response = input("> ")
    if response.lower() == "n":
        print("OK. Maybe another time")
    else:
        start_game(roller)
        
def welcome():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
        
def start_game(roller):
    total_score = 0
    round = 1
    dice = 6
    dice_remaining = 6
    # dice_rolled = (4, 4, 5, 2, 3, 1)
    
    while True:
        print(f"Starting round {round}")
        print(f"Rolling {dice_remaining} dice...")
        dice_rolled = roller(dice_remaining)

        dice_str = " ".join(map(str, dice_rolled))
        print(f"*** {dice_str} ***")
        
        print("Enter dice to keep, or (q)uit:")
        keep_response = input("> ").strip()
        if keep_response.lower() == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break

        try:
            # Process each character in the input as a separate die
            dice_kept = tuple(int(die) for die in keep_response)
            if not all(die in dice_rolled for die in dice_kept):
                print("Invalid input. Please enter only the dice that were rolled.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        score = GameLogic.calculate_score(dice_kept)
        dice_remaining -= len(dice_kept)

        print(f"You have {score} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        action = input("> ")
        
        if action.lower() == "b":
            total_score += score
            print(f"You banked {score} points in round {round}")
            print(f"Total score is {total_score} points")
            round += 1
            dice_remaining = 6  # Reset dice count for new round
        elif action.lower() == "r":
            if dice_remaining == 0:
                dice_remaining = 6  # If all dice are scored, the player gets to roll all 6 dice again.
            # Continue with the next iteration to roll again
        elif action.lower() == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break
        

if __name__ == "__main__":
    play()