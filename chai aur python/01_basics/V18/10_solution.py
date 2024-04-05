# Multiple Inheritance
# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    total_car=0 #It is called class variable

    def __init__(self, brand, model):
        self.__brand = brand  #It is called Object variable.
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static method is a method that is part of a class rather than an 'instance of that class'(or objects)
    # @staticmethod apply krte hi object can't take the methods of classes or methods described in classes as they convert the methods into static methods which break the connection of self between classes and objects.
    @staticmethod
    def general_description(self):
        return "Cars are means of transport."
    
    # to call the methods through classes, we don't need to ive self as a parameter in those methods
    def general_description1():
        return "Cars are means of transport."
    
    @property
    def model(self):
        return self.__model


class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar("Tesla", "CyberTruck")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())