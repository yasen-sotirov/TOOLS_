"DEPENDENCY INJECTION"   # https://www.youtube.com/watch?v=bXujm9PqqIU&ab_channel=PythonforEveryone
# много добър пример!


from window import Window
from file_logic import FileLogic
from database import Database


# зареждаме новата логика в контейнера
# storage = FileLogic

# лесно подменяме начина на save - просто сменяме в контейнера,
# без да пипаме Window класа
storage = Database      # без скоби!


# създава инстанция
window = Window(storage)    # подаваме контейнера на window
# вписва текст в инстанцията
window.write_text("This is a test window. ")
# показва резултата
window.show_window()
# когато извикаме save_text, обектът window предава това извикване
# на контейнера, който предава на FileLogic
window.save_text()

"""Използвахме Dependency injection, за да разделим двете логики.
Storage обектът е инжектиран в window обекта. Двата обекта нямат 
знание един за друг. Единственото място, където има инфо за всичко е main.py
Сега ако решим да променим логиката и да запазим файла по друг начин,
може просто да напишем новия клас и да го подменим в контейнера в main.py

"""