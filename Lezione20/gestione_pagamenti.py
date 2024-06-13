# Definizione della classe base 'Pagamento'
class Pagamento:
    def __init__(self) -> None:
        # Attributo privato per memorizzare l'importo del pagamento
        self._pagamento: float = None  

    def set_pagamento(self, valore: float) -> None:
        # Metodo per impostare l'importo del pagamento

        self._pagamento = valore  
    def get_pagamento(self) -> float:
        # Metodo per ottenere l'importo del pagamento
        return self._pagamento  

    def dettagliPagamento(self) -> str:
        # Metodo per ottenere una stringa con i dettagli del pagamento
        return f"Importo del pagamento: €{self._pagamento}"  

# Definizione della classe 'PagamentoContanti' che eredita da 'Pagamento'
class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()  # Chiama il costruttore della classe base

    def dettagliPagamento(self) -> str:
        # Stampa i dettagli del pagamento in contanti
        print(f"Pagamento in contanti di: €{self._pagamento}")  
        # Chiama il metodo per calcolare e stampare la divisione in pezzi
        self.inPezziDa()  

    # Dizionario con i tagli delle banconote e monete in euro
    def inPezziDa(self) -> str:
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

        # Ottiene l'importo del pagamento
        importo_restante = self.get_pagamento()  

        # Dizionario per memorizzare il numero di pezzi di ogni taglio
        pezzi_banconote = {}  

         # Itera sui tagli delle banconote e monete
        for pezzi, valori in valori_euro.items(): 
             # Calcola il numero di pezzi per ogni taglio
            numero_pezzi = int(importo_restante // valori)

            if importo_restante > 0 and numero_pezzi > 0:
                # Memorizza il numero di pezzi
                pezzi_banconote[pezzi] = numero_pezzi  
                
                # Stampa il numero di pezzi
                print(f"{numero_pezzi} banconote da {pezzi}")  

                # Aggiorna l'importo restante
            importo_restante = round(importo_restante - numero_pezzi * valori, 2) 

# Definizione della classe 'PagamentoCartaDiCredito' che eredita da 'Pagamento'
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome: str, data_scadenza: str, numero_di_carta: int) -> None:
        super().__init__()  # Chiama il costruttore della classe base
         # Inizializza il nome del titolare della carta
        self.nome = nome 
        # Inizializza la data di scadenza della carta
        self.data_scadenza = data_scadenza  
        # Inizializza il numero della carta
        self.numero_di_carta = numero_di_carta  

    def dettagliPagamento(self) -> str:
        print(f"Pagamento di: €{self.get_pagamento()} effettuato con la carta di credito\nNome sulla carta: {self.nome}\nData di scadenza: {self.data_scadenza}\nNumero della carta: {self.numero_di_carta}")  # Stampa i dettagli del pagamento con carta di credito

# Creazione di un'istanza della classe 'PagamentoContanti'
pagamento_contanti1: PagamentoContanti = PagamentoContanti()

 # Imposta l'importo del pagamento
pagamento_contanti1.set_pagamento(95.25) 

# Stampa i dettagli del pagamento e la divisione in pezzi
pagamento_contanti1.dettagliPagamento()  

print()

# Creazione di un'altra istanza della classe 'PagamentoContanti'
pagamento_contanti2: PagamentoContanti = PagamentoContanti()

# Imposta l'importo del pagamento
pagamento_contanti2.set_pagamento(215.35)  

 # Stampa i dettagli del pagamento e la divisione in pezzi
pagamento_contanti2.dettagliPagamento() 

print()
print("--*--" * 36)
print()

# Creazione di un'istanza della classe 'PagamentoCartaDiCredito'
pagamento_carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Leonardo Brussani", "24/07", 2365489514782365)

# Imposta l'importo del pagamento
pagamento_carta1.set_pagamento(450)  

# Stampa i dettagli del pagamento con carta di credito
pagamento_carta1.dettagliPagamento()  

print()
print("--*--" * 36)
print()

# Creazione di un'altra istanza della classe 'PagamentoCartaDiCredito'
pagamento_carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Matteo Cardelli", "10/03", 14725642314865749)

# Imposta l'importo del pagamento
pagamento_carta2.set_pagamento(50)  

# Stampa i dettagli del pagamento con carta di credito
pagamento_carta2.dettagliPagamento()  

 