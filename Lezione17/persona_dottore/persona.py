class Persona:
    def __init__(self, _first_name: str, _last_name:str) -> None:
        if isinstance(_first_name, str):
            self._first_name = _first_name
        else:
            self._first_name = None 

        if isinstance(_last_name, str):
            self._last_name = _last_name
        else:
            self._last_name = None 

        if isinstance(_first_name, str) and isinstance(_last_name, str):
            self._age = 0
        else:
            self._age = None

    def setName(self, first_name: str) ->None:
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name: str) ->None:
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age: int) ->None:
        if isinstance(age, int):
            self._age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self) ->str:
        return self._first_name
    
    def getLastname(self) ->str:
        return self._last_name
    
    def getAge(self) ->str:
        return self._age
    
    def greet(self) ->str:
        print(f"Ciao, sono {self.getName()} {self.getLastname()}! Ho età {self.getAge()}!")
            





