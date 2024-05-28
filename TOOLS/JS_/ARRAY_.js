"ARRAY"   // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

"СЪЗДАВАНЕ"
// console.log(new Array(5));			// прави масив с 5 празни слота
let numArray = new Array(1, 2, 3, 4, 5);



"ДОБАВЯНЕ"
// let array = [1, 2, 3, 4, 5];

// array.push(6);                    // добавя накрая
// array[9] = 7;                     // добавя na индекс + празени слотове ако масива не е толкова пълен
// console.log(array);

// array.unshift(0);                  // добавя в началото
// console.log(array)



"ПРЕМАХВАНЕ"
// let array = [1, 2, 3, 4, 5];

// console.log(array)
// console.log('последен елемент: ', array.pop());   // премахва последния и го пази, не приема параметри
// console.log(array);

// console.log(array);
// console.log('първи елемент: ', array.shift());    // премахва първия елемент и го пази, не приема параметри
// console.log(array);



"SLICE"     // НЕ мутира стария масив
// let array = [1, 2, 3, 4, 5];
// console.log("от инд 3 нататък", array.slice(2));
// console.log("от инд 2 до 4", array.slice(2, 4));
// console.log("от -2 до края", array.slice(-2));
// console.log("последен ел", array.slice(-1));
// console.log("от -4 до -2", array.slice(-4, -2));



"SPLICE"     /* 
  - мутира стария масив 
  - същите методи са валидни
  - интересува ни резултатът в стария масив   */ 
// let array = [1, 2, 3, 4, 5];

// array.splice(4);
// console.log(array);

// array.splice(2, 4)
// console.log(array);

// array.splice(-2)
// console.log(array);



"EXPRESSION"     // може да сложим всякакви изрази в масива
// let firstName = "Stamat";
// let age = 1986;
// let numbers = new Array(1, 2, 3);
// let description = new Array(firstName, 2024-age, numbers);
// console.log(description)



"ВРЪЩА ДЪЛЖИНАТА НА МАСИВА"
// array1 = ['one', 'two', 'three'];
// console.log("дължина:", array1.length);



"КОПИЕ"   // лък и меч
// let array = [1, 2, 3, 4];
// let arr2 = [...array];



"ПОКАЗВА НА ИНДЕКС"
// array1 = ['one', 'two', 'three'];

// console.log("елемент на индекс 1: ", array1[1]);
// console.log("индекс на елемент 'three': ", array1.indexOf("three"));    // -1 ако го няма
// console.log('findIndex', array1.findIndex(i => i.length == 5));					// връща първото попадение, работи само с функции
// console.log('ел на последен индекс:', array1[array1.length-1])      		// или арр[-1]



"ЕЛЕМЕНТ @"   // позволява method chaining
// array = ['one', 'two', 'three'];
// console.log(array.at(1));



"ИМА ЛИ ГО В МАСИВА"							// работи с равенство
// array1 = ['one', 'two', 'three'];
// console.log('има ли four: ', array1.includes('four'))



"ИМА ЛИ ЕЛ ОТГОВАРЯЩ НА УСЛОВИЕ"		// работи с условие
// const array = [1, 2, 3, -5, -6, 0, -3];
// console.log(array.some(arr => arr > 0 && arr < 3));



"ИЗРАВНЯВАНЕ"		
// const arrDeep = [[1, 2, [3, 4, [5, 6]]]];
// console.log(arrDeep.flat());
// console.log(arrDeep.flat(3));



"FLATMAP"		// изравнява само на едно ниво



"СОРТИРАНЕ"		/* 
	- мутира обекта
	- конвертира в стринг и тогава сортира			*/

'по азбучен ред'
// const array = [5, 3, 2, -1, 1, 4, -2];
// console.log(array.sort());				

'по големина'
const array2 = [5, 3, 2, -1, 1, 4, -2];
// return < 0, A, B (keep order)
// return > 0, B, A (switch order)

'ascending order'
// дълго записване
// array2.sort((a, b) =>{		
// 	if (a > b) return 1;
// 	if (a < b) return -1;
// })

//съкратено записване
// array2.sort((a, b) => a - b);
// console.log(array2);

'descending order'
// дълго записване
// array2.sort((a, b) =>{		
// 	if (a > b) return -1;
// 	if (a < b) return 1;
// })

//съкратено записване
// array2.sort((a, b) => b - a);
// console.log(array2);



