from film import Film
class Noleggio:
    def __init__(self, film_list: list) -> None:
        self.rented_film: dict = {}
        self.film_list = film_list

    def isAvaible(self, film: Film) ->bool:
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle}!")
            return True
        else:
            print(f"Il film scelto è disponibile: {film.getTitle}!")
            return False
        
    def rentAMovie(self, film: Film, clientID: int) ->None:
        if film in self.film_list:
            self.film_list.remove(film)
            self.rented_film[clientID] = [film]
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle}!")
        else: 
            print(f"Non è possibile nolegiare il film {film.getTitle}!")