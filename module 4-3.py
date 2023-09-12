num = input("Enter a number: ")
min = num
max = num

while True:
    num = input("Enter a number: ")
    print("Do you want to enter another number or enter a  empty string to quit! ")
    if num == "" :
     break
    if num < min:
        min = num
    if num > max:
        max = num

print(f"The smallest number is: {min},"
      f"the largest number is: {max}")


