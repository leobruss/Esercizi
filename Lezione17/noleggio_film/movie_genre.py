# movie_genre.py
from film import Film

class Azione(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 3.0

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale

    def calcolaPenaleRitardo(self, giorni_ritardo):
        return giorni_ritardo * self.__penale

class Commedia(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Commedia"
        self.__penale = 2.5

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale

    def calcolaPenaleRitardo(self, giorni_ritardo):
        return giorni_ritardo * self.__penale

class Dramma(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self.__genere = "Dramma"
        self.__penale = 2.0

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale

    def calcolaPenaleRitardo(self, giorni_ritardo):
        return giorni_ritardo * self.__penale
