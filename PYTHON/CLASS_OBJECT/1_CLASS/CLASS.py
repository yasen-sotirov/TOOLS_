"CLASS AND OBJECTS"  #

class Books:            # именуване в CamelCase
    '''This is book class in a library'''
    BOOK_LIST = []      # клас атрибут, достъпва се от класа и от инстанцията
    NUMBER_BOOKS = 0

    # state - състоянието на обект. Описваме го чрез атрибутите.
    def __init__(self, title: str, publisher: str, price: float, barcode: int = None, **kwargs):   # конструктор / инициализатор
                        # параметри ↑
        self.title = title
        self.publisher = publisher              # атрибути / пропъртита на инстанцията
        self.price = price
        self.barcode = barcode                  # атрибут по желание
        self.other = kwargs                     # позволява подаването на произволен брой ключови аргументи
        self.is_available: bool = True

        Books.BOOK_LIST.append(self.title)      # пълни листа на класа
        Books.NUMBER_BOOKS += 1                 # брояч на създадените инстанции
        self.book_number = Books.NUMBER_BOOKS   # запазва поредния си номер



    # процедури - описват се чрез методи и с тях може да манипулираме стейта на обекта
    def change_price(self, new_price: float):      # метод na инстанцията
        '''
        @param new_price:
        @return: change the old price with the new price
        '''
        self.price = new_price



    def __str__(self):                      # неформална презентация на обекта като str
        return (f'Title: {self.title} \n'
                f'author: {self.publisher} \n'
                f'price: {self.price} \n'
                f'book number: {self.book_number}')

    # def __repr__(self):     # връща техническа информация за обекта
    #     return repr()


"СЪЗДАВА ИНСТАНЦИЯ - НОВ ОБЕКТ"
book_1 = Books("Math", "Prosveta", 20.00)
book_2 = Books("Biology", "Anubis", 15.99, 12345)
book_3 = Books("Chemistry", "BAN", 12.80, 12345, author = "G. Dimitrov", year = 2015)
            # аргументи ^


"РЕПРЕЗЕНТАЦИЯ НА ИНСТАНЦИЯТА"      # връща __str__ метода, ако има такъв, иначе <__main__.Books object at 0x0000025D92BFE210>
# print(Books.__doc__)
# print(book_2)
# print(book_2.__dict__)
# print(Books.change_price.__doc__)


"ПОЛЗВАНЕ НА МЕТОДИТЕ НА КЛАСА"
# print(book_1.price)
# book_1.price = 30.00
# print(book_1.price)


"ДОСТЪПВАНЕ НА КЛАС АТРИБУТИ"
# print('number books', Books.number_books)       # достъпване през класа
# print('number books', book_1.number_books)      # достъпване през инстанцията


"ИЗВИКВАНЕ НА KWARGS"
# print(book_3.other)


"ПРИНТИРАНЕ СПИСЪК С ОБЕКТИ"
# lst = [
#     Books("История", "Анубис", 20),
#     Books("География", "Анубис", 20),
#     Books("Биология", "Анубис", 20)]

# print(lst)
# print(*lst, sep='\n')


"СОРТИРАНЕ НА ОБЕКТИ С ЛАМБДА"
# books_list = [book_1, book_2, book_3]
# for book in sorted(books_list, key=lambda x: (x.title, -x.price)):
# # ще сортира по име. Ако имената съвпадат, ще сортира по цена низходящо
#     print(book)