import random
from collections import Counter

class GameLogic:
    """
    A class to represent game logic for the ten thousand game.
    
    Attributes:
    none
    
    Methods:
    roll_dice: returns a tuple with random values between 1 and 6
    calculate_score: an integer representing the roll's score according to rules of game
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
        
        # Scoring for 1's
        ones = count[1]
        if ones == 1:
            score += 100
        elif ones == 2:
            score += 200
        elif ones == 3:
            score += 1000
        elif ones == 4:
            score += 2000
        elif ones == 5:
            score += 3000
        elif ones == 6:
            score += 4000

        # Remove counted '1's from the count
        count[1] = 0

        # Score three or more of a kind
        for num, qty in count.items():
            
            if qty >= 3:
                if num == 1:
                    continue  # Skip '1's as they are already scored
                else:
                    three_of_a_kind_score = num * 100

                if qty == 3:
                    score += three_of_a_kind_score
                elif qty == 4:
                    score += three_of_a_kind_score + num * 100  # Double the three of a kind score
                elif qty == 5:
                    score += three_of_a_kind_score + ((5 - 3) * three_of_a_kind_score) 
                elif qty == 6:
                    score += three_of_a_kind_score + ((6 - 3) * three_of_a_kind_score)

                # Remove the scored dice from the count for ones and fives
                if num == 1 or num == 5:
                    count[num] = 0

        # Score individual fives if they are not part of a set
        score += count[5] * 50

        return score