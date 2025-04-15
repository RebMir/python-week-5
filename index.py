#Assignment 1
# Defining class, methods and attributes
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__battery = 100  # Encapsulated attribute

    def get_battery(self):
        return f"Battery level: {self.__battery}%"

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} is now fully charged.")

# the smartphone inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def show_info(self):
        print(f"Smartphone Info:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  OS: {self.os}")

# testing
phone = Smartphone("Apple", "iPhone 14", "iOS 17")
phone.show_info()
phone.make_call("0723456789")
print(phone.get_battery())
phone.charge()


# Activity 2:Polymorphism Challenge! 
class Vehicle:
    def move(self):
        print("This Vehicle moves")
        
#polymorphism in action
class Lorry(Vehicle):
    def move(self):
        print("The Lorry is driving on the road")
        
class Boat(Vehicle):
    def move(self):
        print("Sailing on water")
        
def vehicle_movement(vehicle):
    vehicle.move()
    
    
vehicles = [Lorry(), Boat()]

for v in vehicles:
    vehicle_movement(v)