class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return '{self.title}'.format(self=self)

    def __repr__(self):
        return '{self.title}'.format(self=self)


class Library:
    def __init__(self):
        self.list_of_books = []

    def add_book(self, title):
        self.list_of_books.append(Book(title))

    def borrow(self, book, customer):
        for i in self.list_of_books:
            if i.title == book:
                self.list_of_books.remove(i)
                customer.list_of_customer_books.append(i)
                return True

    def give_back(self, book, customer):
        for i in customer.list_of_customer_books:
            if i.title == book:
                self.list_of_books.append(i)
                customer.list_of_customer_books.remove(i)
                return True


class Customer:
    def __init__(self, customer):
        self.customer = customer
        self.list_of_customer_books = []
