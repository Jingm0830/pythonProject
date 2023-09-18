"""
Write a function that returns a random dice roll between 1 and 6.
The function should not have any parameters.
Write a main program that rolls the dice until the result is 6.
The main program should print out the result of each roll
"""
import random
def dice_roll(num):
    num = random.range(1,6)
    return

i = 0
list = []
for i in range(1,6):
    i = random.randint(1,6)
    if i == 6:
        break
    else:
        list.append(i)
print([list])




