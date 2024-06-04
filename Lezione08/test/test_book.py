import unittest
from Esercizi.Lezione08.esercizi.library_managment_system import Library, Book


class TestBook(unittest.TestCase):
    def test_book(self):
        books = Library()
        book1_info = "The Great Gatsby, F. Scott Fitzgerald, 9780743273565"
        book2_info = "La Divina Commedia, D. Alighieri, 99900066"

        book1 = Book.from_string(book1_info)
        book2 = Book.from_string(book2_info)
        
        books.add_book(book1)
        books.add_book(book2)

        self.assertEqual(books.library_statistics(), 2, "Numero di libri errato")

if __name__ == '__main__':
    unittest.main()