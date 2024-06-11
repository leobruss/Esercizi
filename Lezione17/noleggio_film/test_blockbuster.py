# test_blockbuster.py
import unittest
from film import Film
from movie_genre import Azione, Commedia, Dramma
from noleggio import Noleggio

class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film_azione1 = Azione(1, "Azione1")
        self.film_azione2 = Azione(2, "Azione2")
        self.film_azione3 = Azione(3, "Azione3")
        self.film_azione4 = Azione(4, "Azione4")
        self.film_azione5 = Azione(5, "Azione5")
        self.film_commedia1 = Commedia(6, "Commedia1")
        self.film_commedia2 = Commedia(7, "Commedia2")
        self.film_commedia3 = Commedia(8, "Commedia3")
        self.film_commedia4 = Commedia(9, "Commedia4")
        self.film_dramma = Dramma(10, "Dramma1")

        self.film_list = [
            self.film_azione1, self.film_azione2, self.film_azione3,
            self.film_azione4, self.film_azione5, self.film_commedia1,
            self.film_commedia2, self.film_commedia3, self.film_commedia4,
            self.film_dramma
        ]

        self.noleggio = Noleggio(self.film_list)

    def test_isAvaible(self):
        self.assertTrue(self.noleggio.isAvaible(self.film_azione1))
        self.noleggio.rentAMovie(self.film_azione1, 1)
        self.assertFalse(self.noleggio.isAvaible(self.film_azione1))

    def test_rentAMovie(self):
        self.noleggio.rentAMovie(self.film_azione1, 1)
        self.assertFalse(self.noleggio.isAvaible(self.film_azione1))
        self.assertIn(self.film_azione1, self.noleggio.rented_film[1])

    def test_rentUnavailableMovie(self):
        self.noleggio.rentAMovie(self.film_azione1, 1)
        self.noleggio.rentAMovie(self.film_azione1, 2)
        self.assertNotIn(self.film_azione1, self.noleggio.rented_film.get(2, []))

    def test_giveBack(self):
        self.noleggio.rentAMovie(self.film_azione1, 1)
        self.noleggio.giveBack(self.film_azione1, 1, 5)
        self.assertTrue(self.noleggio.isAvaible(self.film_azione1))
        self.assertNotIn(self.film_azione1, self.noleggio.rented_film[1])

    def test_calcolaPenaleRitardo(self):
        self.assertEqual(self.film_azione1.calcolaPenaleRitardo(3), 9.0)
        self.assertEqual(self.film_commedia1.calcolaPenaleRitardo(3), 7.5)
        self.assertEqual(self.film_dramma.calcolaPenaleRitardo(3), 6.0)

    def test_printMovies(self):
        self.noleggio.printMovies()

    def test_printRentMovies(self):
        self.noleggio.rentAMovie(self.film_azione1, 1)
        self.noleggio.rentAMovie(self.film_commedia1, 1)
        self.noleggio.printRentMovies(1)

if __name__ == '__main__':
    unittest.main()
