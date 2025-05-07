class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass
from custom_exceptions import BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not book:
            raise BookNotFoundException(f"'{book_title}' not found in the library.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book_title}' is already borrowed.")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{member_name} has already borrowed 3 books.")

        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if book:
            book.is_borrowed = False
            member.borrowed_books.remove(book)

# Testing 
lib = Library()

# Add
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Python Basics", "Jane Doe"))

# Add members
lib.add_member(Member("Alice"))

# Borrow and return books
try:
    lib.borrow_book("Alice", "1984")
    lib.borrow_book("Alice", "Python Basics")
    lib.return_book("Alice", "1984")
    lib.borrow_book("Alice", "1984")  # Reb
except Exception as e:
    print(e)
