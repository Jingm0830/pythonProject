"""
Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise
the same as the original list except that all uneven numbers
have been removed. For testing, write a main program
where you create a list, call the function,
and then print out both the original as well as the cut-down list.
"""

from random import randint
def new_list(num):
    even_list = []
    for i in num:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

test_begin = randint(0,30)
test_end = randint(test_begin + 10, test_begin + 20)

num = list(range(test_begin, test_end))
even_list = new_list(num)

print(f"The original list is  {num}")
print(f"The new list is {even_list}")





