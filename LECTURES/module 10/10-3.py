"""
Extend the program again by adding a method fire_alarm that does not receive any parameters
and moves all elevators to the bottom floor.
Continue the main program b y causing a fire alarm in your building.
"""
class Elevator:
    def __init__(self, elevator_number, button_floor=1):
        self.elevator_number = elevator_number
        self.button_floor = button_floor

    def move_to(self, target_floor):
        self.target_floor = target_floor
        print(f"Elevator {self.elevator_number} is moving from {self.button_floor} to {self.target_floor}")
        self.button_floor = target_floor
        print(f"Elevator {self.elevator_number} has arrived at {self.button_floor}")

class Building():
    def __init__(self, button_floor, top_floor, number_elevator):
        self.button_floor = button_floor
        self.top_floor = top_floor
        self.number_elevator = number_elevator
        self.elevator = [Elevator(i) for i in range(1, number_elevator+1)]

    def run_elevator(self,elevator_number, target_floor):
        self.elevator_number = elevator_number
        self.target_floor = target_floor
        if 1<=target_floor <= self.top_floor:
            elevator = self.elevator[elevator_number - 1]
            elevator.move_to(target_floor)
        else:
            print(f"Choose again between 1 and {self.top_floor}")

    def fire_alarm(self):
        print("The fire bell is ringing!")
        for i in self.elevator:
            i.move_to(self.button_floor)







# creat a building with 20 floors and 5 elevators
buildings = Building(1,20, 5)

buildings.run_elevator(1,12)
buildings.run_elevator(2,8)
buildings.run_elevator(3,19)
buildings.run_elevator(4,16)
buildings.run_elevator(5,6)

buildings.fire_alarm()