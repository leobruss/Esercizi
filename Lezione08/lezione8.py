#Exercise 1: Creating an Abstract Class with Abstract Methods
from abc import ABC, abstractmethod
class Shape (ABC):

    @abstractmethod
    def area()->float:
        pass

    @abstractmethod
    def perimeter()->float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self)->float:
        area: float = 3.14 * (self.radius**2)
        return area

    def perimeter(self)->float:
        perimeter: float = 2 * (3.14 * self.radius)
        return perimeter

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


    def area(self)->float:
        area: float = self.width * self.height
        return area


    def perimeter(self)->float:
        perimeter: float = (self.width * 2) + (self.height * 2)
        return perimeter
    
circle = Circle(5)
rectangle = Rectangle(4, 7)
print()
print("CERCHIO:")
print(f"L'area del cerchio è: {circle.area()}")
print(f"Il perimetro del cerchio è: {circle.perimeter()}")
print()
print("RETTANGOLO:")
print(f"L'area del rettangolo è: {circle.area()}")
print(f"Il perimetro del rettangolo è: {circle.perimeter()}")

print("\n")
print("*","-"*100,"*")
print("\n")
#Exercise 2: Implementing Static Methods
from abc import ABC
class MathOperations (ABC):
        
    @staticmethod
    def add(num1: int, num2: int) -> int:
        number_sum: int = num1 + num2
        return number_sum

    @staticmethod
    def multiply (num1: int, num2: int) -> int: 
        number_sum: int = num1 * num2
        return number_sum
    

print(f"Somma: {MathOperations.add(4, 6)}")
print()
print(f"Moltiplicazione: {MathOperations.multiply(4, 6)}")