from flask import render_template, request
from models import Person


"ЗА ДА ИЗБЕГНЕМ ЦИКЛИЧЕН ИМПОРТ ГО ПОДАВАМЕ ПРЕЗ ФУНКЦИЯ"
def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people=people)
        
        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            # за да покаже отново данните:
            people = Person.query.all()
            return render_template('index.html', people=people)
        

    @app.route('/delete/<id_person>', methods=['DELETE'])
    def delete(id_person):
        Person.query.filter(Person.id_person == id_person).delete()

        db.session.commit()
        
        people = Person.query.all()
        return render_template('index.html', people=people)


    