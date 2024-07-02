"FLASK"   
# official tutorials
# micro, simple, minimalistic framework, няма много неща - инсталират допълнително 


"1. "
"В ТЕРМИНАЛА"   '''
    - mkdir app_name
    - python3 -m venv .venv
        - python3   командата за стартиране на Python3.x. интерпретатора, версия 3.x. 
        - m         флаг указващ на интерпретатора да изпълни посочения модул като скрипт
        - venv      модул в библиотеката на Python за създаване на виртуални среди.
        - .venv     името на директорията  . за да е скрита   

    защо venv:
        - съдържа библиотеките необходими за този конкретен проект
        - позволява да се направи requirement.txt
        - и още много други важни, но неизвестни за мен неща!

    - source .venv/bin/activate    - активира виртуалната среда
        - source                   - изпълнява даден скрипт в текущата сесия на терминала

    - pip3 install flask           
    - pip3 freeze                  - показва какви пакети са инсталирани      '''



"СЪЗДАВАНЕ НА FACTORY - flaskr/__init__.py"
import os
from flask import Flask
from . import db
from . import auth


# https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

# "6."
    db.init_app(app)
# 8 auth
    app.register_blueprint(auth.bp)
    return app




"СТАРТИРАНЕ НА FLASK"
'flask --app flaskr run --debug'



"2. СЪЗДАВАНЕ НА ВРЪЗКА С БАЗА ДАННИ - flaskr/db.py"


"7. Initialize the Database File"
# flask --app flaskr init-db    flaskr/auth

"8. authentication  flaskr/auth"

    
