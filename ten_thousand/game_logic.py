import random
from collections import Counter

class GameLogic:
    """
    A class to represent game logic for the ten thousand game.
    
    Attributes:
    none
    
    Methods:
    roll_dice: returns a tuple with random values between 1 and 6
    calculate_score: returns an integer representing the roll's score according to rules of game
    """
    @staticmethod
    def roll_dice(number_of_dice):
        """
        Static method that handles rolling dice
        Parameters:
        number_of_dice: int, between 1 and 6
        Returns:
        - tuple: with random values between 1 and 6; length of tuple must match the argument given to `roll_dice` method

        """
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")
        
    @staticmethod
    def calculate_score(roll):
        """
        Static method that handles calculating the score for the dice roll
        Parameters:
        roll: tuple of integers that represent a dice roll
        Returns:
        integer representing the roll's score according to the rules of the game
        """
        # Use Counter to count the occurrences of each number
        count = Counter(roll)
        
        # Check for three pairs
        if len(roll) == 6 and len(count) == 3 and all(qty == 2 for qty in count.values()):
            return 1500
        
        # Check for a straight (1-6)
        if all(count[num] == 1 for num in range(1, 7)):
            return 1500

        score = 0
        
        for num, qty in count.items():
            if qty >= 3:
                # calculate base score for three_of_a_kind
                three_of_a_kind_score = 1000 if num == 1 else num * 100
                multiplier = 1

                if qty == 4:
                    multiplier = 2
                elif qty == 5:
                    multiplier = 3
                elif qty == 6:
                    multiplier = 4

                # calculate score for roll based on base score for three of a kind * multiplier then add to score
                score += three_of_a_kind_score * multiplier
            elif num == 1:
                # Scoring for individual 1's
                score += qty * 100
            elif num == 5:
                # Scoring for individual 5's
                score += qty * 50

        return score
    
    print(calculate_score((1, 1, 1, 1, 1, 6)))
    # output: 3000