"FLASK"   # micro, simple, minimalistic framework, няма много неща - инсталират допълнително 

"В ТЕРМИНАЛА"   '''
    - mkdir app_name
    - python3 -m venv venv
        - python3   командата за стартиране на Python3.x. интерпретатора, версия 3.x. 
        - m         флаг указващ на интерпретатора да изпълни посочения модул като скрипт
        - venv      модул в библиотеката на Python за създаване на виртуални среди.
        - venv      името на директорията  . за да е скрита   

    създаване на venv:
        - съдържа библиотеките необходими за този конкретен проект
        - позволява да се направи requirement.txt
        - и още много други важни, но неизвестни за мен неща!

    - source venv/bin/activate    - активира виртуалната среда
        - source                    - изпълнява даден скрипт в текущата сесия на терминала

    - pip3 install flask           - става и с pip3
    - pip3 freeze                  - показва какви пакети са инсталирани

    - избиране на интерпретатора във venv   - долен десен ъгъл на vscode    '''



"CURL"  '''
инструмент за трансфер на данни с URL синтаксис през терминала. 
    - GET
        curl http://127.0.0.1:5000/sum/1/2

    - RESPONSE HEADER - връща хедъра, където е и статус кода
        curl -I http://127.0.0.1:5000

    - POST
        curl -X POST  http://127.0.0.1:5000/Maniana

    - изпращане на JSON данни с POST заявка:
        curl -X POST -H "Content-Type: application/json" -d '{"key1":"value1","key2":"value2"}' http://example.com/resource


    - Изтегляне на HTML съдържанието на уеб страница:
        curl http://example.com     '''



"IMPORTS"
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template


app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():
    return "<h1 style='text-align:center; font-family:Sans-serif'>Hello Flask!<h1/>", 201
    # http://127.0.0.1:5000/




"URL PROCESSORS"     '''
    - подава променлива в адреса която да ползване в функцията
    <number1>       парсва към стринг
    <int:number1>   парсва към int   '''

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    return f"<h3 style='text-align:center; font-family:Sans-serif'> {num1} + {num2} = {num1 + num2} </h3>"
    # http://127.0.0.1:5000/sum/1/2







"URL PARAMETERS  "      # import request

@app.route('/handle_params')
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args['name']
        return f"{greeting}, {name}!"
        # http://127.0.0.1:5000/handle_params?greeting=Helloooo&name=Yasen

    else:
        return 'Some parameters are missing'
        # http://127.0.0.1:5000/handle_params?greeting=Helloooo




"CUSTOM RESPONSE"

@app.route('/hello')
def hello():
    response = make_response("Hi you!")
    response.status_code = 123
    response.headers['content-type'] = '.............'
    return response
    # curl -I http://127.0.0.1:5000/hello




"TEMPLATE"     '''
    - import render_template        
    - jinja2    - template language for Flask               '''

@app.route('/template')
def template():
    res = [10, 20, 30, 40, 50]
    text = "Lorem ipsum"
    return render_template('index.html', nums = res, paragraph = text)
    # http://127.0.0.1:5000/template




"FILTERS"
@app.route('/filters')
def filters():
    text = "Hello world! This is filters in jinja"
    return render_template('filters.html', text = text)
    # http://127.0.0.1:5000/filters



"CUSTOM FILTER"
@app.template_filter('custom_filter')
def custom_filter(string):
    return string[::-1]

@app.template_filter('repeat_filter')
def repeat_filter(string, times=2):
    return string * times



"DYNAMIC URL"   
@app.route('/-------')
def dynamic_url():
    return render_template('filters.html')
    # http://127.0.0.1:5000/template





"СТАРТИРАНЕ НА АПП"  '''
    host='0.0.0.0'
        - стартира на локалния хост по подразбиране == http://127.0.0.1:5000
        - стартира на private local ip address      == http://192.168.0.35:5000/

    debug=True    
        - по време на разработка само
        - позволява дебъг без рестарт 
        - ъпдейтва автоматично
        - позволява връщане на грешки
        
    debug=False
        - след деплоиване   '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



"ФАЙЛ С ИЗПОЛЗВАНИТЕ ПАКЕТИ"
    # pip3 freeze > requirements.txt