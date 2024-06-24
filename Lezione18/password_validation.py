
#Password Validation: 
#Write a function validate_password(password) that checks if a password meets certain criteria
#(i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
#Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
import string
def validate_password(password) ->str:
    string_uppercase = string.ascii_uppercase
    string_special = string.punctuation
    variable = 0
    variable1 = 0
    if len(password) < 20:
        raise ShortPassworsd("Password troppo corta")
    for p in password:
        if p in string_uppercase:
            variable += 1
    if variable < 3:
        raise UppercasePassworsd("Numero di Uppercase non esaustivo")
    for p in password:
        if p in string_special:
            variable1 += 1
    if variable1 < 4:
        raise SpecialPassworsd("Numero di caratteri speciali non esaustivo")


class ShortPassworsd(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UppercasePassworsd(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SpecialPassworsd(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

validate_password("NPladf,.,.bsiorsxadrbs")