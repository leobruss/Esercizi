class Pagamento:
    def __init__(self) -> None:
        self._pagamento: float = None

    def set_pagamento(self, valore: float) ->None:
        self._pagamento = valore

    def get_pagamento(self) ->float:
        return self._pagamento

    def dettagliPagamento(self) ->str:
        return f"Importo del pagamento: €{self._pagamento}"  


class PagamentoContanti (Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self) -> str:
        print(f"Pagamento in contanti di: €{self._pagamento}")
        self.inPezziDa()

    def inPezziDa(self) ->str:
        valori_euro = {
            '500€': 500,
            '200€': 200,
            '100€': 100,
            '50€': 50,
            '20€': 20,
            '10€': 10,
            '5€': 5,
            '2€': 2,
            '1€': 1,
            '0,50€': 0.50,
            '0,20€': 0.20,
            '0,10€': 0.10,
            '0,05€': 0.05,
            '0,01€': 0.01
        } 

        importo_restante = self.get_pagamento()
        pezzi_banconote = {}
        for pezzi, valori in valori_euro.items():
            numero_pezzi = int(importo_restante // valori)
            if importo_restante > 0 and numero_pezzi > 0:
                pezzi_banconote[pezzi] = numero_pezzi
                print(f"{numero_pezzi} banconote da {pezzi}")
            importo_restante = round(importo_restante - numero_pezzi * valori, 2)
            
    

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome: str, data_scadenza: str, numero_di_carta: int) -> None:
        super().__init__()
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero_di_carta = numero_di_carta

    def dettagliPagamento(self) -> str:
        print(f"Pagamento di: €{self.get_pagamento()} effettuato con la carta di credito\nNome sulla carta: {self.nome}\nData di scadenza: {self.data_scadenza}\nNumero della carta: {self.numero_di_carta}")
    





pagamento_contanti1: PagamentoContanti = PagamentoContanti()
pagamento_contanti1.set_pagamento(95.25)
pagamento_contanti1.dettagliPagamento()
print()

pagamento_contanti2: PagamentoContanti = PagamentoContanti()
pagamento_contanti2.set_pagamento(215.35)
pagamento_contanti2.dettagliPagamento()
print()

pagamento_carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Leonardo Brussani", "24/07", 2365489514782365)
pagamento_carta1.set_pagamento(450)
pagamento_carta1.dettagliPagamento()
print()

pagamento_carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Matteo Cardelli", "10/03", 14725642314865749)
pagamento_carta2.set_pagamento(50)
pagamento_carta2.dettagliPagamento()
