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



  
"ОСНОВИ НА АПП"  '''

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return "<h1>Hello Flask!<h1/>"


    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)


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




"ФАЙЛ С ИЗПОЛЗВАНИТЕ ПАКЕТИ"
    # pip3 freeze > requirements.txt



"URL processor"     '''
    - подава променлива в адреса която да ползване в функцията
    <number1>       парсва към стринг
    <int:number1>   парсва към int

    @app.route('/greet/<number1>/<number2>')        парсва към стринг
    def greet(name):
        return f"<p>Hello {name}!<p/>"      '''




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




"CUSTOM RESPONSE"   '''
@app.route('/hello')
def hello():
    response = make_response("Hi you!")
    response.status_code = 123
    response.headers['content-type'] = '.............'
    return response
    # curl -I http://127.0.0.1:5000/hello       '''


