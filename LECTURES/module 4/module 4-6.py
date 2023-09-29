import random

N = int(input("How many points do you need: "))
n = 0
times = N
i=0
while i<times:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        n+=1
    i+=1

Pi = 4*n/N
print(f"Pi is: ", {Pi})
