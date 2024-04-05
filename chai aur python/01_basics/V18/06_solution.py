# Class Variable
# Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car=0 #It is called class variable

    def __init__(self, brand, model):
        self.__brand = brand  #It is called Object variable.
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "Safari")
safari3 = Car("Tata", "Nexon")

# print(safari.total_car)
print(Car.total_car)
#Here total_car represensts number of objects formed by the class Car.
