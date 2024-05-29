"NUMS"
// NaN  - не е число




"STR -> NUM"
// console.log(Number('2024'));
// console.log(+'2024');

'int'
// console.log(Number.parseInt('  22paragraph'));        // работи ако числото е в началото
// console.log(Number.parseInt('1234567890', 5));          // регекс дето няма логика        

'float'
// console.log(Number.parseFloat('  22.5 paragraph'));    


"NUM -> STR"
// console.log(String(2024));
// console.log(numToString + "");




"TYPE COERCION  - автоматично конвертира "
' + / конвертира към str'
// console.log('I am ' + 23 + ' years old.' );
// console.log('23' + '10' + 3);     // 23103
// console.log('20' / '5' / 2);      // 2

' - * конвертира към number'
// console.log('23' - '10' - 3);     // 10
// console.log('3' * '10' * 3);      // 90

'комбинации'
// console.log('23' + '10' - 3);     // 2307

// let n = '1' + 1;
// console.log(n = n - 1)            // 10




"ЗАКРЪГЛЯНЕ"  // type coercion - работят и със string
// console.log(Math.round(10.4));         // класическо закръгляне
// console.log(Math.round('10.5'));
// console.log(Math.round(10.6));

// console.log('floor 10.6:', Math.floor(10.6));         // закръгля надолу
// console.log('ceil str 10.3:', Math.ceil('10.3'));     // закръгля нагоре
// console.log('trunc 10.3365:', Math.trunc(10.33652));  // премахва всичко след запетаята  

// console.log('trunc -10.3:', Math.trunc(-10.3));        // -10
// console.log('floor -10.3:', Math.floor(-10.3));        // -11

// console.log(10.9.toFixed(2));        // връща STRING, добавя до ор знак
// console.log(10.256.toFixed(2));      // връща STRING, премахва до ор знак
// console.log(+10.256.toFixed(2));     // връща FLOAT, премахва до ор знак



"ЧИСЛО ЛИ Е?  float / int"      // THE BEST WAY!
// console.log(Number.isFinite(20));       // true
// console.log(Number.isFinite(20.2));     // true
// console.log(Number.isFinite('20'));     // false
// console.log(Number.isFinite(+'20'));    // true



"INT ЛИ Е?"
// console.log(Number.isInteger(20));        // true
// console.log(Number.isInteger(20.0));      // true
// console.log(Number.isInteger(+'20.0'));   // true



"НЕ-ЧИСЛО ЛИ Е  NaN"    // тегаво е, много изключения има
// console.log('NaN', Number.isNaN(20));
// console.log('NaN', Number.isNaN('20'));
// console.log('NaN', Number.isNaN('str'));
// console.log('NaN', Number.isNaN(+'str'));
// console.log('NaN', Number.isNaN(20/0));



"MATH LIB"
  // let e = Math.pow(5, 2)         // степенува
  
  'коренуване'
    'квадратен'
      // console.log(Math.sqrt(81)); 
      // console.log(81 ** (1/2)); 
    'кубичен'
      // console.log(8 ** (1/3)); 

    // console.log(Math.sin(1));
    // console.log(Math.log(2));            // логаритъм
    // console.log(Math.cos(1));
    // console.log(Math.tan(1));
    // console.log(Math.abs(-10));         // маха минуса
    // console.log(Math.sign(-10));
  'min max'
    // console.log(Math.max(1, 5, '6', '10'));
    // console.log(Math.min('1', 5, 6, 10));
  'pi'
    // console.log((Math.PI).toFixed(4));



"RANDOM"
// console.log(Math.random());                       // 0-1
// console.log(Math.trunc(Math.random() * 6) +1);    // 1-6
// console.log(Math.floor(Math.random() * 6));       // 0-6

// const randGen = (min, max) => Math.floor(Math.random() * (max - min) + 1) + min
// console.log(randGen(10, 20));                         




"RANDOM COLOR GENERATOR"
// function getRandomColor() {
//   var letters = "0123456789ABCDEF";
//   var color = "#";
//   for (var i = 0; i < 6; i++) {
//     color += letters[Math.floor(Math.random() * 16)];
//   }
//   return color;
// }

// function changeHeaderColor() {
//   header.style.color = getRandomColor();
// }

// setInterval(changeHeaderColor(), 500); // в милисекунди



"ДЕЛЕНЕ"
// console.log(5 % 2);   // reminder, връща остатъка
// console.log(5 / 2);   // обикновено делене


"ЧЕТНИ И НЕЧЕТНИ"
// const isEven = num => num % 2 === 0; 
// console.log(isEven(8));
// console.log(isEven(23));


"NUMERIC SEPARATOR"
// console.log(123_456_789);
// console.log('length in mm: ', 15_2);
// console.log('price in cents: ', 15_99);