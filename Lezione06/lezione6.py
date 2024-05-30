class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        """
        
        """
        self.__name: str = name
        self.__surname: str = surname
        self.birth_date: str = birth_date
        self.birth_place: str = birth_place
        self.gender: str = gender
        self.__ssn: str = self.compute__ssn()
    def get__ssn(self) -> None:
        """
        This function returns the ssn  the ssn name
        input: none
        return: self._ssn str, this function returns  the ssn value
        """

        return self.__ssn
    
    def set__ssn(self, ssn: str) -> None:
        """
        This function returns the ssn  the ssn
        input: self._ssn str, this parametere contains the user"s snn
        return: none
        """
        self._snn = ssn
    
    def get__name(self):
        """
        This function returns a person"s name
        input: none
        return: self._name: str, this function returns person"s name 
        """
        return self.__name
    
    def set__name(self, name:str) -> None:
        """
        This function set the attribute name
        input: name: str, the parameter contains the user"s name
        Return: None
        """
        self.__name = name
        self.__ssn = self.compute__ssn
    
    def get__surname(self):
        """
        This function returns a person"s name
        input: none
        return: self._name: str, this function returns person"s name 
        """
        return self.__surname
    
    def set__surname(self, surname:str) -> None:
        """
        This function set the attribute name
        input: name: str, the parameter contains the user"s name
        Return: None
        """
        raise Exception("You cannot modify the surname!")
    def compute__ssn(self) -> str:
        """
        Check the ssn"s correction
        """

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

        #ora calcolo on base al mese di nascita la lettera che va messa dopo le ultime 2 cifre dell"anno di nascita
        birth_month: str = self.birth_date[3:5]
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

        gender = self.gender
        birth_day:str = self.birth_date[0:2]
        if gender.upper() == "F":
            birth_day = int(birth_day) + 40
            birth_day =  str(birth_day)

        birth_place = self.birth_place
        cadastral_codes: dict = {"Ancona":"A271","Aosta":"A326","L'Aquila":"A345","Roma":"H501",
                                     "Bologna":"A944","Cagliari":"B354","Campobasso":"B519",
                                     "Catanzaro":"C352","Firenze":"D612","Genova":"D969",
                                     "Milano":"F205","Napoli":"F839","Palermo":"G273","Bari":"A662",
                                     "Perugia":"G478","Potenza":"G942","Torino":"L219",
                                     "Trento":"L378","Trieste":"L424","Venezia":"L736"}  
        birth_place= cadastral_codes[birth_place]    

        codice_fiscale_parziale = consonanti_accettate_cognome + consonanti_accettate_nome + self.birth_date[-2:] + month_letter + birth_day + birth_place

        codice_fiscale = ""
       
        even_nums: dict = {
            " ": " ",
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
            "J": 9,
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "K": 10,
            "L": 11,
            "M": 12,
            "N": 13,
            "O": 14,
            "P": 15,
            "Q": 16,
            "R": 17,
            "S": 18,
            "T": 19,
            "U": 20,
            "V": 21,
            "W": 22,
            "X": 23,
            "Y": 24,
            "Z": 25
        }

        odd_nums = {
            " ": " ",
            "A": 1,
            "B": 0,
            "C": 5,
            "D": 7,
            "E": 9,
            "F": 13,
            "G": 15,
            "H": 17,
            "I": 19,
            "J": 21,
            "0": 1,
            "1": 0,
            "2": 5,
            "3": 7,
            "4": 9,
            "5": 13,
            "6": 15,
            "7": 17,
            "8": 19,
            "9": 21,
            "K": 2,
            "L": 4,
            "M": 18,
            "N": 20,
            "O": 11,
            "P": 3,
            "Q": 6,
            "R": 8,
            "S": 12,
            "T": 14,
            "U": 16,
            "V": 10,
            "W": 22,
            "X": 25,
            "Y": 24,
            "Z": 23
        }

        control_digits: dict = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H",
            8: "I",
            9: "J",
            10: "K",
            11: "L",
            12: "M",
            13: "N",
            14: "O",
            15: "P",
            16: "Q",
            17: "R",
            18: "S",
            19: "T",
            20: "U",
            21: "V",
            22: "W",
            23: "X",
            24: "Y",
            25: "Z"
        }

        sum_odd = 0
        for i in range(0,15,2):
            sum_odd += odd_nums[codice_fiscale_parziale[i]]

        sum_even = 0
        for i in range(1,15,2):
            sum_even += even_nums[codice_fiscale_parziale[i]]

        rest = (sum_odd + sum_even) % 26
        
        if rest in control_digits:
            codice_fiscale_parziale += str(control_digits[rest])
            codice_fiscale = codice_fiscale_parziale
        return codice_fiscale
        
                
       
person_1 : Person = Person(name="Leonardo", surname="Brussani", birth_date="24/07/2004", birth_place="Roma", gender="M")


print("Name: ", person_1.get__name())
print("Surname: ", person_1.get__surname())
print("Date of birth: ", person_1.birth_date)
print("Place of birth: ", person_1.birth_place)
print("Your gender: ", person_1.gender)
print(person_1.get__name(), person_1.get__surname(), "your ssn is: ", person_1.get__ssn())
