# Question:
# Create a Library class.
#
# Add books to the library.
# Display all books.
# Search for a book by name.
#
# Topic:
# Class, Object, List, Methods

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def search_book(self, book_name):

        if book_name in self.books:
            print(book_name, "is available")
        else:
            print(book_name, "is not available")

lib = Library()

lib.add_book("Python")
lib.add_book("Java")
lib.add_book("DBMS")

lib.display_books()

lib.search_book("Java")