class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title} Author: {self.author} Isbn: {self.isbn}"

    @classmethod
    def from_string( cls, book_str) ->None:
        title, author, isbn = book_str.split(', ')
        return cls(title, author, int(isbn))
    

class Member:
    def __init__(self, name: str, member_id: int) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book: str) ->None:
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            print("Book is alredy in the list")

    def return_book(self, book: str) ->None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("Book is not in the list")
        
    def __str__(self) -> str:
        return f"Name: {self.name} Member id: {self.member_id}"
    
    @classmethod
    def from_string(cls, member_str) ->None:
        name, member_id = member_str.split(', ')
        return cls(name, int(member_id))
    
class Library:
    total_books = 0
    def __init__(self) -> None:
        self.books = []
        self.members = []
    
    def add_book(self, book) -> None:
        if book not in self.books:
            self.books.append(str(book))
            Library.total_books += 1
        else: 
            print("Book is alredy in the list")

    def remove_book(self, book) ->None:
        if book in self.books:
            self.books.remove(str(book))
            Library.total_books -= 1
        else: 
            print("Book is not   in the list")

    def register_member(self, member) ->None:
        if member not in self.members:
            self.members.append(str(member))
        else:
            print("Member is alredy in the list")
        
    def lend_book(self, book, member) ->None:
        if book in self.books and member in self.members:
            self.books.remove(book)
        else:
            print("Impossible to lend the book")
    def __str__(self) -> str:
        return f"In this library we have there books\n\t{self.books}\nAnd our members are \n\t{self.members}"
    
    @classmethod
    def library_statistics(cls):
        return cls.total_books


if __name__ == '__main__':
    library1 = Library()
    book1_info = "The Great Gatsby, F. Scott Fitzgerald, 9780743273565"
    book2_info = "La Divina Commedia, D. Alighieri, 999000666"

    book1 = Book.from_string(book1_info)
    book2 = Book.from_string(book2_info)

    library1.add_book(book1)
    library1.add_book(book2)


    member1_info = ("Leonardo, 240704")
    member2_info = ("Matteo, 241629")

    member1 = Member.from_string(member1_info)
    member2 = Member.from_string(member2_info)

    library1.register_member(member1)
    library1.register_member(member2)

    tot_books = Library.library_statistics()

    print()
    print(book1)
    print()
    print(book2)
    print("\n")
    print(member1)
    print()
    print(member2)
    print()
    print(library1)
    print()
    print(tot_books)

