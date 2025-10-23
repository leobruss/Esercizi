from datetime import datetime, timedelta
from typing import List, Optional, Dict

class Autore:
    """Classe per rappresentare un autore."""
    
    def __init__(self, nome: str, cognome: str, anno_nascita: int):
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita
    
    def nome_completo(self) -> str:
        return f"{self.nome} {self.cognome}"
    
    def __str__(self) -> str:
        return f"{self.nome_completo()} ({self.anno_nascita})"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Autore):
            return (self.nome == other.nome and 
                   self.cognome == other.cognome and 
                   self.anno_nascita == other.anno_nascita)
        return False

class Categoria:
    """Classe per rappresentare una categoria di libri."""
    
    def __init__(self, nome: str, descrizione: str = ""):
        self.nome = nome
        self.descrizione = descrizione
    
    def __str__(self) -> str:
        return self.nome
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome == other.nome
        return False

class Libro:
    """Classe per rappresentare un libro."""
    
    def __init__(self, isbn: str, titolo: str, autore: Autore, 
                 categoria: Categoria, anno_pubblicazione: int, pagine: int):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.categoria = categoria
        self.anno_pubblicazione = anno_pubblicazione
        self.pagine = pagine
        self.disponibile = True
        self.data_prestito = None
        self.data_scadenza = None
        self.utente_prestito = None
    
    def presta(self, utente: str, giorni_prestito: int = 14) -> bool:
        """Presta il libro a un utente per un numero specificato di giorni."""
        if not self.disponibile:
            return False
        
        self.disponibile = False
        self.utente_prestito = utente
        self.data_prestito = datetime.now()
        self.data_scadenza = self.data_prestito + timedelta(days=giorni_prestito)
        return True
    
    def restituisci(self) -> bool:
        """Restituisce il libro alla biblioteca."""
        if self.disponibile:
            return False
        
        self.disponibile = True
        self.utente_prestito = None
        self.data_prestito = None
        self.data_scadenza = None
        return True
    
    def is_in_ritardo(self) -> bool:
        """Verifica se il libro è in ritardo."""
        if self.disponibile or self.data_scadenza is None:
            return False
        return datetime.now() > self.data_scadenza
    
    def giorni_rimasti(self) -> Optional[int]:
        """Restituisce i giorni rimanenti prima della scadenza."""
        if self.disponibile or self.data_scadenza is None:
            return None
        
        differenza = self.data_scadenza - datetime.now()
        return max(0, differenza.days)
    
    def __str__(self) -> str:
        status = "Disponibile" if self.disponibile else f"In prestito a {self.utente_prestito}"
        return f"\"{self.titolo}\" di {self.autore.nome_completo()} ({self.anno_pubblicazione}) - {status}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Libro):
            return self.isbn == other.isbn
        return False

class Biblioteca:
    """Classe principale per gestire la biblioteca digitale."""
    
    def __init__(self, nome: str):
        self.nome = nome
        self.libri: List[Libro] = []
        self.autori: List[Autore] = []
        self.categorie: List[Categoria] = []
    
    def aggiungi_autore(self, autore: Autore) -> bool:
        """Aggiunge un autore se non esiste già."""
        if autore not in self.autori:
            self.autori.append(autore)
            return True
        return False
    
    def aggiungi_categoria(self, categoria: Categoria) -> bool:
        """Aggiunge una categoria se non esiste già."""
        if categoria not in self.categorie:
            self.categorie.append(categoria)
            return True
        return False
    
    def aggiungi_libro(self, libro: Libro) -> bool:
        """Aggiunge un libro alla biblioteca."""
        if libro in self.libri:
            return False
        
        # Aggiungi automaticamente autore e categoria se non esistono
        self.aggiungi_autore(libro.autore)
        self.aggiungi_categoria(libro.categoria)
        
        self.libri.append(libro)
        return True
    
    def cerca_per_titolo(self, titolo: str) -> List[Libro]:
        """Cerca libri per titolo (ricerca parziale, case-insensitive)."""
        titolo_lower = titolo.lower()
        return [libro for libro in self.libri 
                if titolo_lower in libro.titolo.lower()]
    
    def cerca_per_autore(self, nome_autore: str) -> List[Libro]:
        """Cerca libri per nome autore (ricerca parziale, case-insensitive)."""
        nome_lower = nome_autore.lower()
        return [libro for libro in self.libri 
                if nome_lower in libro.autore.nome_completo().lower()]
    
    def cerca_per_categoria(self, categoria: str) -> List[Libro]:
        """Cerca libri per categoria."""
        categoria_lower = categoria.lower()
        return [libro for libro in self.libri 
                if categoria_lower in libro.categoria.nome.lower()]
    
    def cerca_per_isbn(self, isbn: str) -> Optional[Libro]:
        """Cerca un libro specifico per ISBN."""
        for libro in self.libri:
            if libro.isbn == isbn:
                return libro
        return None
    
    def libri_disponibili(self) -> List[Libro]:
        """Restituisce tutti i libri disponibili."""
        return [libro for libro in self.libri if libro.disponibile]
    
    def libri_in_prestito(self) -> List[Libro]:
        """Restituisce tutti i libri attualmente in prestito."""
        return [libro for libro in self.libri if not libro.disponibile]
    
    def libri_in_ritardo(self) -> List[Libro]:
        """Restituisce tutti i libri in ritardo."""
        return [libro for libro in self.libri if libro.is_in_ritardo()]
    
    def statistiche(self) -> Dict[str, int]:
        """Genera statistiche sulla biblioteca."""
        return {
            'totale_libri': len(self.libri),
            'libri_disponibili': len(self.libri_disponibili()),
            'libri_in_prestito': len(self.libri_in_prestito()),
            'libri_in_ritardo': len(self.libri_in_ritardo()),
            'totale_autori': len(self.autori),
            'totale_categorie': len(self.categorie)
        }
    
    def top_categorie(self) -> List[tuple]:
        """Restituisce le categorie più popolari (nome, numero_libri)."""
        conteggio_categorie = {}
        for libro in self.libri:
            nome_cat = libro.categoria.nome
            conteggio_categorie[nome_cat] = conteggio_categorie.get(nome_cat, 0) + 1
        
        return sorted(conteggio_categorie.items(), 
                     key=lambda x: x[1], reverse=True)
    
    def __str__(self) -> str:
        stats = self.statistiche()
        return (f"Biblioteca {self.nome}:\n"
                f"- {stats['totale_libri']} libri totali\n"
                f"- {stats['libri_disponibili']} disponibili\n"
                f"- {stats['libri_in_prestito']} in prestito\n"
                f"- {stats['libri_in_ritardo']} in ritardo")