"FROM METHOD"
// const numArr = Array.from({length: 7} , (_, i) => i+2);
// console.log(numArr);




"ПЪЛНИ С ЕДНАКВИ ЕЛ"
// let array = [2, 3, 4, 5, 6]
// console.log(array.fill('a'));				// пълни с 'a'

// let array = [2, 3, 4, 5, 6]
// console.log(array.fill('а', 1, 3));				// пълни с 'a' от 1 до 3



"ДЕКОНСТРУКЦИЯ"   // присвояване на елементи от масива
// const arr = [2, 3, ['a', 'b'], 5, 6];

// const [x, y, z] = arr;
// console.log(x, y, z);               // присвоява първите три елемента към променливите x, y, z

// const [a, , [b, c]] = arr;          // изпуска елемент и достъпва вложения списък
// console.log(a, b, c);

// [first, last] = [last, first];      // сменя им местата
// console.log(first, last);



"ОБРЪЩА РЕДА"     // мутира обекта
// let array = [1, 2, 3, 4];
// array.reverse()
// console.log(array);



"ENTRIES == ENUMERATE  "  
// const menu = ['a', 'b', 'c', 'd', 'e'];
// for (const el of menu.entries()) console.log(el);

// for (const el of menu.entries()) console.log(`№ ${el[0]}: ${el[1]}`);

// for (const [i, el] of menu.entries()) console.log(`№ ${i}: ${el}`);



"JOIN"  // обединява елементите на масива в стринг
// let strArray = ['a', 'b', 'c', 'd'];
// console.log(strArray.join());
// console.log(strArray.join("-"));



"ОБЕДИНЯВАНЕ"   
// const arr1 = [1, 2, 3]
// const arr2 = [4, 5, 6]
// const arr12 = arr1.concat(arr2);
// console.log(arr12);



"...SPREAD"   // разопакова масива

	// let strArray2 = ['a', 'b', 'c', 'd', 'e'];
	// console.log(strArray2);
	// console.log(...strArray2);


	"обединяване на два масива"   // разопаковани са и сложени в нов масив  
	// let array1 = ['one', 'two', 'three'];
	// let combine = [...array1, ...strArray2, "eggs"];
	// console.log("обединява", combine);


	"Подаване на много променливи във функция - args"
	// const addNums = function (...nums) {
	// 	let sum = 0;
	// 	for (let i = 0; i<nums.length; i++)
	// 		sum += nums[i];
	// 	console.log(sum);
	// 	}
	
	// const n1 = 4;
	// const n2 = 5;
	// const n3 = 6;
	// addNums(n1, n2, n3)

	// const n = [1, 2, 3];
	// addNums(...n)


	"Нацепване на iterables, раздробява стрингове "
	// const stringName = 'Jonas';
	// console.log(...stringName, '', 'S' );


	"Разопаковане в обект"
	// const objPerson = {
	// 	firstName: 'Yasen',
	// 	lastName: 'Sotirov'
	// }

	// const objPersonExtend = {
	// 	...objPerson,
	// 	email: 'mail@gmail.com',
	// 	number: 123456,
	// }
	// console.log(objPersonExtend);



"MAP"  // създава нов масив, прилага действие към всеки елемент
// const arrayBGN = [2.50, 3.40, 4.80, 5.20];

// const toEuro1 = arrayBGN.map(el => el * 1.95);
// const toEuro2 = arrayBGN.map((el, i) => `${i+1}: ${el * 1.95}`);

// 'или като функция'
// const convertEuro = arrayBGN.map(function (el) {
//   return el * 1.95
// });

// console.log(toEuro1);
// console.log(toEuro2);



"FILTER"    // създава нов списък от елементи отговарящи на условие
// const movements = [-100, 20, 50, -30, 40];
// const positive = movements.filter(el => el > 0)
// console.log(positive);



"REDUCE"    /* редуцира елементите до един
  - accu - събирателна
  - current     - текущ елемент на итерацията
  - i           - индекс на елемента
  - arr         - целия списък
  - }, 0)       - начална точна на натрупването      */

// const movements = [10, 20, 30, 40, 50];

// const balance = movements.reduce((acc, current, i, array) => acc + current, 0)
// console.log(`result: ${balance}`);

// const max = movements.reduce((acc, curr) => {
//   if (acc > curr) return acc;
//   else return curr;
// }, movements[0]);
// console.log(max);



