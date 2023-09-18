"""
Write a function that returns a random dice roll between 1 and 6.
The function should not have any parameters.
Write a main program that rolls the dice until the result is 6.
The main program should print out the result of each roll
"""
from random import randint
def dice_roll():
    return randint(1,6)


while True:
    result = dice_roll()
    print(f"It's: {result}.")
    if result == 6:
        break




