from Esercizi.Lezione17.persona_dottore.dottore import Dottore
from Esercizi.Lezione17.persona_dottore.paziente import Paziente
class Fattura:
    def __init__(self, _patient: list[Paziente], _doctor: Dottore) -> None:
        self._patient = _patient
        self._doctor = _doctor
        if _doctor.isAValidDoctor():
            self._fatture: int = len(_patient)
            self._salry: int = 0
        else:
            self.fatture: int = None
            self.salry: int = None
            self._patient = None
            self._doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalary(self) ->int:
        self._salry = self._doctor._parcel * len(self._patient)
        return self._salry
    
    def getFatture(self) ->int:
        self._fatture = len(self._patient)
        return self._fatture
    
    def addPatient(self, newPatient: Paziente) ->str:
        self._patient.append(newPatient)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor {self._doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}")

    def removePatient(self, idCode: str) ->str:
        for i in self._patient:
            if idCode == i.getidCode():
                self._patient.remove(i)
                self.getSalary()
                self.getFatture()
                break
        print(f"Alla lista del Dottor {self._doctor.getLastname()} è stato rimosso il paziente {idCode}")