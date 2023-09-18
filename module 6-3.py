"""
Write a function that gets the quantity of gasoline in American gallons
and returns the number converted to litres. Write a main program that asks for
a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function.
Conversions continue until the user inputs a negative value.
"""

def gas_quantity_return(i):
    result = i * 3.78541178
    return result


while True:
    i = float(input("Enter the quantity of gas in gallons and enter a negative number to quit:\n  "))
    result = gas_quantity_return(i)
    if result < 0:
        print("Quit!")
        break
    else:
        print(f"The quantity is {result:.3f} liters!")


