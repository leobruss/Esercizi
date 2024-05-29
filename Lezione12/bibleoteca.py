class Libro:
    def __init__(self, titolo:str, autore: str) -> None:
        self.titolo: str = titolo
        self.autore: str = autore
        self.prestato: bool = False
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = []
        
    def aggiungi_libro(self, libro: Libro) -> str:
        self.catalogo.append(libro)
        print(f"Il libro {libro.titolo} è stato aggiunto nel catalogo con successo.")

    def presta_libro(self, titolo: str) -> str: 
        for libro in self.catalogo:
            if titolo == libro.titolo:
                if not libro.prestato:
                    libro.prestato = True
                    return(f"Il libro {titolo} è disponibile ed è stato prestato con successo.")
                else:
                    return(f"Il libro {titolo} non è disponibile.")
        print(f"Libro {titolo} non è all'interno del catalogo.")
    def restituisci_libro(self, titolo: str) -> str:
        for libro in self.catalogo:
            if titolo == libro.titolo:
                if libro.prestato:
                    libro.prestato = False
                    return(f"Il libro {titolo} è stato restituito con successo.")
                else:
                    return(f"Il libro {titolo} è già disponibile.")
        print(F"Libro {titolo} non è all'interno del catalogo.")

    def mostra_libri_disponibili(self) -> str: 
        if self.catalogo:
            return[libro.titolo for libro in self.catalogo if not libro.prestato]
        else:
            raise RuntimeError("Catalogo dei libri vuoto.")
        

biblioteca: Biblioteca = Biblioteca()

libro1: Libro = Libro("Piccolo principe", "Antoine de Saint-Exupéry")
libro2: Libro = Libro("Il signore degli anelli", "J. R. R. Tolkien")
libro3: Libro = Libro("Il fantasma di Canterville", "Oscar Wilde")

biblioteca.aggiungi_libro(libro1)
print()
biblioteca.aggiungi_libro(libro2)
print()
biblioteca.aggiungi_libro(libro3)
print()
print(biblioteca.presta_libro(libro1.titolo))
print()
print(biblioteca.presta_libro(libro3.titolo))
print()
print(biblioteca.restituisci_libro(libro1.titolo))
print()
print("La lista dei titoli disponibili:")
print("\t",biblioteca.mostra_libri_disponibili())