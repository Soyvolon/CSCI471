class Book(object):
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
        self.key = None

    def __str__(self):
        return "[{0}, {1}, {2}, {3}]".format(self.title, self.author, self.price, self.key)



