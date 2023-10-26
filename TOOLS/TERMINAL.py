"CONSOLE"  # конзолата в python
# https://www.jetbrains.com/help/pycharm/using-consoles.html#array


# Type commands and press Enter to execute them.
# Results are displayed in the same console.

vars()  # показва структурата (dictionary), която python си пази, кое къде се намира в паметта
        # показва нещата използвани във файла

# "x" in vars()


"""
pip freeze - pokazva koi библиотеки за инсталирани на това ниво

Виртуална среда - място в рама, където има отделна среда, където са инсталирани само
необходимите библиотеки на питон



ВИРТУАЛНА СРЕДА ПРЕЗ ТЕРМИНАЛА
    python3 -m venv FastEnv     - инсталиране
    .\env\Scripts\Activate.ps1  - активиране от Нора



СПИСЪК С ПАКЕТИ - Versioning
    pip install -r requirements     - създава файл с пакетите използвани в конкретния проект
    pip freeze > requirements.txt   - записва необходимите пакети за проекта

"""