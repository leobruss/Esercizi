#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from biblioteca import Biblioteca, Libro, Autore, Categoria
import time

def test_sistema_biblioteca():
    """Test completo del sistema biblioteca digitale."""
    
    print("=" * 60)
    print("\t\tTEST SISTEMA BIBLIOTECA DIGITALE")
    print("=" * 60)
    
    # Creazione biblioteca
    biblioteca = Biblioteca("Biblioteca Comunale di Roma")
    print(f"\n✓ Creata {biblioteca.nome}")
    
    # Creazione autori
    autori = [
        Autore("Umberto", "Eco", 1932),
        Autore("Italo", "Calvino", 1923),
        Autore("Elena", "Ferrante", 1943),
        Autore("Alessandro", "Manzoni", 1785),
        Autore("Dante", "Alighieri", 1265)
    ]
    
    # Creazione categorie
    categorie = [
        Categoria("Narrativa", "Romanzi e racconti di finzione"),
        Categoria("Classici", "Opere della letteratura classica"),
        Categoria("Saggistica", "Opere di carattere critico e divulgativo"),
        Categoria("Poesia", "Raccolte poetiche e opere in versi")
    ]
    
    # Creazione libri
    libri = [
        Libro("9788845292613", "Il nome della rosa", autori[0], categorie[0], 1980, 624),
        Libro("9788804668275", "Se una notte d'inverno un viaggiatore", autori[1], categorie[0], 1979, 286),
        Libro("9788866327803", "L'amica geniale", autori[2], categorie[0], 2011, 331),
        Libro("9788817071175", "I promessi sposi", autori[3], categorie[1], 1827, 712),
        Libro("9788804472131", "La Divina Commedia", autori[4], categorie[3], 1320, 798),
        Libro("9788845280801", "Il pendolo di Foucault", autori[0], categorie[2], 1988, 623),
        Libro("9788804465928", "Le città invisibili", autori[1], categorie[0], 1972, 164)
    ]
    
    # Aggiunta libri alla biblioteca
    print("\n✓ Aggiunta di libri alla biblioteca:")
    for libro in libri:
        if biblioteca.aggiungi_libro(libro):
            print(f"  + {libro.titolo} di {libro.autore.nome_completo()}")
    
    # Statistiche iniziali
    print("\n" + "="*50)
    print("STATISTICHE INIZIALI")
    print("="*50)
    print(biblioteca)
    
    stats = biblioteca.statistiche()
    print(f"\nDettagli:")
    print(f"- Autori registrati: {stats['totale_autori']}")
    print(f"- Categorie disponibili: {stats['totale_categorie']}")
    
    # Test delle categorie più popolari
    print("\nCategorie più popolari:")
    for categoria, count in biblioteca.top_categorie():
        print(f"  {categoria}: {count} libri")
    
    # Test ricerca
    print("\n" + "="*50)
    print("TEST FUNZIONI DI RICERCA")
    print("="*50)
    
    # Ricerca per titolo
    print("\n1. Ricerca per titolo 'Il':")
    risultati = biblioteca.cerca_per_titolo("Il")
    for libro in risultati:
        print(f"  - {libro}")
    
    # Ricerca per autore
    print("\n2. Ricerca per autore 'Eco':")
    risultati = biblioteca.cerca_per_autore("Eco")
    for libro in risultati:
        print(f"  - {libro}")
    
    # Ricerca per categoria
    print("\n3. Ricerca per categoria 'Narrativa':")
    risultati = biblioteca.cerca_per_categoria("Narrativa")
    for libro in risultati:
        print(f"  - {libro}")
    
    # Test sistema prestiti
    print("\n" + "="*50)
    print("TEST SISTEMA PRESTITI")
    print("="*50)
    
    # Prestito di alcuni libri
    prestiti_test = [
        ("9788845292613", "Mario Rossi", 14),
        ("9788804668275", "Anna Verdi", 7),
        ("9788866327803", "Luca Bianchi", 21)
    ]
    
    print("\nEsecuzione prestiti:")
    for isbn, utente, giorni in prestiti_test:
        libro = biblioteca.cerca_per_isbn(isbn)
        if libro and libro.presta(utente, giorni):
            print(f"  ✓ Prestato '{libro.titolo}' a {utente} per {giorni} giorni")
            print(f"    Scadenza: {libro.data_scadenza.strftime('%d/%m/%Y %H:%M')}")
        else:
            print(f"  ✗ Impossibile prestare il libro con ISBN {isbn}")
    
    # Verifica stato prestiti
    print("\nStato attuale dei prestiti:")
    libri_prestito = biblioteca.libri_in_prestito()
    for libro in libri_prestito:
        giorni_rim = libro.giorni_rimasti()
        status = "IN RITARDO" if libro.is_in_ritardo() else f"{giorni_rim} giorni rimasti"
        print(f"  - {libro.titolo} → {libro.utente_prestito} ({status})")
    
    # Test restituzione
    print("\nRestituzione del libro 'Il nome della rosa':")
    libro_da_restituire = biblioteca.cerca_per_isbn("9788845292613")
    if libro_da_restituire and libro_da_restituire.restituisci():
        print(f"  ✓ '{libro_da_restituire.titolo}' restituito con successo")
    
    # Statistiche finali
    print("\n" + "="*50)
    print("STATISTICHE FINALI")
    print("="*50)
    print(biblioteca)
    
    print("\n✓ Test completato con successo!")
    
    # Mostra tutti i libri disponibili
    print("\nLibri attualmente disponibili per il prestito:")
    disponibili = biblioteca.libri_disponibili()
    for libro in disponibili:
        print(f"  • {libro.titolo} ({libro.autore.nome_completo()})")

def demo_interattiva():
    """Breve demo interattiva del sistema."""
    
    print("\n" + "="*60)
    print("\t\tDEMO INTERATTIVA")
    print("="*60)
    
    # Creazione rapida di una biblioteca
    biblioteca = Biblioteca("Biblioteca Demo")
    
    # Aggiunta di alcuni libri
    autore1 = Autore("George", "Orwell", 1903)
    categoria1 = Categoria("Distopia")
    libro1 = Libro("9780451524935", "1984", autore1, categoria1, 1949, 328)
    
    biblioteca.aggiungi_libro(libro1)
    
    print(f"Libro aggiunto: {libro1}")
    
    # Test prestito
    if libro1.presta("Utente Demo", 10):
        print(f"\n✓ Libro prestato a 'Utente Demo'")
        print(f"Giorni rimasti: {libro1.giorni_rimasti()}")
        print(f"Data scadenza: {libro1.data_scadenza.strftime('%d/%m/%Y')}")
    
    # Simulazione passaggio del tempo (solo per demo)
    print("\n[Simulazione: passano alcuni giorni...]")
    time.sleep(1)
    
    print(f"Giorni rimasti aggiornati: {libro1.giorni_rimasti()}")
    print(f"Il libro è in ritardo? {libro1.is_in_ritardo()}")

def main():
    """Funzione principale per eseguire tutti i test."""
    try:
        test_sistema_biblioteca()
        demo_interattiva()
        
        print("\n" + "="*60)
        print("✓ TUTTI I TEST SUPERATI CON SUCCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\n✗ ERRORE durante l'esecuzione: {e}")
        print("Verifica il codice e riprova.")

if __name__ == "__main__":
    main()
