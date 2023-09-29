import random

num =random.randint(1,10)
guess = 0
print("Guess the number in the box(1-10)")

while num != guess:
    guess = int(input("Guess the number: "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print("Correct!")
