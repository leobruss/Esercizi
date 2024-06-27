def is_valid_parenthesis(s: str) -> bool:
    stack = []

    parentesi = {')': '(', 
                 '}': '{', 
                 ']': '['
    }
    
    for char in s:
        if char in parentesi:
            if stack:
                top_element = stack.pop()
            else:
                return False
            
            if parentesi[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack






	
print(is_valid_parenthesis("()"))

print(is_valid_parenthesis("()[]{}"))

print(is_valid_parenthesis("(]"))

print(is_valid_parenthesis("([)]"))      

print(is_valid_parenthesis("{[]}"))

print(is_valid_parenthesis(""))
