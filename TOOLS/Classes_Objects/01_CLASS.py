

class Books:
    book_list = []    # клас атрибут, достъпва се от класа и от инстанцията
    number_books = 0
    def __init__(self, title: str, publisher: str, price: float):   # конструктор / инициализатор
        self.title = title
        self.publisher = publisher  # атрибути / пропъртита на инстанцията
        self.price = price
        Books.book_list.append(self.title)
        Books.number_books += 1      # брояч на създадените инстанции
        self.book_number = Books.number_books


    def change_price(self, new_price: float):      # метод na инстанцията
        """
        @param new_price: this new price will override old price
        """
        self.price = new_price


    @classmethod                # метод на класа
    def sort_book_list(cls):
        Books.book_list.sort()
        return "The books list was sorted alphabetically"



    @staticmethod           # обикновена функция вложена в класа по организационни причини
    def clean_dust():       # метод които не ползва достъп до класа или инстанциите му
        '''
        @clean_dust: This static method is in the Book class for organizational purposes
        @return: Conformational string
        '''
        return "The dust was cleaned"



    def __str__(self):                      # неформална презентация на обекта като str
        return (f'Title: {self.title} \n'
                f'author: {self.publisher} \n'
                f'price: {self.price} \n'
                f'book number: {self.book_number}')

    # def __repr__(self):     # връща техническа информация за обекта
    #     return repr()


"СЪЗДАВА ИНСТАНЦИЯ - НОВ ОБЕКТ"
book_1 = Books("Math", "Prosveta", 20.00)
book_2 = Books("Biology", "Anubis", 15.99)
book_3 = Books("Chemistry", "BAN", 12.80)


"РЕПРЕЗЕНТАЦИЯ НА ИНСТАНЦИЯТА"      # връща __str__ метода, ако има такъв, иначе <__main__.Books object at 0x0000025D92BFE210>
# print(book_2)


"ПОЛЗВАНЕ НА МЕТОДИТЕ НА КЛАСА"
# print(book_1.price)
# book_1.price = 30.00
# print(book_1.price)


"ДОСТЪПВАНЕ НА КЛАС АТРИБУТИ"
# print('number books', Books.number_books)       # достъпване през класа
# print('number books', book_1.number_books)      # достъпване през инстанцията


"ИЗВИКВАНЕ НА @CLASSMETHOD"
# print(Books.book_list)
# print(Books.sort_book_list())
# print(Books.book_list)


"ИЗВИКВАНЕ НА @STATICMETHOD"
# print(Books.clean_dust)
# print(book_3.sort_book_list())


"ИЗВИКВАНЕ НА ДОКУМЕНТАЦИЯ"     # ако има записана такава
print(Books.change_price.__doc__)
print(Books.clean_dust.__doc__)