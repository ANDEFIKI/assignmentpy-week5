class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")

# Example usage:
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()