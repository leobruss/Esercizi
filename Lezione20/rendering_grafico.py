from abc import ABC

# Definizione della classe base Forma che estende ABC (Abstract Base Class)
class Forma(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def getArea(self) -> None:
        pass  # Metodo astratto, da implementare nelle classi derivate

    def render(self) -> None:
        pass  # Metodo astratto, da implementare nelle classi derivate

# Classe Quadrato che estende Forma
class Quadrato(Forma):
    def __init__(self, nome: str, lunghezza_lato: int) -> None:
        super().__init__(nome)
        self.lunghezza_lato = lunghezza_lato
        print(f"Il valore del lato del {nome} è pari a {lunghezza_lato}")

    def getArea(self) -> None:
        self.area_quadrato = self.lunghezza_lato ** 2
        print(F"L'area del {self.nome} è pari a {self.area_quadrato}")

    def render(self) -> None:
        # Costruzione della rappresentazione del quadrato con asterischi
        lato_lungo: str = "* " * self.lunghezza_lato
        spazio_vuoto: str = "* " + "  " * (self.lunghezza_lato - 2) + "*\n"
        linee_spazi_vuoti: str = spazio_vuoto * (self.lunghezza_lato - 2)
        if self.lunghezza_lato > 0:
            print(f"{lato_lungo}\n{linee_spazi_vuoti}{lato_lungo}")

# Classe Rettangolo che estende Forma
class Rettangolo(Forma):
    def __init__(self, nome: str, base: int, altezza: int) -> None:
        self.nome = nome
        self.altezza = altezza
        self.base = base
        print(f"Il valore dei lati del {nome} sono pari a:\nBase: {base}\nAltezza: {altezza}")

    def getArea(self) -> None:
        self.area_rettangolo = self.altezza * self.base
        print(F"L'area del {self.nome} è pari a {self.area_rettangolo}")

    def render(self) -> None:
        # Costruzione della rappresentazione del rettangolo con asterischi
        lato_lungo: str = "* " * self.base
        spazio_vuoto: str = "* " + "  " * (self.base - 2) + "*\n"
        linee_spazi_vuoti: str = spazio_vuoto * (self.altezza - 2)
        print(f"{lato_lungo}\n{linee_spazi_vuoti}{lato_lungo}")

# Classe Triangolo che estende Forma
class Triangolo(Forma):
    def __init__(self, nome: str, lunghezza_base: int, lunghezza_altezza: int) -> None:
        super().__init__(nome)
        self.lunghezza_base = lunghezza_base
        self.lunghezza_altezza = lunghezza_altezza

    def getArea(self) -> None:
        self.area_triangolo = (self.lunghezza_base * self.lunghezza_altezza) / 2
        print(F"L'area del {self.nome} è pari a {self.area_triangolo}")

    def render(self) -> None:
        # Costruzione della rappresentazione del triangolo con asterischi
        for a in range(self.lunghezza_altezza):
            for b in range(self.lunghezza_base):
                if a == self.lunghezza_altezza - 1 or a == b or b == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

# Creazione e test delle istanze
quadrato1: Quadrato = Quadrato("quadrato", 4)
quadrato1.getArea()
quadrato1.render()

print()
print("--*--" * 36)
print()

rettangolo1: Rettangolo = Rettangolo("rettangolo", 8, 4)
rettangolo1.getArea()
rettangolo1.render()

print()
print("--*--" * 36)
print()

triangolo1: Triangolo = Triangolo("triangolo", 10, 10)
triangolo1.getArea()
triangolo1.render()
