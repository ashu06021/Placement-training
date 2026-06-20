# Question:
# Add books, issue books and return books.

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book):

        if book in self.books:
            self.books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")

    def return_book(self, book):
        self.books.append(book)

    def display(self):
        print("\nAvailable Books")

        for book in self.books:
            print(book)

lib = Library()

lib.add_book("Python")
lib.add_book("Java")
lib.add_book("DBMS")

lib.display()

lib.issue_book("Python")

lib.display()

lib.return_book("Python")

lib.display()