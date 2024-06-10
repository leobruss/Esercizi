from Esercizi.Lezione17.persona_dottore.persona import *
class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        self._idCode: str = None

    def setIdCode(self, idCode: str) ->None:
        self._idCode = idCode

    def getidCode(self) ->str:
        return self._idCode
    
    def patientInfo(self) ->str:
        print(f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.getidCode()}")
        