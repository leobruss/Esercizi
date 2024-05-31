class MovieCatalog(): 
    def __init__(self) -> None:
        self.movies: dict = {}
        
        
    def add_movie(self, director_name: str, movies: list) ->None:
        if director_name not in self.movies:
            self.movies[director_name] = movies
        else:
            self.movies[director_name].append(movies.movie_name)
        for chiave, valore in self.movies.items():
            if isinstance(valore, list):
                print(chiave + ":")
                for elemento in valore:
                    print("- " + str(elemento))
        

    def  remove_movie(self, director_name: str, movie_name: str) ->None:
        if director_name in self.movies: 
            if movie_name in self.movies[director_name]:
                self.movies[director_name].remove(movie_name)
                if not self.movies[director_name]:
                    del self.movies[director_name]

        for chiave, valore in self.movies.items():
            if isinstance(valore, list):
                print(chiave + ":")
                for elemento in valore:
                    print("- " + str(elemento)).


    def list_directors(self) ->None:
        print(self.movies.keys())


    def get_movies_by_director(self, director_name: str) ->list:
        print(self.movies[director_name])


    def search_movies_by_title(self, title: str) ->None:
        key_word = title.lower() 
        film_list = []

        for director, movies in self.movies.items():
            for movie in movies:
                if key_word in movie.lower():
                    film_list.append((director, movie))
        if film_list:
            return film_list
        else:
            raise RuntimeError("Film non trovato")


film: MovieCatalog = MovieCatalog()

film.add_movie("Stanley Kubrick", ["Shining", "Paura e desiderio", "Barry Lyndon"])
print()
film.add_movie("Christopher Nolan", ["Oppenheimer ", "Inception", "Il cavaliere oscuro", "Interstellar"])
print()
film.remove_movie("Stanley Kubrick", "Paura e desiderio")
print()
film.list_directors()
print()
film.get_movies_by_director("Stanley Kubrick")
film.get_movies_by_director("Christopher Nolan")
print()
print(film.search_movies_by_title("Barry"))
print(film.search_movies_by_title("Cavaliere"))

