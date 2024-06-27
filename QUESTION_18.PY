# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class


""" 
In Python, a class is defined using the class keyword followed by the class name and a 
colon (:). Inside the class block, you define attributes (data) and methods (functions) 
that all instances (objects) of the class will have access to. The self parameter is used 
within the methods of the class to refer to the instance itself.
"""

class Car:
    # Constructor method to initialize the attributes of the class
    def __init__(self, brand, model, year):
        self.brand = brand   # Attribute: brand of the car
        self.model = model   # Attribute: model of the car
        self.year = year     # Attribute: year of manufacture
    
    # Method to display information about the car
    def display_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")

    # Method to accelerate the car
    def accelerate(self, speed):
        print(f"{self.brand} {self.model} is accelerating at {speed} km/h")

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

# Accessing attributes and methods of the objects
car1.display_info()           # Output: Car: Toyota Corolla (2020)
car2.accelerate(120)          # Output: Honda Civic is accelerating at 120 km/h
