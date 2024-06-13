#Safe Square Root: 
#Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
#Handle ValueError if the input is negative by returning an informative message
import math
def safe_sqrt(number) ->str:
    if number > 0:
        square_root = math.sqrt(number)
    else:
        raise ValueError("Impossibile restituire una radice quadrata di un numero negativo")
    
    return f"La radice quadrata di {number} è: {square_root}"

print(safe_sqrt(9))