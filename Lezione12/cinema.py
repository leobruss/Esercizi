class MovieCatalog():
    def __init__(self) -> None:
        self.movies: dict[str, list[str]] = {}
        # Inizializza un nuovo dizionario per memorizzare i film per ogni regista.

    def add_movie(self, director_name: str, movies: list) -> None:
        if director_name not in self.movies:
            self.movies[director_name] = movies
            # Se il regista non è già nel dizionario, aggiungi il regista e la lista di film.
        else:
            self.movies[director_name].append(movies.movie_name)
            # Se il regista è già presente, aggiungi il nome del film alla lista dei suoi film.
        
        for chiave, valore in self.movies.items():
            if isinstance(valore, list):
                print(chiave + ":")
                for elemento in valore:
                    print("- " + str(elemento))
                    # Stampa ogni regista e i suoi film. Questo è più per debug e non è strettamente necessario.

    def remove_movie(self, director_name: str, movie_name: str) -> None:
        if director_name in self.movies:
            if movie_name in self.movies[director_name]:
                self.movies[director_name].remove(movie_name)
                # Rimuovi il film dalla lista del regista.
                if not self.movies[director_name]:
                    del self.movies[director_name]
                    # Se la lista dei film del regista è vuota dopo la rimozione, rimuovi il regista dal dizionario.

        for chiave, valore in self.movies.items():
            if isinstance(valore, list):
                print(chiave + ":")
                for elemento in valore:
                    print("- " + str(elemento))
                    # Stampa ogni regista e i suoi film. Questo è più per debug e non è strettamente necessario.

    def list_directors(self) -> None:
        print(list(self.movies.keys()))
        # Stampa tutti i registi presenti nel catalogo.

    def get_movies_by_director(self, director_name: str) -> list:
        if director_name in self.movies:
            return self.movies[director_name]
        else:
            return f"Il regista {director_name} non è all'interno del catalogo"
        # Stampa i film di un determinato regista.

    def search_movies_by_title(self, title: str) -> None:
        film_list = []

        for director, movies in self.movies.items():
            for movie in movies:
                if title.lower() in movie.lower():
                    film_list.append((director, movie))
                    # Cerca film che contengono la parola chiave nel titolo e aggiungi il regista e il film trovati alla lista.

        if film_list:
            return film_list
            # Se sono stati trovati dei film, restituisci la lista.
        else:
            raise RuntimeError("Film non trovato")
            # Se nessun film è stato trovato, solleva un'eccezione.

# Creazione di un'istanza di MovieCatalog
film: MovieCatalog = MovieCatalog()

# Aggiunta di film di Stanley Kubrick al catalogo
film.add_movie("Stanley Kubrick", ["Shining", "Paura e desiderio", "Barry Lyndon"])
print()

# Aggiunta di film di Christopher Nolan al catalogo
film.add_movie("Christopher Nolan", ["Oppenheimer ", "Inception", "Il cavaliere oscuro", "Interstellar"])
print()

# Rimozione di un film di Stanley Kubrick dal catalogo
film.remove_movie("Stanley Kubrick", "Paura e desiderio")
print()

# Elenco dei registi nel catalogo
film.list_directors()
print()

# Ottenere i film di Stanley Kubrick
print(film.get_movies_by_director("Stanley Kubrick"))

# Ottenere i film di Christopher Nolan
film.get_movies_by_director("Christopher Nolan")
print()

# Ricerca di film per titolo
print(film.search_movies_by_title("Barry"))
print(film.search_movies_by_title("Cavaliere"))

