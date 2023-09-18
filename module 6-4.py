"""
Write a function that gets a list of integers as a parameter.
The function returns the sum of all the numbers in the list. For testing,
write a main program where you create a list, call the function,
and print out the value it returned.
"""

def sum_of_list(list, sum):
    for i in list:
        sum += i
    return sum

sum = 0
list = []
while True:
    numbers = input("Enter a number to list:  ")
    if numbers != "":
        list. append(int(numbers))

    else:
        break
sum = sum_of_list(list, sum)
print(f"The sum of the list is {sum}")