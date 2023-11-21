"""
Extend the previosly written Car class by adding two subclasses:
ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property.
Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses.
For example, the initializer of electric cars receives the registration number, maximum speed
and battery capacity as its parameter. It calls the initializer of the base class to set the first
two properties and then sets its capacity. Write a main program where you create one
electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
Select speeds for both cars,
make them drive for three hours and print out the values of their kilometer counters.
"""
class Car:
    total_cars = 0
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.speed = 0
    def accelerate(self, change):
        self.change=change
        current_speed = self.speed + change
        if current_speed < 0:
            self.speed = 0
        elif current_speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = current_speed

    def distance(self, time):
        values = self.speed * time
        return values

class Electric_cars(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity

class Gasoline_cars(Car):
    def __init__(self, reg_num, Max_speed, tank_volume):
        super().__init__(reg_num, Max_speed)
        self.tank_volume = tank_volume




ecar=Electric_cars("ABC-15",180, 52.5)
gcar=Gasoline_cars("ACD-123",165, 32.3)
ecar.accelerate(120)
gcar.accelerate(130)
ecar.distance(3)
gcar.distance(3)
print(f"The distance of {ecar.reg_num} is {ecar.distance(3)}")
print(f"The distance of {gcar.reg_num} is {gcar.distance(3)}")
