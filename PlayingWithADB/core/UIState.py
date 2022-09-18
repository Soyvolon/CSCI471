from . import Book

class UIState(object):
    def __init__(self):
        self.state = 0
        self.output = []
        self.input = []
        self.__main_menu_index = [
            (1, "Add Book"),
            (2, "List Books"),
            (3, "Search Books"),
            (4, "Edit Book"),
            (5, "Delete Book"),
            (6, "Exit")
        ]
        self.__search_menu_index = [
            (1, "Search By Title"),
            (2, "Search By Author")
        ]
        self.__book_header = ["ID", "Title", "Author", "Price ($)"]

    def reset_state(self):
        self.state = 0
        self.output = []
        self.input = []

    def handle_state(self) -> str:
        if (self.state == 0):
            self.__main_menu()
        elif (self.state == 1):
            # add book
            return self.__add_book()
        elif (self.state == 2):
            # list books
            return "list"
        elif (self.state == 3):
            # search book
            return self.__search_books()
        elif (self.state == 4):
            # Edit book
            return self.__edit_book()
        elif (self.state == 5):
            # delete book
            return self.__delete_book()
        elif (self.state == 6):
            self.output = []
            self.state = -1
            return "exit"
        elif (self.state == 10):
            # waiting for book details
            return self.__finalize_edit()
        elif (self.state == 11):
            # waiting for book details
            return self.__finalize_delete()

        # if we hit here, there was no usable input to
        # tell the calling class about
        self.output = []
        return ""

    def __main_menu(self) -> None:
        print("Book Database")
        for index, name in self.__main_menu_index:
            print(f'{index:4} :: {name:15}')
        selRaw = input("Please select an option: ")
        try:
            self.state = int(selRaw)
        except:
            print("\nInvalid input. Please try again.\n")
            self.state = 0

    def __add_book(self) -> str:
        print("\n--- Add Book ---\n")
        try:
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            price = float(input("Enter Book Price: "))
        except:
            print("Invalid input. Make sure the price is a number.")
        
        self.output = [title, author, price]
        return "add"

    def __search_books(self) -> str:
        print("Search Options")
        for index, name in self.__search_menu_index:
            print(f'{index:4} :: {name:15}')
        selRaw = input("Please select an option: ")
        try:
            searchType = int(selRaw)
            if (searchType == 1):
                contents = input("Enter Search Query (Search By Title): ")
                self.output = [contents]
                return "search-title"
            elif (searchType == 2):
                contents = input("Enter Search Query (Search By Author): ")
                self.output = [contents]
                return "search-author"
            else:
                print("\nInvalid selection. Please select an option from the list below:")
        except:
            print("\nInvalid input. Please try again.\n")

    def __edit_book(self) -> str:
        print("Edit Book")
        selRaw = input("Please enter the ID of the book to edit: ")
        try:
            editId = int(selRaw)
            self.output = [editId]
            self.state = 10
            return "get-book"
        except:
            print("\nInvalid input. Please try again.\n")

    def __finalize_edit(self) -> str:
        self.display_book(self.input[0])

        print("\nLeave any of the following blank to skip")
        newTitle = input("Enter New Title: ")
        newAuthor = input("Enter New Author: ")
        newPrice = input("Enter New Price: ")
        try:
            if (newPrice != ""):
                newPrice = float(newPrice)
        except:
            print("Price must be a number.")
            self.reset_state()

        if (newTitle == ""):
            newTitle = self.input[0].title
        if (newAuthor == ""):
            newAuthor = self.input[0].author 
        if (newPrice == ""):
            newPrice = self.input[0].price

        self.output = [newTitle, newAuthor, newPrice, self.input[0].key]
        return "finalize-edit"

    def __delete_book(self) -> str:
        print("Delete Book")
        selRaw = input("Please enter the ID of the book to delete: ")
        try:
            editId = int(selRaw)
            self.output = [editId]
            self.state = 11
            return "get-book"
        except:
            print("\nInvalid input. Please try again.\n")

    def __finalize_delete(self) -> str:
        self.display_book(self.input[0])
        
        res = input("\nAre you sure you want to delete this book? [yes(y)/no(n)]: ").lower()
        if (res == "y" or res == "yes"):
            self.output = [self.input[0].key]
            return "del"
        else:
            print("Cancelling delete operation.")
            self.reset_state()

    def display_books(self, books):
        print('-'*40)
        print(f'{self.__book_header[0]:4} | {self.__book_header[1]:10} | {self.__book_header[2]:10} | {self.__book_header[3]}')
        for book in books:
            print(f'{book.key:4} | {book.title:10} | {book.author:10} | ${book.price:.2f}')
        print('-'*40)

    def display_book(self, book: Book.Book):
        print('-'*40)
        print(f'{self.__book_header[0]:10}: {book.key}')
        print(f'{self.__book_header[1]:10}: {book.title}')
        print(f'{self.__book_header[2]:10}: {book.author}')
        print(f'{self.__book_header[3]:10}: ${book.price:.2f}')
        print('-'*40)
