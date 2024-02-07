import requests
from twilio.rest import Client
import time
# twilio_code = "Q1QSR3GM478N6AXZ1V3APR9K"

# Вашите Twilio акаунт SID, токен и телефонен номер
account_sid = 'AC646f618713e9c842dcc901202329b0c8'
auth_token = 'd7fc281d1bfb1d7d488847f572abac9a'
twilio_phone_number = '+14794484407'
recipient_phone_number = '+359886921385'

# Уебсайт, който ще следим
url = 'https://www.clubr.bg/event_view.php?id=1316'

# Последно видяна версия на уебсайта
last_seen_html = ''


# Функция за изпращане на SMS чрез Twilio
def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"SMS изпратено успешно. SID: {message.sid}")


# Основна логика
while True:
    # Извличане на HTML кода от уебсайта
    response = requests.get(url)
    current_html = response.text

    # Сравнение с последната видяна версия на уебсайта
    if current_html != last_seen_html:
        print("Има нов запис в ClubR")

        # Изпращане на SMS съобщение
        send_sms("Има нов запис в ClubR")

        # Актуализация на последната видяна версия на уебсайта
        last_seen_html = current_html

    # Проверка на интервали, например всеки час
    time.sleep(1800)
