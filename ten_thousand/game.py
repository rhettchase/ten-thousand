from ten_thousand.game_logic import calculate_score

def play(roller=None):
    welcome()
    response = input("> ")
    if response.lower() == "n":
        print("OK. Maybe another time")
    else:
        start_game()
        
def welcome():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
        
def start_game():
    round = 1
    dice = 6
    dice_num = (4, 4, 5, 2, 3, 1)
    
    print(f"Starting round {round}")
    print(f"Rolling {dice} dice...")
    
    # Calculate score based on dice_num
    score = calculate_score(dice_num)
    print("Score:", score)
    
    # Convert tuple elements to strings and join them with a space
    dice_str = " ".join(map(str, dice_num))
    print(f"*** {dice_str} ***")
    
    print("Enter dice to keep, or (q)uit:")
    response = input("> ")
    if response.lower() == "q":
        print("Thanks for playing. You earned 0 points")
        

if __name__ == "__main__":
    play()