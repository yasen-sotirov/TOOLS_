"С __init__ папката става package"
# от тук ще се импортва

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    # всеки шаблон ползва свой си template folders
    app = Flask(__name__, template_folder='templates')
    # конфигуриране на база данни
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprint_db.db'

    db.init_app(app)


    "import and register all blueprint"
    from blueprint_app.blueprints.core.routes import core
    from blueprint_app.blueprints.peoples.routes import people 
    from blueprint_app.blueprints.todos.routes import todos
   
    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(people, url_prefix='/people')
    # flask db init
    # flask db upgrade
    # flask db migrate


    migrate = Migrate(app, db)

    return app 