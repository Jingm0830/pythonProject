
import random

N = []
n = int(input("How many dices? "))

for item in range(n):
    N.append(random.randint(1,6))
amount = sum (N)
print(f"the amount is",{amount})





