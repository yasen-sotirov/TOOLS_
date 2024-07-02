from app import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)


'''
    flask db init       - създаване на базата данни - веднъж за създаване
    flask db migrate    - мигриране на базата данни - при промяна на таблицата
    flask db upgrade    - &&

'''