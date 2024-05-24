class Film:
    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero_identificativo: int, film: Film, posti_totali: int) -> None:
        self.numero_identificativo = numero_identificativo
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int) -> str:
        if num_posti <= self.posti_disponibili():
            return f"Vi confermiamo la disponibilità dei posti n.{num_posti}"
        else:
            return "Ci dispiace ma non c'è disponibilità dei posti"


    def posti_disponibili(self) -> int:
        return self.posti_totali - self.posti_prenotati
        

class Cinema:
    def __init__(self) -> list:
        self.sala: list[Sala] = []
        
    def aggiungi_sala(self, sala: Sala) -> int:
        self.sala.append(sala)
        
    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        self.titolo_film = titolo_film
        for s in self.sala:
            if titolo_film == s.film.titolo:
                if s.posti_disponibili() >= num_posti:
                    print(f"Prenotazione de posti per il film {titolo_film} completata")
                    return s.prenota_posti(num_posti)
                else:
                    print(f"Numero di posti per il film {titolo_film} non disponibile")
                    return s.prenota_posti(num_posti)
        return "Film non disponibile"
        
    def presentazione(self) -> str:
        return f"Sala {self.sala}\n\tFilm in programma: {self.titolo_film}\nDurata film: {self.sala[0].film.durata}"
        






cinema = Cinema()
film1: Film = Film("Avengers", 143)
film2: Film = Film("Interstellar", 169)
film3: Film = Film("Dune", 155)

sala1: Sala = Sala(1, film1, 50)
sala2: Sala = Sala(1, film2, 70)
sala3: Sala = Sala(1, film3, 40)


cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)
cinema.aggiungi_sala(sala3)
print(cinema.prenota_film("Avengers", 20))

print("\n")
print(cinema.prenota_film("Interstellar", 80))
print("\n")
print(cinema.prenota_film("Dune", 20))