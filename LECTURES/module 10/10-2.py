"""
Extend the previous program by creating a Building class.
The initializer parameters for the class are the numbers of the bottom
and top floors and the number of elevators in the building.
When a building is created, the building creates the required number of elevators.
The list of elevators is stored as a property of the building.
Write a method called run_elevator that accepts the number of the elevator
and the destination floor as its parameters.
In the main program, write the statements for creating a new building
and running the elevators of the building.
"""
class Elevator:
    def __init__(self, elevator_number, button_floor=1):
        self.elevator_number = elevator_number
        self.current_floor = button_floor

    def move_to(self, target_floor):
        self.target_floor = target_floor
        print(f"Elevator {self.elevator_number} is moving from {self.current_floor} to {self.target_floor}")
        self.current_floor = target_floor
        print(f"Elevator {self.elevator_number} has arrived at {self.current_floor}")

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


# creat a building with 20 floors and 5 elevators
builtins = Building(1,19, 5)

builtins.run_elevator(1,12)
builtins.run_elevator(2,8)
builtins.run_elevator(3,19)
builtins.run_elevator(4,16)
builtins.run_elevator(5,6)

