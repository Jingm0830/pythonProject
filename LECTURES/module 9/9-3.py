"""
Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed
in the given time. Example: The travelled distance of car object is 2000 km.
The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
"""
class car:
    def __init__(self, name, Current_speed=60, travelled_distance=2000):
        self.name = name
        self.speed = Current_speed
        self.distance = travelled_distance

    def drive(self, hour):
        new_distance = self.distance + self.speed * hour
        print(f"After {hour} hours, the travelled distance is: {new_distance} KM")

CAR = car("MINI")
CAR.drive(1.5)