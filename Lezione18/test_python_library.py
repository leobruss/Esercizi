from personalized_math_library import Fraction, ZeroDenominatorError, InvalidOperationError

try:
    frac1 = Fraction(1, 2)
    frac2 = Fraction(3, 4)
    
    print("Fraction 1:", frac1)
    print("Fraction 2:", frac2)
    
    result = frac1.add(frac2)
    print("Addition:", result)
    
    result = frac1.subtract(frac2)
    print("Subtraction:", result)
    
    result = frac1.multiply(frac2)
    print("Multiplication:", result)
    
    result = frac1.divide(frac2)
    print("Division:", result)
    
    print("Fractions are equal:", frac1 == frac2)
    
    print("Numerator of Fraction 1:", frac1.get_numerator())
    print("Denominator of Fraction 1:", frac1.get_denominator())

except ZeroDenominatorError as zde:
    print(f"ZeroDenominatorError: {zde}")
except InvalidOperationError as ioe:
    print(f"InvalidOperationError: {ioe}")
except FractionError as fe:
    print(f"FractionError: {fe}")