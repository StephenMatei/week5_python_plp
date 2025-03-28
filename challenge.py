class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road."

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky."

class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on water."

# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Calling move() for each object
for v in vehicles:
    print(v.move())
