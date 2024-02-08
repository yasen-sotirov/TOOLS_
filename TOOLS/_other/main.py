from book import Book
from order import OrderNewBook

container = OrderNewBook

book_1 = Book('book', 10.00, 'Title 1', container)

print('books in stock', book_1.in_stock)
book_1.order_book(10)

print('books in stock', book_1.in_stock)

print(book_1.sell_copies(2))
