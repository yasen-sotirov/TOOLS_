from items import Items

class Book(Items):

    def __init__(self, item, price, title: str, container):
        super().__init__(item, price)
        self.item = 'Book'
        self.price = price
        self.title = title
        self.in_stock: int = 0
        self.container = container


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value > 0:
            self._price = value
        else:
            raise ValueError('The price must be positive number')


    def order_book(self, number):
        new_books = self.container.order_book(self, number)
        self.in_stock = new_books

    def sell_copies(self, num_copies):
        self.in_stock -= num_copies
        return f'Copies left {self.in_stock}'