#An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to 
#(possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), 
#and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
#If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). 

#Catch any ValueError that occurs, and instead raise a FormulaError.

#If the second input is not '+' or '-', again raise a FormulaError.

#If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, 
#until the user enters quit.

class FormulaError(Exception):
    pass

def parse_input(user_input):
    parts = user_input.split()
    
    if len(parts) != 3:
        raise FormulaError("Input does not consist of three elements.")
    
    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        raise FormulaError("The first and third input values must be numbers.")
    
    operator = parts[1]
    if operator not in ('+', '-'):
        raise FormulaError("The operator must be '+' or '-'.")
    
    return num1, operator, num2

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

def main():
    while True:
        user_input = input("Enter a formula (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        try:
            num1, operator, num2 = parse_input(user_input)
            result = calculate(num1, operator, num2)
            print("Result:", result)
        except FormulaError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()