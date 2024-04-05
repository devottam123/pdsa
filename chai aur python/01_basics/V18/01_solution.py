# Basic Class and Object
# Create a Car class with attributes like brand and model. Then create an instance of this class.

# Class Method and Self
# Add a method to the Car class that displays the full name of the car (brand and model). 

# Inheritance
# Create an ElectricCar Class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.full_name())
