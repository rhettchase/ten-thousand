# Prompt Guide

## Prompt used to generate code

### Prompt 1

```chatGPT
in python, create a GameLogic class. 

add a roll_dice static method to the GameLogic class.

The input to `roll_dice` is an integer between 1 and 6.
The output of `roll_dice` is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to `roll_dice` method.
```

### Prompt 2

```chatGPT
Add `calculate_score` static method to GameLogic class.
 The input to `calculate_score` is a tuple of integers that represent a dice roll.
 The output from `calculate_score` is an integer representing the roll’s score according to scoring rules.

scoring rules:
- Single _fives_ are worth 50 points
- Single _ones_ are worth 100 points
- Three of a kind are worth 100 points times the number rolled, 
	- except for three _ones_ which are worth 1000 points
- If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 dice showing the number 3 would be 600 points and 5 dice showing the number 3 would be 1200 points
    - This makes the highest possible score in a single roll 8000 for six _ones_ (1000 for three _ones_, after that player multiplies the roll by two for each additional _one_ in that series of rolling.)
- A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
- Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
- Full house (3 of a kind plus 2 of a kind) are worth 1,500

existing code:

import random

class GameLogic:

    @staticmethod
    def roll_dice(number_of_dice):
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")

tests:
< tests >
```

### Subsequent Prompts (not exhaustive)

```chatGPT
how can this code be modified to use the Counter library?
```

```chatGPT
 I want to add one more rule: 3 pairs are worth 1500 points for example 
((2, 2, 3, 3, 6, 6), 1500),
```

## Actual code from AI

### Prompt 1 Code

```python
import random

class GameLogic:
    @staticmethod
    def roll_dice(number_of_dice):
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")

# Example of using the roll_dice method
example_roll = GameLogic.roll_dice(3)
example_roll

```

### Prompt 2 Code

```python
import random

class GameLogic:
    @staticmethod
    def roll_dice(number_of_dice):
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")
    
    @staticmethod
    def calculate_score(roll):
        # Initialize a dictionary to count the occurrences of each number
        count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        
        # Count the occurrences of each number in the roll
        for num in roll:
            count[num] += 1
        
        score = 0
        
        # Calculate the score based on the scoring rules
        
        # Single fives are worth 50 points
        score += count[5] * 50
        
        # Single ones are worth 100 points
        score += count[1] * 100
        
        # Three of a kind
        for num in range(1, 7):
            if count[num] >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
        
        # Four or more of a kind
        for num in range(1, 7):
            if count[num] >= 4:
                score += (num * 100) * (2 ** (count[num] - 3))
        
        # A straight from 1 to 6 is worth 1500 points
        if all(count[num] >= 1 for num in range(1, 7)):
            score = 1500
        
        # Three pairs are worth 1000 points
        if all(count[num] == 2 for num in range(1, 7)):
            score = 1000
        
        # Full house (3 of a kind plus 2 of a kind) are worth 1500 points
        if any(count[num] == 3 for num in range(1, 7)) and any(count[num] == 2 for num in range(1, 7)):
            score = 1500
        
        return score

```

## Calculate Score Method Code v2

```python
class GameLogic:
    # ... existing methods ...

    @staticmethod
    def calculate_score(roll):
        # Count the occurrences of each number
        count = {num: roll.count(num) for num in range(1, 7)}
        
        # Check for a straight (1-6)
        if all(count[num] == 1 for num in range(1, 7)):
            return 1500

        score = 0

        # Score three or more of a kind
        for num in range(1, 7):
            if count[num] >= 3:
                if num == 1:
                    score += 1000 * (2 ** (count[num] - 3))
                else:
                    score += (num * 100) * (2 ** (count[num] - 3))

                # Remove the scored dice from the count
                count[num] = max(count[num] - 3, 0)

        # Score individual ones and fives if they are not part of a set
        score += count[1] * 100
        score += count[5] * 50

        return score

```

### Adds Counter

```python
from collections import Counter

class GameLogic:
    # ... existing methods ...

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
                    score += 1000 * (2 ** (qty - 3))
                else:
                    score += (num * 100) * (2 ** (qty - 3))

                # Remove the scored dice from the count
                count[num] = max(qty - 3, 0)

        # Score individual ones and fives if they are not part of a set
        score += count[1] * 100
        score += count[5] * 50

        return score

```


