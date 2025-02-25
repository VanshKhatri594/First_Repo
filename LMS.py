from datetime import datetime, timedelta


class LibraryInventory:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}  # {user_name: {book_title: (borrow_date, due_date)}}

    def add_book(self, title, author, quantity):
        if title in self.books:
            self.books[title]['quantity'] += quantity
        else:
            self.books[title] = {'author': author, 'quantity': quantity}

    def remove_book(self, title):
        try:
            if title in self.books:
                del self.books[title]
                print(f'Book "{title}" removed successfully.')
            else:
                raise KeyError(f'Book "{title}" not found in inventory.')
        except KeyError as e:
            print(e)

    def search_book(self, title):
        if title in self.books:
            print(f'Book "{title}" is available.')
        else:
            print(f'Book "{title}" is not available.')

    def update_book(self, title, new_author=None, new_quantity=None):
        try:
            if title in self.books:
                if new_author:
                    self.books[title]['author'] = new_author
                if new_quantity is not None:
                    self.books[title]['quantity'] = new_quantity
                print(f'Book "{title}" updated successfully.')
            else:
                raise KeyError(f'Book "{title}" not found in inventory.')
        except KeyError as e:
            print(e)

    def display_books(self):
        if self.books:
            print("Available books:")
            for title, details in self.books.items():
                print(f'Title: {title}, Author: {details["author"]}, Quantity: {details["quantity"]}')
        else:
            print("No books available in the inventory.")

    def borrow_book(self, user_name, title):
        try:
            if user_name not in self.borrowed_books:
                self.borrowed_books[user_name] = {}

            if len(self.borrowed_books[user_name]) >= 2:
                raise ValueError("You can only borrow a maximum of 2 books at a time.")

            if title in self.books and self.books[title]['quantity'] > 0:
                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=14)  # 2 weeks due date
                self.borrowed_books[user_name][title] = (borrow_date, due_date)
                self.books[title]['quantity'] -= 1
                print(f'Book "{title}" borrowed successfully. Due date: {due_date.date()}')
            else:
                raise ValueError(f'Book "{title}" is not available for borrowing.')
        except ValueError as e:
            print(e)

    def return_book(self, user_name, title):
        try:
            if user_name in self.borrowed_books and title in self.borrowed_books[user_name]:
                del self.borrowed_books[user_name][title]
                self.books[title]['quantity'] += 1
                print(f'Book "{title}" returned successfully.')
            else:
                raise KeyError(f'Book "{title}" was not borrowed by {user_name}.')
        except KeyError as e:
            print(e)

    def view_borrowed_books(self, user_name):
        if user_name in self.borrowed_books and self.borrowed_books[user_name]:
            print(f'{user_name} has borrowed the following books:')
            for title, (borrow_date, due_date) in self.borrowed_books[user_name].items():
                print(f'Title: {title}, Borrowed on: {borrow_date.date()}, Due on: {due_date.date()}')
        else:
            print(f'{user_name} has not borrowed any books.')

library = LibraryInventory()
library.add_book("Marvel", "Vansh", 3)
library.add_book("Python Basics", "Khatri", 5)
library.display_books()
library.borrow_book("Alice", "Marvel")
library.view_borrowed_books("Alice")
library.return_book("Alice", "Marvel")
library.display_books()
