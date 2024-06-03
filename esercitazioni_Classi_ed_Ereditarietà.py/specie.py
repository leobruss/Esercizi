class Specie:
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
       self.nome = nome
       self.popolazione = popolazione
       self.tasso_crescita = tasso_crescita

    def cresci(self) ->None:
        self.popolazione *= (1 + (self.tasso_crescita / 100))
        self.popolazione = int(self.popolazione)

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        while self.popolazione <= altra_specie.popolazione and anni < 1000:
           self.cresci() 
           altra_specie.cresci()
           anni += 1
        return anni

    def getDensita(self, area_kmq: float) -> int: 
        densita = self.popolazione / area_kmq
        anni = 0
        while densita < 1 and anni < 1000:
            self.cresci()
            densita = self.popolazione / area_kmq
            anni += 1
        return anni



class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float) -> None:
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float) -> None:
        super().__init__("Elefante", popolazione, tasso_crescita)


bufalo_klingon = BufaloKlingon(100, 15)
elefante = Elefante(10, 35)

anni_necessari = elefante.anni_per_superare(bufalo_klingon)
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

anni_densita = bufalo_klingon.getDensita(1500)
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")