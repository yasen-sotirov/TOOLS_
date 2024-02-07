class Window:
    def __init__(self, storage):
        self.text = ""
        self.storage = storage
        # инжектиране на save^

    def write_text(self, add_text):
        self.text += add_text

    def show_window(self):
        print('-= Text Window =-')
        print(self.text)


    "SAVE TEXT"
    def save_text(self):
    # print('The text is saved')
    # ^ може да включим този метод тук, но ще внесе нова, допълнителна логика,
    # което обърква нещата. Нарушава принципа за единична отговорност на класа
    # Решаваме това с разделяне. Изплзваме Dependency Injection.
    # Преместваме save логиката в собствен клас file_logic
    # и от там докарване нужната ни логика.
        self.storage.save(self.text)
    # от контейнера^  ^ включваме новата логика, върху инстанцията
    # сега класа не знае логиката на save, знае само,
    # че контейнера съдържа обект, който може да прави това