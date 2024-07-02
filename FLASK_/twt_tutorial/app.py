"FLASK  - Tech with Tim"
# vs code flask tut - https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask, redirect, url_for, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')



"ПАРАМЕТРИ"
@app.route('/params/<name>')
def params(name):
    lst_names = ['tim', 'john', 'az']
    return render_template('params.html', content=name, lst=lst_names)
    # http://127.0.0.1:5000/params/yass123



"ПРЕНАСОЧВАНЕ КЪМ ДРУГА СТРАНИЦА"
@app.route('/admin/<user>')
def admin(user):
    # подава на функция   def params   парам user
    return redirect(url_for('params', name=user))
    # http://127.0.0.1:5000/admin/yass


"BASE"
@app.route('/home')
def index():
    return render_template('base.html')
    # http://127.0.0.1:5000/home



if __name__ == "__main__":
    app.run(debug=True)
