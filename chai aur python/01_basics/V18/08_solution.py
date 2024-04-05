# Property Decorator
# Use a property decorator in the Car class to make the model attribute read-only.

# class Car:
#     total_car=0 #It is called class variable

#     def __init__(self, brand, model):
#         self.__brand = brand  #It is called Object variable.
#         self.model = model
#         Car.total_car += 1

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def get_brand(self):
#         return self.__brand + " !"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     # static method is a method that is part of a class rather than an 'instance of that class'(or objects)
#     # @staticmethod apply krte hi object can't take the methods of classes or methods described in classes as they convert the methods into static methods which break the connection of self between classes and objects.
#     @staticmethod
#     def general_description(self):
#         return "Cars are means of transport."
    
#     # to call the methods through classes, we don't need to ive self as a parameter in those methods
#     def general_description1():
#         return "Cars are means of transport."
    


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"


# my_car = Car("Tata", "Safari")
# print(my_car.model)
# my_car.model = "City"
# print(my_car.model)
# We can overwrite the variables(or attributes) of an object.

# If we don't want this to happen:
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

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Tata", "Safari") 

# my_car.model = "City"
# print(my_car.model())

print(my_car.model)
