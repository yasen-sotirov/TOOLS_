"FLASK DATABASE"

'''
ИНСТАЛИРАНЕ НА НЕОБХОДИМИТЕ ПАКЕТИ ВЪВ VENV
    pip3 install flask-sqlalchemy flask-migrate
        - flask-sqlalchemy  - ORM 
        - flask-migrate


models.py   - тук е ORM-а, който връзва с базата данни
app.py      - тук е питонската логика
run.py      - стартира приложението. За да се избегне цикличния импорт, 
              правя отделен файл, създавам функция, която създава обект, 
              който да не се изпълнява постоянно
            

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



"СЪЗДАВА БАЗА ДАННИ"
db = SQLAlchemy()



"СЪЗДАВА ПРИЛОЖЕНИЕ И ГО ВРЪЩА КАТО ОБЕКТ, ЗА ДА НЕ СЕ ИЗПЪЛНЯВА КОДА ПРИ ИМПОРТ НА ТЕКУЩИЯ МОДУЛ"
# когато се импортира модул се изпълнява целият му код. ако е функция - не.
def create_app():
    app = Flask(__name__, template_folder='template')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test_db.db'
    # за PostgreSQL
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/test_db.db'

    # свързване с базата данни
    db.init_app(app)
    
    # правя импортите във функцията, за да се избегне цикъл
    from routes import register_routes
    register_routes(app, db)


    migrate = Migrate(app, db)

    return app

