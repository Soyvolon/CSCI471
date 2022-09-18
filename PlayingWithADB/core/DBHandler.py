import sqlite3 as sql
import uuid
from . import Book

class DBHandler(object):
    def __init__(self, conString: str):
        self.con = sql.connect(conString)

    def initalize(self):
        self.con.execute("""
CREATE TABLE IF NOT EXISTS "Books"
(
    "Key" integer NOT NULL,
    "Title" character varying(256) NOT NULL,
    "Author" character varying(256) NOT NULL,
    "Price" double precision NOT NULL,
    PRIMARY KEY ("Key")
)""")

    def add_book(self, book: Book.Book) -> None:
        self.con.execute("""
INSERT INTO "Books"(
	"Title", "Author", "Price")
	VALUES ("{0}", "{1}", "{2}");
""".format(book.title, book.author, book.price))
        self.con.commit()

    def del_book(self, key: int) -> int:
        res = self.con.execute("""
DELETE FROM "Books" WHERE Key = "{0}";
""".format(key))
        self.con.commit()
        return res.fetchone()

    def edit_book(self, book: Book.Book) -> int:
        res = self.con.execute("""
UPDATE "Books" SET "Title" = "{0}", "Author" = "{1}", "Price" = "{2}" WHERE Key = "{3}";
""".format(book.title, book.author, book.price, book.key))
        self.con.commit()
        return res.fetchone()

    def get_books_by_author(self, author: str):
        res = self.con.execute("""
SELECT "Key", "Title", "Author", "Price" FROM "Books" WHERE "Author" = "{0}" ORDER BY "Key";
""".format(author))
        data = res.fetchall()
        return self.__parse_books(data)

    def get_books_by_name(self, title: str):
        res = self.con.execute("""
SELECT "Key", "Title", "Author", "Price" FROM "Books" WHERE "Title" = "{0}" ORDER BY "Key";
""".format(title))
        data = res.fetchall()
        return self.__parse_books(data)

    def get_all_books(self):
        res = self.con.execute("""
SELECT "Key", "Title", "Author", "Price" FROM "Books" ORDER BY "Key";
""")
        data = res.fetchall()
        return self.__parse_books(data)

    def get_book(self, id: int) -> Book.Book:
        res = self.con.execute("""
SELECT "Key", "Title", "Author", "Price" FROM "Books" WHERE "Key" = "{0}";
""".format(id))

        data = res.fetchall()
        books = self.__parse_books(data)
        if (len(books) > 0):
            return books[0]
        return None

    def __parse_books(self, data):
        books = []
        for key, title, author, price in data:
            book = Book.Book(title, author, price)
            book.key = key
            books.append(book)
        return books
