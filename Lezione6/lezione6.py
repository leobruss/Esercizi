class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        '''
        
        '''
        self.__name: str = name
        self.__surname: str = surname
        self.birth_date: str = birth_date
        self.birth_place: str = birth_place
        self.gender: str = gender
        self.__ssn: str = self.compute__ssn()
    def get__ssn(self) -> None:
        '''
        This function returns the ssn  the ssn name
        input: none
        return: self._ssn str, this function returns  the ssn value
        '''

        return self.__ssn
    
    def set__ssn(self, ssn: str) -> None:
        '''
        This function returns the ssn  the ssn
        input: self._ssn str, this parametere contains the user's snn
        return: none
        '''
        self._snn = ssn
    
    def get__name(self):
        '''
        This function returns a person's name
        input: none
        return: self._name: str, this function returns person's name 
        '''
        return self.__name
    
    def set__name(self, name:str) -> None:
        '''
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        Return: None
        '''
        self.__name = name
        self.__ssn = self.compute__ssn
    
    def get__surname(self):
        '''
        This function returns a person's name
        input: none
        return: self._name: str, this function returns person's name 
        '''
        return self.__surname
    
    def set__surname(self, surname:str) -> None:
        '''
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        Return: None
        '''
        raise Exception("You cannot modify the surname!")
    def compute__ssn(self) -> str:
        '''
        Check the ssn's correction
        '''

        first_three_name_char = self.__name
        vocali: str = "AEIOU"
        consonanti:str = "BCDFGHJKLMNPQRSTVWXYZ"
        counter1 = 0
        counter2 = 0
        consonanti_accettate_nome: str = ""
        #calcolo le prime 3 consonanti del nome
        for char in first_three_name_char.upper():
            if char in consonanti:
                counter1 += 1
                consonanti_accettate_nome += char
        if len(consonanti_accettate_nome) == 3 :
            consonanti_accettate_nome = consonanti_accettate_nome
        if len(consonanti_accettate_nome) > 3 :
            consonanti_accettate_nome = consonanti_accettate_nome[0] + consonanti_accettate_nome[2] + consonanti_accettate_nome[3]
        consonanti_mancanti = 3 - len(consonanti_accettate_nome)
        #se le consonanti sono minori di 3 pasa alle vocali 
        for char in first_three_name_char.upper():
            if char in vocali:
                counter2 += 1
                if counter2 <= consonanti_mancanti:
                    consonanti_accettate_nome += char
        lettere_mancanti = 3 - len(consonanti_accettate_nome)
        #se anche le vocali non sono abbastanza aggiunge le x
        for i in range(0, lettere_mancanti):
            consonanti_accettate_nome += "X"
        


        first_three_surname_char = self.__surname
        vocali: str = "AEIOU"
        consonanti:str = "BCDFGHJKLMNPQRSTVWXYZ"
        counter1 = 0
        counter2 = 0
        consonanti_accettate_cognome: str = ""
        #calcolo le prime 3 consonanti del cognome
        for char in first_three_surname_char.upper():
            if char in consonanti:
                counter1 += 1
                consonanti_accettate_cognome += char
        if len(consonanti_accettate_cognome) == 3 :
            consonanti_accettate_cognome = consonanti_accettate_cognome
        if len(consonanti_accettate_cognome) > 3 :
            consonanti_accettate_cognome =  consonanti_accettate_cognome[0] + consonanti_accettate_cognome[1] + consonanti_accettate_cognome[2]
        consonanti_mancanti = 3 - len(consonanti_accettate_cognome)
         #se le consonanti sono minori di 3 pasa alle vocali
        for char in first_three_surname_char.upper():
            if char in vocali:
                counter2 += 1
                if counter2 <= consonanti_mancanti:
                    consonanti_accettate_cognome += char
        lettere_mancanti = 3 - len(consonanti_accettate_cognome)
        #se anche le vocali non sono abbastanza aggiunge le x
        for i in range(0, lettere_mancanti):
            consonanti_accettate_cognome += "X"

        #ora calcolo on base al mese di nascita la lettera che va messa dopo le ultime 2 cifre dell'anno di nascita
        birth_month= self.birth_date[3:5]
        month: dict = {
            "01" : "A",  
            "02" : "B",
            "03" : "B",
            "04" : "D",
            "05" : "E",
            "06" : "H",
            "07" : "L",
            "08" : "M",
            "09" : "P",
            "10" : "R",
            "11" : "S",
            "12" : "T"
        }
        month_letter: str = month[birth_month]
       
                

        return consonanti_accettate_cognome + consonanti_accettate_nome + self.birth_date[-2:] + month_letter
       
person_1 : Person = Person(name="Leonardo", surname="Brussani", birth_date="24/07/2004", birth_place="Rome", gender="Male")


'''queue: list[Person] = [person_1, person_2]
for person in queue:
    print(person.get__ssn())'''

print(person_1.get__name())
print(person_1.get__surname())
print(person_1.get__ssn())
#print(person_1.__name, person_1.__surname, person_1.__ssn)
