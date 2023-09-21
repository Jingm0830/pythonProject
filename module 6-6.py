"""
Write a function that receives two parameters:
the diameter of a round pizza in centimeters and the price of the pizza in euros.
The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and price of two pizzas
and tells the user which pizza provides better value for money (which of them has a lower unit price).
You must use the function you wrote for calculating the unit prices.
"""

from math import pi
def pizza_price(diameter, price):
    area = pi *(float(diameter)*0.5)**2
    unit_price = float(price)/area
    return unit_price

while True:
    diameter_1 = input("Diameter of the first pizza is:  ")
    price_1 = input("Price of the first pizza is:  ")

    diameter_2 = input("Diameter of the second pizza is:  ")
    price_2 = input("Price of the second pizza is:  ")

    unit_price_1 = pizza_price(diameter_1, price_1)
    unit_price_2 = pizza_price(diameter_2, price_2)

    if unit_price_1 < unit_price_2:
        print("The first pizza provides better value of money!")
    else:
        print("The second pizza provides better value of money!")

