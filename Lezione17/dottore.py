from persona import Persona
class Dottore(Persona):
    def __init__(self, _first_name: str, _last_name: str, _specialization: str, _parcel:float) -> None:
        super().__init__(_first_name, _last_name)

        if isinstance(_specialization, str):
            self._specialization = _specialization
        else: 
            self._specialization = None
            print("La specializzazione  inserita non è una stringa!")

        if isinstance(_parcel, float):
            self._parcel = _parcel
        else: 
            self._parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization: str) ->None:
        if isinstance(specialization, str):
            self._specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float) ->None:
        if isinstance(parcel, float):
             self._parcel = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self) ->str:
        return self._specialization
    
    def getParcel(self) ->float:
        return self._parcel
    
    def isAValidDoctor(self) ->str:
        if self._age > 30:
            print(f"Doctor {self.getName()} e {self.getLastname()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} e {self.getLastname()} is not valid!")
            return False

        
    def doctorGreet(self) ->str:
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")



    

