class Prodotto:
    def __init__(self, nome: str, quantita: int) -> None:
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self) -> None:
        self.magazzino = []

    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        self.prodotto = prodotto
        for m in self.magazzino:
            if m.nome == prodotto.nome:
                m.quantita += prodotto.quantita
                return
        self.magazzino.append(prodotto)
        
    def cerca_prodotto(self, nome: str) -> Prodotto:
        for m in self.magazzino:
            if m.nome == nome:
                return f"Prodotto:{m.nome}\nQuantità: {m.quantita}"
        return "Prodotto non trovato"
                

    def verifica_disponibilità(self, nome: str) -> str: 
        for prodotto in self.magazzino:
            if prodotto.nome == nome:
                return f"Il prodotto {prodotto.nome} è disponibile in magazzino"
        return f"Il prodotto {prodotto.nome} non è disponibile in magazzino"
            
prodotto1: Prodotto = Prodotto("Pizza", 2)
prodotto2: Prodotto = Prodotto("Pasta", 5)
magazzino: Magazzino = Magazzino()

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)


print(magazzino.cerca_prodotto("Pizza"))
print(magazzino.verifica_disponibilità("Pizza"))
print("\n")
print(magazzino.cerca_prodotto("Pasta"))
print(magazzino.verifica_disponibilità("Pasta"))


