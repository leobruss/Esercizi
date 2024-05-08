class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        '''
        
        '''
        self._name: str = name
        self._surname: str = surname
        self.birth_date: str = birth_date
        self.birth_place: str = birth_place
        self.gender: str = gender
        self._ssn: str = self.compute_ssn()
    def get_ssn(self) -> None:
        '''
        This function returns the ssn  the ssn name
        input: none
        return: self._ssn str, this function returns  the ssn value
        '''

        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        '''
        This function returns the ssn  the ssn
        input: self._ssn str, this parametere contains the user's snn
        return: none
        '''
        self._snn = ssn
    
    def get_name(self):
        '''
        This function returns a person's name
        input: none
        return: self._name: str, this function returns person's name 
        '''
        return self._name
    
    def set_name(self, name:str) -> None:
        '''
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        Return: None
        '''
        self._name = name
        self._ssn = self.compute_ssn
    
    def get_surname(self):
        '''
        This function returns a person's name
        input: none
        return: self._name: str, this function returns person's name 
        '''
        return self._surname
    
    def set_surname(self, surname:str) -> None:
        '''
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        Return: None
        '''
        raise Exception("You cannot modify the surname!")
    def compute_ssn(self) -> str:
        '''
        Check the ssn's correction
        '''

        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]
        return first_three_name_char + last_three_surname_char

person_1 : Person = Person(name="Leonardo", surname="Brussasni", birth_date="24/07/2004", birth_place="Rome", gender="Male")


'''queue: list[Person] = [person_1, person_2]
for person in queue:
    print(person.get_ssn())'''

print(person_1.get_name())
print(person_1.get_surname())
print(person_1.get_ssn())
print(person_1._name, person_1._surname, person_1._ssn)
