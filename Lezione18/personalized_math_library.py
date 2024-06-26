from math import gcd

class FractionError(Exception):
    pass

class ZeroDenominatorError(FractionError):
    pass

class InvalidOperationError(FractionError):
    pass

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDenominatorError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def add(self, other):
        try:
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except Exception as e:
            raise InvalidOperationError(f"Error in addition: {e}")

    def subtract(self, other):
        try:
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except Exception as e:
            raise InvalidOperationError(f"Error in subtraction: {e}")

    def multiply(self, other):
        try:
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except Exception as e:
            raise InvalidOperationError(f"Error in multiplication: {e}")

    def divide(self, other):
        try:
            if other.numerator == 0:
                raise ZeroDenominatorError("Cannot divide by a fraction with a numerator of zero.")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        except ZeroDenominatorError as zde:
            raise zde
        except Exception as e:
            raise InvalidOperationError(f"Error in division: {e}")

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"