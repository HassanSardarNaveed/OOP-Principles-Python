# Example demonstrating OOP principles in Python

# 1. Encapsulation
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__year = year  # Private attribute (Encapsulation)
    
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        if year > 1885:  # Year should be after the invention of the car
            self.__year = year

# 2. Inheritance
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def car_info(self):
        return f"{self.brand} {self.model}, Year: {self.get_year()}, Doors: {self.doors}"

# 3. Polymorphism
class ElectricCar(Car):
    def __init__(self, brand, model, year, doors, battery_size):
        super().__init__(brand, model, year, doors)
        self.battery_size = battery_size
    
    def car_info(self):  # Overriding method
        return f"{self.brand} {self.model}, Year: {self.get_year()}, Battery: {self.battery_size} kWh"

# 4. Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# Example Usage

# Encapsulation
my_vehicle = Vehicle("Toyota", "Corolla", 2020)
print(my_vehicle.get_year())

# Inheritance and Polymorphism
my_car = Car("Honda", "Civic", 2021, 4)
print(my_car.car_info())

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 4, 100)
print(my_electric_car.car_info())

# Abstraction
payment1 = CreditCardPayment()
payment1.pay(100)

payment2 = PayPalPayment()
payment2.pay(250)
