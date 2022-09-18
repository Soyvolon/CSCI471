from . import DBHandler
from . import UIState
from . import Book
import sys

class Program(object):
    def __init__(self):
        self.db = DBHandler.DBHandler("books.db")
        self.ui = UIState.UIState()
        self.books = []

    def start(self):
        print("....initalzing")
        self.db.initalize()
        print("initalized....")
        self.__main_loop()

    def __main_loop(self):
        while self.ui.state != -1:
            res = self.ui.handle_state()
            
            if res == "add":
                self.__add_book()
                self.ui.reset_state()
            elif res == "del":
                self.__del_book()
                self.ui.reset_state()
            elif res == "list":
                self.__list_books()
                self.ui.reset_state()
            elif res == "search-author":
                self.__search_by_author()
                self.ui.reset_state()
            elif res == "search-title":
                self.__search_by_title()
                self.ui.reset_state()
            elif res == "get-book":
                self.__get_book()
            elif res == "finalize-edit":
                self.__edit_book()
                self.ui.reset_state()

        print("Exiting....")

    def __add_book(self):
        try:
            book = Book.Book(self.ui.output[0], self.ui.output[1], self.ui.output[2])
            self.db.add_book(book)
            print("Added book!\n")
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to add book: {0}".format(the_value))

    def __del_book(self):
        try:
            self.db.del_book(self.ui.output[0])
            print("Deleted book!\n")
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to delete book: {0}".format(the_value))

    def __search_by_title(self):
        try:
            books = self.db.get_books_by_name(self.ui.output[0])
            self.ui.display_books(books)
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to find books by title: {0}".format(the_value))

    def __search_by_author(self):
        try:
            books = self.db.get_books_by_author(self.ui.output[0])
            self.ui.display_books(books)
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to find books by author: {0}".format(the_value))

    def __list_books(self):
        try:
            books = self.db.get_all_books()
            self.ui.display_books(books)
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to get a list of books: {0}".format(the_value))

    def __get_book(self):
        try:
            book = self.db.get_book(self.ui.output[0])
            if (book == None):
                print("No book found by the provided ID")
                self.ui.reset_state()
            else:
                self.ui.input = [book]
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to get a list of books: {0}".format(the_value))

    def __edit_book(self):
        try:
            book = Book.Book(self.ui.output[0], self.ui.output[1], self.ui.output[2])
            book.key = self.ui.output[3]
            self.db.edit_book(book)
            print("Edited book!\n")
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            print("Failed to edit book: {0}".format(the_value))




