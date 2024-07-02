"2. СЪЗДАВАНЕ НА БД"

import sqlite3        # вградена бд
import click
from flask import current_app, g

# https://flask.palletsprojects.com/en/3.0.x/tutorial/database/

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()




"3. СЪЗДАВАНЕ НА SQL ТАБЛИЦИТЕ  - flaskr/schema.sql"

"4. ИЗПЪЛНЯВАНЕ НА SQL СКРИПТА"
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')



"5. Register with the Application"
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

"6. __init__.py"