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

