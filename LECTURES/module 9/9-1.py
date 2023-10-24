"""
Write a Car class that has the following properties:
registration number, maximum speed, current speed and travelled distance.
Add a class initializer that sets the first two of the properties based on parameter values.
The current speed and travelled distance of a new car must be automatically set to zero.
Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
Finally, print out all the properties of the new car.
"""

class Car:
    def __init__(self, Reg_number, Max_speed, Cur_speed=0, Tra_distance=0):
        self.name = Reg_number
        self.Maxspeed = Max_speed
        self.Cur_speed = Cur_speed
        self.Tra_distance = Tra_distance

car=Car('ABC-123',142)
#car=Car('ABC-123',142,120,20000)
print(f"The registeration number is {car.name}\nThe maxspeed is {car.Maxspeed}\n"
      f"The current speed is {car.Cur_speed}\nThe travalled distance is {car.Tra_distance}.")


