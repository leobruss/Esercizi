#Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
#Handle ValueError if the input is negative by returning an informative message.
import math
def safe_sqrt(number) -> float:
    if number >= 0:
        squere_number = math.sqrt(number)
        return squere_number
    else:
        raise ValueError("the number is negative therefore it is impossible to calculate the squared index")
    
print(safe_sqrt(4))