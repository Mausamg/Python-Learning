class Car:
    total_car = 0
    def __init__(self, userbrand,usermodel,useryear):
        self.__brand = userbrand
        self.model = usermodel
        self.year = useryear
        Car.total_car+=1
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.year} {self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars have 4 wheels and are used for transportation."
    
class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, useryear,battery_size):
        super ().__init__(userbrand, usermodel, useryear)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla=ElectricCar("Tesla","Model S","2024","85kwh")
print(my_tesla.fuel_type(), Car.total_car)  
    
Car1 = Car("Toyota", "Corolla", 2020)
print(Car1.fuel_type(), Car.total_car)

Car2 = Car("Honda", "Civic", 2021)
print(Car2.full_name(),Car.total_car)

Car3 = Car("Ford", "Mustang", 2022)
print(Car3.full_name(),Car.total_car) 