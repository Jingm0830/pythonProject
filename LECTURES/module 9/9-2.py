"""
Extend the program by adding an accerelate method into the new class.
The method should receive the change of speed (km/h) as a parameter.
If the change is negative, the car reduces speed.
The method must change the value of the speed property of the object.
The speed of the car must stay below the set maximum and cannot be less than zero.
Extend the main program so that the speed of the car is first increased by +30 km/h,
then +70 km/h and finally +50 km/h.
Then print out the current speed of the car.
Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet.
"""

class car:
    def __init__(self, name, Max_speed):
        self.name = name
        self.max_speed = Max_speed
        self.speed = 0

    def accelerate(self, change):
        current_speed = self.speed + change
        if current_speed < 0:
            self.speed = 0
        elif current_speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = current_speed


CAR = car("MINI",140)

CAR.accelerate(+30)
print(f"After +30km/h, the speed is:", CAR.speed, "km/h now!")

CAR.accelerate(+70)
print(f"After +70km/h, the speed is:", CAR.speed, "km/h now!")

CAR.accelerate(+50)
print(f"After +50km/h, the speed is:", CAR.speed, "km/h now!")

CAR.accelerate(-200)
print(f"After -200km/h, the speed is:", CAR.speed, "km/h now!")

