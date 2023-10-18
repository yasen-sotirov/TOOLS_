"Authentication & Authorization"   # записки с Нора



'''
AUTHENTICATION - удостоверяване, процес на потвърждаване идентичността на потребителя
- Authentication включва идентификация, но също така включва и проверка на идентичността,
- Identification се отнася само до идентификацията на субектите, без проверка на тяхната идентичност.

Бисквитки
    Сървърът генерира защитена бисквитка.
    Сървърът запазва бисквитка за всеки клиент
    Бисквитката се изпраща обратно с всяка заявка и сървърът я проверява.

Токен
    Сървърът създава подписан токен
    Клиентите искат токен
    Клиентите изпращат токена с всяка заявка
    
OpenId протокол
    Удостоверяване от външен доставчик (google, facebook)



AUTHORIZATION - Упълномощаване


JSON WEB TOKEN (JWT) 
    https://pyjwt.readthedocs.io/en/stable/usage.html#encoding-decoding-tokens-with-hs256
    отворен стандарт, който дефинира компактен и самостоятелен начин за 
    предаване на информация като JSON

    HEADER - дава метаинформация за токена
        {"alg" : "HS256",
          "typ" : "JWT"}
          
    PAYLOAD - дава инфо за юзера
        {"sub":1,               subject – уникален id за обекта
        "username": "John",
        "role": "User",
        "iat": 1601470897,      issued at – време на създаване
        "exp": 1601474497}      expiration – срок на годност

    SIGNATURE - хеширан сбор от header, payload и secret key (подаван от сървъра)
    

Payload
Signature




HTTP AUTHENTICATION
    https://blog.risingstack.com/web-authentication-methods-explained/
    най-простият начин за контрол на достъпа, 
    не изисква бисквитки, сесии или друго. 
    Потребителското име и паролата не са криптирани, 
    а са конструирани по следния начин:
    
         п.име и паролата са свързани в string: username:password
         този string е кодиран с Base64
         ключовата дума Basic се поставя преди тази кодирана стойност

import basicAuth from 'basic-auth';

'''





































