"FIND" 		// връща първото попадение. Особено полезно при списък с обекти
// const result = numArray.find(el => el === 4);
// console.log(result);



"FOR EACH"
// const dogs = [
//   { weight: 22, curFood: 250, owners: ['Alice', 'Bob'] },
//   { weight: 8, curFood: 200, owners: ['Matilda'] },
//   { weight: 13, curFood: 275, owners: ['Sarah', 'John'] },
//   { weight: 32, curFood: 340, owners: ['Michael'] }
// ];

// dogs.forEach(dog => dog.recFood = Math.trunc(dog.weight ** 0.75 * 28))
// console.log(dogs);







" --= Coding Challenge =-- "

/* 
We're building a football betting app!

Suppose we get data from a web service about a certain game (below). 
In this challenge we're gonna work with the data. So here are your tasks:

1. Create one player array for each team (variables 'players1' and 'players2')

2. The first player in any player array is the goalkeeper and the others are field players. 
   For Bayern Munich (team 1) create one variable ('gk') with the goalkeeper's name, 
   and one array ('fieldPlayers') with all the remaining 10 field players

3. Create an array 'allPlayers' containing all players of both teams (22 players)

4. During the game, Bayern Munich (team 1) used 3 substitute players. 
   So create a new array ('players1Final') containing all the original team1 players plus 
   'Thiago', 'Coutinho' and 'Perisic'

5. Based on the game.odds object, create one variable for each odd (called 'team1', 'draw' and 'team2')

6. Write a function ('printGoals') that receives an arbitrary number of player names (NOT an array) 
   and prints each of them to the console, along with the number of goals that were scored in total 
   (number of player names passed in)

7. The team with the lower odd is more likely to win. Print to the console which team 
   is more likely to win, WITHOUT using an if/else statement or the ternary operator.

TEST DATA FOR 6: Use players 'Davies', 'Muller', 'Lewandowski' and 'Kimmich'. Then, call the function again with players from game.scored

GOOD LUCK 😀
*/

// const game = {
//   team1: "Bayern Munich",
//   team2: "Borrussia Dortmund",
//   players: [
//     [
//       "Neuer",
//       "Pavard",
//       "Martinez",
//       "Alaba",
//       "Davies",
//       "Kimmich",
//       "Goretzka",
//       "Coman",
//       "Muller",
//       "Gnarby",
//       "Lewandowski",
//     ],
//     [
//       "Burki",
//       "Schulz",
//       "Hummels",
//       "Akanji",
//       "Hakimi",
//       "Weigl",
//       "Witsel",
//       "Hazard",
//       "Brandt",
//       "Sancho",
//       "Gotze",
//     ],
//   ],
//   score: "4:0",
//   scored: ["Lewandowski", "Gnarby", "Lewandowski", "Hummels"],
//   date: "Nov 9th, 2037",
//   odds: {
//     team1: 1.33,
//     x: 3.25,
//     team2: 6.5,
//   },
// };

// // 1.
// console.log("--- 1 ---");
// const [players1, players2] = game.players;
// console.log(players1, players2);

// // 2.
// console.log("--- 2 ---");
// const [gk, ...fieldPlayers] = players1;

// // 3.
// console.log("--- 3 ---");
// const allPlayers = [...game.players[0], ...game.players[1]];
// console.log("3. all players: ", "\n", allPlayers, "\n");

// // 4. Players1Final
// console.log("--- 4 ---");
// const players1Final = [...game.players[0], "Thiago", "Coutinho", "Perisic"];
// console.log("Players 1 final:", "\n", players1Final, "\n");

// // 5.
// console.log("--- 5 ---");
// const {
//   odds: { team1, x: draw, team2 },
// } = game;
// console.log("team 1: ", team1, "draw", draw, "team 2:", team2, "\n");

// //      това пак става, но не е по задание
// //      const { team1, x, team2 } = game.odds;
// //      console.log("team 1:", team1, "\n", "draw;", x, "\n", "team 2:", team2, "\n");

// // 6.
// console.log("--- 6 ---");
// function printGoals(...players) {
//   console.log(`${players.length} goals was scored.`, "\n");
// }
// printGoals("Lewandowski", "Gnarby", "Lewandowski", "Hummels");
// printGoals(...game.scored);

// // 7.
// console.log("--- 7 ---");
// team1 < team2 && console.log("Team 1 is more likely to win.");
// team1 > team2 && console.log("Team 2 is more likely to win.");
