import random
from collections import Counter

class GameLogic:
    """
    A class to represent game logic for the ten thousand game.
    
    Attributes:
    name: str - the name of the band member
    
    Methods:
    roll_dice: returns a tuple with random values between 1 and 6
    calculate_score: an integer representing the roll's score according to rules of game
    """
    @staticmethod
    def roll_dice(number_of_dice):
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")
        
    @staticmethod
    def calculate_score(roll):
        # Use Counter to count the occurrences of each number
        count = Counter(roll)
        
        # Check for a straight (1-6)
        if all(count[num] == 1 for num in range(1, 7)):
            return 1500

        score = 0

        # Score three or more of a kind
        for num, qty in count.items():

            if qty >= 3:
                if num == 1:
                    three_of_a_kind_score = 1000
                else:
                    three_of_a_kind_score = num * 100

                if qty == 3:
                    score += three_of_a_kind_score
                elif qty == 4:
                    score += three_of_a_kind_score + num * 100  # Double the three of a kind score
                elif qty == 5:
                    score += three_of_a_kind_score + ((5 - 3) * three_of_a_kind_score) # Four times the three of a kind score
                elif qty == 6:
                    score += three_of_a_kind_score + ((6 - 3) * three_of_a_kind_score)  # Eight times the three of a kind score

                # Remove the scored dice from the count for ones and fives
                if num == 1 or num == 5:
                    count[num] = 0

        # Score individual ones and fives if they are not part of a set
        score += count[1] * 100
        score += count[5] * 50

        return score