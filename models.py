class Book:
    def __init__(self, isbn, title, author, is_available=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"


class User:
    def __init__(self, name, user_id):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
