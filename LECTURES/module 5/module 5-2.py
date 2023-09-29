"""
Write a program that asks the user to enter numbers until they input an empty string to quit.
At the end, the program prints out the five greatest numbers sorted in descending order.
Hint: You can reverse the order of sorted list items by using the method with the argument.
sort reverse=True
"""
#creat a list
number_list = []
n = input("Enter a number or quit by pressing enter: ")

#add numbers into list
while n!="":
    number_list.append(n)
    n = input("Enter next number or quit by pressing enter: ")
    if n == "":
        break

#sort the numbers and print the greatest 5
number_list.sort(reverse=True)
print(number_list[0:5])


