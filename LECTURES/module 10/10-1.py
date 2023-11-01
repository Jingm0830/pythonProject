"""
Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down.
A new elevator is always at the bottom floor.
If you make elevator h for example the method call h.go_to_floor(5),
the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
Test the class by creating an elevator in the main program,
tell it to move to a floor of your choice and then back to the bottom floor.
"""
class Elevator:
    def __init__(self, bottom_F, top_F):
        self.bottom_floor = bottom_F
        self.top_floor = top_F
        self.current_floor = bottom_F

    def floor_up(self, target_F):
        while self.current_floor < target_F:
            self.current_floor += 1
            print(f"The lift goes up to {target_F}")

    def floor_down(self, target_F):
        while self.current_floor > target_F:
            self.current_floor -= 1
            print(f"The lift goes down to {target_F}")
    def go_to_floor(self, target_F):
        if target_F < self.bottom_floor:
            self.floor_down(target_F)
        elif target_F > self.bottom_floor:
            self.floor_up(target_F)
        else:
            print(f"The lift is already on {target_F}")

elevator_h = Elevator(1, 10)

target_F = 5
print(f"The lift is on the bottom floor {elevator_h.current_floor} now")
elevator_h.go_to_floor(target_F)
print(f"The lift has on the {target_F} now")
elevator_h.go_to_floor(1)
print(f"The lift has on the bottom floor now")
