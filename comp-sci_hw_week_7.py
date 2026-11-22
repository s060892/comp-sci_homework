class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")

        print("-------------------")


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")

        book = Book(title, author)
        self.books.append(book)

        print("Book added successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")

        else:
            for book in self.books:
                book.display_info()

    def borrow_book(self):
        title = input("Enter the book title: ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    print("You have borrowed the book!")
                else:
                    print("This book is already borrowed.")

                return

        print("Book not found.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return

        print("Book not found.")

library = Library()

library.books.append(Book("Harry Potter", "J.K. Rowling"))
library.books.append(Book("The Hunger Games", "Suzanne Collins"))
library.books.append(Book("Shatter Me", "Tahereh Mafi"))


while True:

    print("===== LIBRARY =====")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Borrow a book")
    print("4. Remove a book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.remove_book()

    elif choice == "5":
        print("Thank you for using our library!")
        break

    else:
        print("Invalid option.")
