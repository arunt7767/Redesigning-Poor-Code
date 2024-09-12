from storage import Storage
from datetime import datetime
from log_operations import log_operation

class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = Storage.load_data("checkouts.json")

    def checkout_book(self, user_id, isbn):
        user = self.user_manager.search_user(user_id=user_id)
        book = self.book_manager.search_books(isbn=isbn)

        if not user:
            print("User not found.")
            return
        if not book:
            print("Book not found.")
            return
        if not book.is_available:
            print(f"Book '{book.title}' is already checked out.")
            return

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.checkouts.append({
            "user_id": user_id,
            "isbn": isbn,
            "checkout_time": current_time,
            "return_time": None
        })
        self.book_manager.update_book_availability(isbn, False)
        Storage.save_data("checkouts.json", self.checkouts)
        log_operation(f"User with ID {user_id} checked out book with ISBN {isbn} at {current_time}.")
        print(f"Book '{book.title}' checked out by {user.name} at {current_time}")



    def return_book(self, user_id, isbn):
        # Find the checkout entry and update the return time
        for checkout in self.checkouts:
            if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                if checkout["return_time"] is not None:
                    print("Book has already been returned.")
                    return

                # Set the return time to the current time
                return_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                checkout["return_time"] = return_time
                self.book_manager.update_book_availability(isbn, True)
                Storage.save_data("checkouts.json", self.checkouts)
                user = self.user_manager.search_user(user_id)
                book = self.book_manager.search_books(isbn=isbn)
                log_operation(f"User with ID {user_id} returned book with ISBN {isbn} at {return_time}.")
                print(f"Book '{book.title}' returned by {user.name} at {return_time}")
                return
        print("No record of this book being checked out by the user.")
