# OOP Principles in Python
Overview
This repository contains a simple Python program that demonstrates the core principles of Object-Oriented Programming (OOP). The key concepts illustrated in this project include:

Encapsulation: Restricting access to certain components of an object.
Inheritance: Creating a new class from an existing class.
Polymorphism: Using a single interface to represent different data types.
Abstraction: Hiding the internal implementation details of a method and exposing only the functionality.
Code Explanation
Encapsulation
The Vehicle class demonstrates encapsulation by using private attributes to restrict direct access to certain properties.

Inheritance
The Car class inherits from the Vehicle class, and the ElectricCar class inherits from the Car class. This shows how properties and methods can be passed from one class to another.

Polymorphism
The ElectricCar class overrides the car_info method from the Car class to demonstrate polymorphism. The same method name is used, but it behaves differently depending on the object calling it.

Abstraction
The Payment class is an abstract base class that requires subclasses to implement the pay method, showcasing abstraction.

How to Run the Program
Clone the Repository:


git clone https://github.com/HassanSardarNaveed/OOP-Principles-Python.git
cd OOP-Principles-Python
Run the Program:
Ensure you have Python installed on your machine. You can run the program by executing the Python script:


python oop_principles.py
The script will execute and print output demonstrating the OOP principles.

How to Test the Program
To test the program, follow these steps:

Check Encapsulation:

Verify that direct access to the __year attribute of the Vehicle class is restricted.
Test the get_year and set_year methods to ensure they work correctly.
Check Inheritance and Polymorphism:

Create objects of the Car and ElectricCar classes.
Call the car_info method on both objects and observe the different outputs.
Check Abstraction:

Instantiate objects of CreditCardPayment and PayPalPayment.
Call the pay method on these objects to see the output.
Modify and Extend the Code:

Add a new subclass to test inheritance.
Override methods to test polymorphism further.
Implement additional payment methods to see how abstraction can be extended.
Contributing
Feel free to contribute by opening an issue or submitting a pull request if you have any ideas to improve the code or add new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.
