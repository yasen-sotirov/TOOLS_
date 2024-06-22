from flask import Flask, request, jsonify, session, make_response, render_template
from static import info

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')



@app.route('/')
def home():
    return render_template('home.html', technologies=info.technologies)


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=info.projects)







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


# pip3 freeze > requirements.txt
# debug=False след деплоиване