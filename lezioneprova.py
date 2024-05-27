class Book:
    def __init__(self, book_id: str, title: str, author: str) ->None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def borrow(self) ->None:
        if self.is_borrowed == False:
            return "Libro preso in prestito"
        else:
            return "Libro già in prestito"
            
    
    def return_book(self) ->None:
        is_borrowed = False
    
class Member:
    def __init__(self, member_id: str, name: str) ->None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books =[]
    
    def borrow_book(self, book) ->None:
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.is_borrowed = True
        else:
            pass
    def return_book(self, book) ->None:
        if book.is_borrowed:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
         
    
class Library:
    def __init__(self) ->None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str) ->None:
        book = Book(book_id, title, author)
        if book_id not in self.books:
            self.books[book_id] = book
    
    def register_member(self,member_id:str, name: str) ->None:
        member = Member(member_id, name)
        if member_id not in self.members:
            self.members[member_id] = member
    
    def borrow_book(self, member_id: str, book_id: str) ->None:
       self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self, member_id: str, book_id: str) ->None:
        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id) ->list[Book]:
        if member_id in self.members:
            borrowed_books =  self.members[member_id].borrowed_books 
            book_list = []
            for book in borrowed_books:
                book_list.append(book.title)
            return book_list
    
    
    
    