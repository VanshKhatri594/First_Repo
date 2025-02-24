class LibraryInventory:
    def __init__(self):
        self.books = {}

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


# Example usage
library = LibraryInventory()
library.add_book("Marvel", "Vansh", 3)
library.add_book("Python Basics", "Khatri", 5)
library.display_books()
library.update_book("Marvel", new_author="Jayesh", new_quantity=1)
library.search_book("Marvel")
library.remove_book("Python Basics")
library.display_books()
