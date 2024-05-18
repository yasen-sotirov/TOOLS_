/* NOTES

JAVA SCRIPT definitions
https://www.youtube.com/watch?v=q4bHXogfa8A&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=82


HIGH-LEVEL LANGUAGE
  - не се занимавам с ресурсите на хардуера
  - не е толкова бърз колкото low level

GARBAGE COLLECTED
  - има си го вграден
  

MULTI-PARADIGM - подържа и трите
  Procedural programming - пишем командите ред по ред
  OOP - класове и обекти
  Functional - функции


Prototype-Based Object-Oriented
  почти всичко е обект (освен примитивите) 
  
  
FIRST-CLASS FUNCTIONS
  - функциите могат да бъдат третирани като променливи
  - може функция да връща функция и др подобни
  - позволява функционалното програмиране


DYNAMIC TYPED (не е strongly typed)
  - не казваме на променливите какъв тип са - те сами разбират
  - типа променливи може да бъде променян при преназначаване на променливата


NON-BLOCKING EVENT LOOP
  - concurrency model - how the JS engine handles multiple tasks happening at the same time
  - JS is single thread - това е пътеката, по която JS подава на CPU задачите за смятане
  - ако има тежка и дълга задача я прави на заден план и когато я свърши я връща в thread-a



JS ENGINE 
  - изпълнява кода
  - всеки браузър си има свой engine
  - най-добре познатият е на Google: V8 engine
  - както и Node.js

  ЕЛЕМЕНТИ НА ENGINE
    - CALL STACK - тук се изпълнява кода ред по ред
    - HEAP - съдържа всички обекти in memory 




COMPILATION vs. INTERPRETATION
  
  COMPILATION
    - преработва целия код до машинен език наведнъж
    - кода се записва на portable файл, който може 
      да бъде изпълнен на всеки компютър 

  INTERPRETATION
    - минава през кода и го изпълнява ред по ред
    - много по-бавен метод

  JIT - Just in Time 
    - комбинация от горните две
    - модерният JS използва този метод
    - много по-бърз вариант
    1. преработва целия код до машинен език наведнъж 
    2. изпълнява кода наведнъж веднага след комкпилирането
       няма portable файл
  
    ПРИМЕР
      1. Parsing - прочита/анализира кода
      - кода се преработва до структура от данни Abstract Syntactic Tree
      - разделя кода на смислови части - променливи

      2. Компилиране - прави го на машинен код

      3. Започва да изпълнява кода незабавно (без преносим файл)
        - подкарва малка част от кода. Не е оптимизиран, колкото да върши нещо.
        - през това време оптимизира следващата част от кода
        - този цикъл се върти постоянно в отделен thread, недостъпен за нас

        EXECUTION
          1. създава Global execution context - всичко необходимо, за да работи кода
             - вътре включва Top level code - кода извън функциите, кода дето подкарва нещата
          2. изпълнява top-level code
          3. изпълнява функциите и чака Callbacks
            - за всяка функция се създава Execution context,
              за да може тя да бъде изпълнена
            
              Execution context се трупат един след друг в call stack-a
                съдържа: 
                - аргументи и променливи за функцията 
                - Scope chain - референции към променливи извън скоупа
                - This keyword


            
          4. call stack  чака за ново събитие 


  JAVASCRIPT RUN TIME
    - "кутия" съдържаща всички необходими неща за да работи JS.

    JS ENGINE
      CALL STACK
      HEAP

    WEB APIs
      DOM
      FETCH API

    CALLBACK QUEUE
      EVENT LOOP 
        - взема нещата от опашката и ги подава на call stack-a



SCOPE в JS - scope-а има достъп до всички по-горни scope 
  https://www.youtube.com/watch?v=9cl9DXKmwoE&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=85

  GLOBAL 
    - извън всяка функция или блок

  FUNCTIONAL (local) 
    - във функциията 
    - var e функционален

  BLOCK (ES6+) 
    - само променлици в блока
    - само let и const. 
    - var ще е достъпна и отвън
    - блок е всеки код затворен в {}
    - в 'strict mode' всички функции са block scope (ES6+)    




HOISTING 
  - https://www.youtube.com/watch?v=4wtCUiaq3-g&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=87
  - прави декларираните (обикновените) функции достъпни, преди да бъдат декларирани
      зад сцената:
      - преди изпълнение, кодът е сканиран за декларирани променливи
      - за всяка променлива се прави property в variable environment object

  - temporal dead zone 
    - частта от функцията, където променливата все още не е декларирана
    - тя ще бъде декларирана, но по-надолу

  - не става за:
    - променливи 
    - функции декларирани като променливи, arrow functions

  - ЗА ДА СЕ ИЗБЕГНЕ HOISTING:
    - масово се употревява const, по изключение let;
    - никога не се ползва var;
    - функциите и променливите се декларират в началото на кода
    - var прави property в global window object




https://www.youtube.com/watch?v=1tuIGYX5T64&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=92

PRIMITIVES  -   OBJECTS
call stack      heap

numbers     -   object literal
strings     -   arrays
boolean     -   functions
undefined   -   other
null
symbol 
bigint /



















    */



