class Specie:
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
       self.nome = nome
       self.popolazione = popolazione
       self.tasso_crescita = tasso_crescita

    def cresci(self) ->None:
        self.popolazione *= (1 + (self.tasso_crescita / 100)) 

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        while self.popolazione <= altra_specie.popolazione and anni < 1000:
           self.cresci() 
           altra_specie.cresci()
           if self.popolazione > altra_specie.popolazione:
                break
           anni += 1
        return anni

    def getDensita(self, area_kmq: float) -> int: 
        densita = self.popolazione / area_kmq
        anni = 0
        while densita < 1 and anni < 1000:
            self.cresci()
            densita = self.popolazione / area_kmq
            if densita >= 1:
                break
            anni += 1
        return anni



class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float) -> None:
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float) -> None:
        super().__init__("Elefante", popolazione, tasso_crescita)