"NUMS"
// NaN  - не е число




"TYPE CONVERSION    - ръчно конвертиране"
// const year = '2024';
// console.log(typeof Number(year));



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




"ЗАКРЪГЛЯНЕ СЛЕД ДЕСЕТИЧНА ЗАПЕТАЯ"
// let num = 10;
// console.log(num.toFixed(2));




"MATH LIB"
// let a = Math.round(10.5)
// let b = Math.floor(10.3)
// let c = Math.ceil(10.3)
// let d = Math.trunc(10.33652)   // премахва всичко след запетаята
// let e = Math.pow(5, 2)         // степенува
// let f = Math.sqrt(81)
// let g = Math.log(2)            // логаритъм
// let h = Math.sin(1)
// let i = Math.cos(1)
// let j = Math.tan(1)
// let k = Math.abs(-10)          // маха минуса
// let l = Math.sign(-10)
// let m = Math.min(1, 5,10)
// console.log(d)





"RANDOM"
// let dice = Math.trunc(Math.random() * 6) +1;
// console.log(dice)

// let rand;
// const min = 5;
// const max = 10;

// randomNum = Math.random()                            // между 0 и 1
// randomNum = Math.floor(Math.random() * 6)            // между 0 и 6
// rand = Math.floor(Math.random() * (max - min + 1)) + min; // между 3 и 6
// console.log(rand);





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




"В СТРИНГ"
const numToString = 123456;
console.log(String(numToString));
console.log(numToString + "");
