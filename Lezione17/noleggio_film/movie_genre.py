from film import Film
class Azione(Film):
    def __init__(self, _id: int, _title: str, _genere: str, _penale: float) -> None:
        super().__init__(_id, _title)
        self._genere = _genere
        self._penale = _penale

    def getGenere(self) ->str:
        return self._genere
    
    def getPenale(self) ->float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) ->float:
        self.giorni = giorni
        tot_pagare = self.giorni * 3
        return tot_pagare
    
class Commedia(Film):
    def __init__(self, _id: int, _title: str, _genere: str, _penale: float) -> None:
        super().__init__(_id, _title)
        self._genere = _genere
        self._penale = _penale

    def getGenere(self) ->str:
        return self._genere
    
    def getPenale(self) ->float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) ->float:
        self.giorni = giorni
        tot_pagare = self.giorni * 2.50
        return tot_pagare
    
class Drama(Film):
    def __init__(self, _id: int, _title: str, _genere: str, _penale: float) -> None:
        super().__init__(_id, _title)
        self._genere = _genere
        self._penale = _penale

    def getGenere(self) ->str:
        return self._genere
    
    def getPenale(self) ->float:
        return self._penale
    
    def calcolaPenaleRitardo(self, giorni: int) ->float:
        self.giorni = giorni
        tot_pagare = self.giorni * 2
        return tot_pagare
    
    