from log_operations import log_operation
from models import Book
from storage import Storage

class BookManager:
    def __init__(self):
        book_data = Storage.load_data("books.json")
        self.books = [Book(**data) for data in book_data]

    def add_book(self, isbn, title, author):
        book = Book(isbn, title, author)
        self.books.append(book)
        Storage.save_data("books.json", self.books)
        log_operation(f"Added book: {title} by {author} (ISBN: {isbn})")
        
    def delete_book(self, isbn):
        book = self.search_books(isbn=isbn)
        if book:
            self.books.remove(book)
            Storage.save_data("books.json", self.books)
            log_operation(f"Deleted book: {book.title} by {book.author} (ISBN: {book.isbn})")
            return True
        else:
            return False
    
    def update_book(self, isbn, title, author):
        book = self.search_books(isbn=isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            Storage.save_data("books.json", self.books)
            print("\t\t\tBook updated.")
        else:
            print("\t\t\tBook not found.")


    def list_books(self):
        for book in self.books:
            print(book)

    def search_books(self, title=None, author=None, isbn=None):
        if isbn:
            for book in self.books:
                if book.isbn == isbn:
                    return book  
            return None
        else:
            searched = []
            for book in self.books:
                if (title and book.title == title) or (author and book.author == author):
                    searched.append(book)
            return searched if searched else None



    def update_book_availability(self, isbn, is_available):
        book = self.search_books(isbn=isbn)
        if book:
            book.is_available = is_available
            Storage.save_data("books.json", self.books)
        else:
            print("Book not found.")

    def check_availability(self, isbn):
        book = self.search_books(isbn=isbn)
        if book:
            if book.is_available:
                print(f"Book '{book.title}' (ISBN: {book.isbn}) is available.")
            else:
                print(f"Book '{book.title}' (ISBN: {book.isbn}) is currently checked out.")
        else:
            print(f"Book with ISBN {isbn} not found.")