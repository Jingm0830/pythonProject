"""
Write a program that asks the user for an integer and tells if the number is a prime number.
Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
"""

N = int(input("Enter a integer: "))
flag = True
if N ==1:
    print("It's not a prime!")
else:
    for i in range(2, N//2+1):
        if (N % i == 0):
            flag = False
            break
    if flag:
        print(f"{N}","is  a prime number!")
    else:
        print(f"{N}", "is not a prime number!")