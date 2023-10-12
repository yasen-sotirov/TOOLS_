from mariadb import connect
from mariadb.connections import Connection




"УСТАНОВЯВА ВРЪЗКАТА С БД"
def _get_connection() -> Connection:
    return connect(
        user='root',
        password='Tur6ia',
        host='localhost',
        port=3306,
        database='data_access_demo_db')  # името на схемата




"ЧЕТЕНЕ НА QUERY"
def read_query(sql: str, sql_params=()):
    with _get_connection() as conn:
        cursor_var = conn.cursor()
        cursor_var.execute(sql, sql_params)

        return list(cursor_var)


"СЪЗДАВА QUERY"
def insert_query(sql: str, sql_param=()) -> int:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_param)
        conn.commit()

        return cursor.lastrowid


























