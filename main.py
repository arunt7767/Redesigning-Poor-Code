from book import BookManager
from user import UserManager
from check import CheckoutManager
from log_operations import list_log_entries, log_operation
from models import Book

def main_menu():
    print("Choose an option ~")
    print("\t1. Manage Books")
    print("\t2. Manage Users")
    print("\t3. Check Out & In Books")
    print("\t4. Track Book Availability")
    print("\t5. Logging of Operations") 
    print("\t6. Exit")
    choice = input("\tEnter choice: ")
    return choice

def manage_books(book_manager):
    while True:
        print("\t\t1. Add Book")
        print("\t\t2. Update Book")
        print("\t\t3. Delete Book")
        print("\t\t4. List Books")
        print("\t\t5. Search Books")
        print("\t\t6. Back to Main Menu")
        choice = input("\t\tEnter choice: ")

        if choice == '1':
            isbn = input("\t\t\tEnter ISBN: ")
            title = input("\t\t\tEnter title: ")
            author = input("\t\t\tEnter author: ")
            try:
                book_manager.add_book(isbn, title, author)
                print("\t\t\tBook added.")
            except ValueError as e:
                print(f"\t\t\tError: {e}")
        elif choice == '2':
            isbn = input("\t\t\tEnter ISBN: ")
            title = input("\t\t\tEnter updated title (press Enter to skip): ")
            author = input("\t\t\tEnter updated author (press Enter to skip): ")
            book_manager.update_book(isbn, title, author)
        elif choice == '3':
            isbn = input("\t\t\tEnter ISBN: ")
            if book_manager.delete_book(isbn):
                print("\t\t\tBook deleted.")
            else:
                print("\t\t\tBook not found.")
        elif choice == '4':
            book_manager.list_books()
        elif choice == '5':
            isbn = input("\t\t\tEnter ISBN (press Enter to skip): ")
            title = input("\t\t\tEnter title (press Enter to skip): ")
            author = input("\t\t\tEnter author (press Enter to skip): ")

            results = book_manager.search_books(title=title, author=author, isbn=isbn)

            # If the search returns a list of books, iterate over it
            if isinstance(results, list):
                if results:
                    for book in results:
                        print(book)
                else:
                    print("\t\t\tNo books found.")
            # If the search returns a single book (searching by ISBN), print it directly
            elif isinstance(results, Book):
                print(results)
            else:
                print("\t\t\tBook not found.")
        elif choice == '6':
            break
        else:
            print("\t\tInvalid choice, please try again.")


def manage_users(user_manager):
    while True:
        print("\t\t1. Add User")
        print("\t\t2. Update User")
        print("\t\t3. Delete User")
        print("\t\t4. List Users")
        print("\t\t5. Search Users")
        print("\t\t6. Back to Main Menu")
        choice = input("\t\tEnter choice: ")

        if choice == '1':
            user_id = input("\t\t\tEnter user ID: ")
            name = input("\t\t\tEnter name: ")
            try:
                user_manager.add_user(name, user_id)
                print("\t\t\tUser added.")
            except ValueError as e:
                print(f"\t\t\tError: {e}")
        elif choice == '2':
            user_id = input("\t\t\tEnter user ID: ")
            name = input("\t\t\tEnter updated name: ")
            user_manager.update_user(user_id, name)
        elif choice == '3':
            user_id = input("\t\t\tEnter user ID: ")
            if user_manager.delete_user(user_id):
                log_operation(f"\t\t\tUser with ID {user_id} deleted.")
                print("\t\t\tUser deleted.")
            else:
                print("\t\t\tUser not found.")
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            user_id = input("\t\t\tEnter user ID (press Enter to skip): ")
            name = input("\t\t\tEnter name (press Enter to skip): ")
            user = user_manager.search_user(user_id=user_id, name=name)
            if user:
                print(user)
            else:
                print("\t\t\tUser not found.")
        elif choice == '6':
            break
        else:
            print("\t\tInvalid choice, please try again.")

def check_out_and_in_books(checkout_manager):
    while True:
        print("\t\t1. Check Out Book")
        print("\t\t2. Check In Book")
        print("\t\t3. Back to Main Menu")
        choice = input("\t\tEnter choice: ")

        if choice == '1':
            user_id = input("\t\t\tEnter user ID: ")
            isbn = input("\t\t\tEnter ISBN: ")
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '2':
            user_id = input("\t\t\tEnter user ID: ")
            isbn = input("\t\t\tEnter ISBN: ")
            checkout_manager.return_book(user_id, isbn)
        elif choice == '3':
            break
        else:
            print("\t\tInvalid choice, please try again.")

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager(book_manager, user_manager)

    print("Library Management System")
    while True:
        choice = main_menu()
        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            check_out_and_in_books(checkout_manager)
        elif choice == '4':
            isbn = input("\t\tEnter ISBN: ")
            book_manager.check_availability(isbn)
        elif choice == '5':
            print("\nLibrary Operation Logs:")
            list_log_entries()
        elif choice == '6':
            print("\tExiting system.")
            break
        else:
            print("\tInvalid choice, please try again.")

if __name__ == "__main__":
    main()
