// ARRAY
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


let array1 = ['one', 'two', 'three'];
let numArray = new Array(1, 2, 3, 4, 5);



// ДОБАВЯНЕ
array1 = ['one', 'two', 'three'];
console.log('преди: ', array1);

array1.push('four', 'five');        // добавя накрая
array1[12] = 'seven';               // добавя na индекс + празени слотове ако масива не е толкова пълен

array1.unshift('zero');             // добавя в началото
array1.shift('zero');               // добавя в началото
console.log('след: ', array1)



// EXPRESSION - изрази в масива
let firstName = "Stamat";
let age = 1986;
let numbers = new Array(1, 2, 3);
let description = new Array(firstName, 2024-age, numbers);
console.log(description)




// ПРЕМАХВАНЕ
array1 = ['one', 'two', 'three'];
console.log(array1)
console.log('подледен елемент: ', array1.pop());       // премахва последния и го пази
console.log('първи елемент: ', array1.shift());     // премахва първия елемент и го пази
console.log('в масива остана ', array1)




// ВРЪЩА ДЪЛЖИНАТА НА МАСИВА
array1 = ['one', 'two', 'three'];
console.log("дължина:", array1.length);




// ПОКАЗВА НА ИНДЕКС
array1 = ['one', 'two', 'three'];
console.log("елемент на индекс 1: ", array1[1]);
console.log("индекс на елемент 'three': ", array1.indexOf("three"));    // -1 ако го няма
console.log('елемент на последен индекс', array1[array1.length-1])




// ИМА ЛИ ГО В МАСИВА
array1 = ['one', 'two', 'three'];
console.log('има ли four: ', array1.includes('four'))




// ОБХОЖДАНЕ НА МАСИВ
// let array1 = ['one', 'two', 'three'];

console.log("обхождане 1");
for (let i = 0; i < array1.length; i++) {
	console.log(array1[i]);
};


console.log("обхождане 2");
for (let el of array1) {
	console.log(el);
};


console.log("oбратно обхождане");
for (let i = array1.length -1; i >= 0; i--) {
	console.log(array1[i]);
};





// СОРТИРАНЕ
console.log(array1.sort());
console.log(array1.sort().reverse());




// ПРИСВОЯВАНЕ НА ЕЛЕМЕНТИ ОТ МАСИВА - ДЕКОНСТРОИРАНЕ
const arr = [2, 3, ['a', 'b'], 5, 6];
const [x, y, z] = arr;
console.log(x, y, z);               // поредни елементи

const [a, , [b, c]] = arr;          // вложени масиви
console.log(a, b, c);


let [first, , , last] = arr;        // прескача елементи
console.log(first, last);

[first, last] = [last, first];      // сменя им местата
console.log(first, last);



// ОБРЪЩА РЕДА
console.log(array1.reverse());



// ENTRIES == ENUMERATE    
const menu = ['a', 'b', 'c', 'd', 'e'];
for (const el of menu.entries()) console.log(el);

for (const el of menu.entries()) console.log(`№ ${el[0]}: ${el[1]}`);

for (const [i, el] of menu.entries()) console.log(`№ ${i}: ${el}`);






// JOIN - ОБЕДИНЯВА ЕЛЕМЕНТИТЕ НА МАСИВА В СТРИНГ
let strArray = ['a', 'b', 'c', 'd'];
console.log(strArray.join());
console.log(strArray.join("-"));




// -----------------------------
// ...SPREAD - разопакова масива

	let strArray2 = ['a', 'b', 'c', 'd', 'e'];
	console.log(strArray2);
	console.log(...strArray2);


	// обединяване на два масива - разопаковани са и сложени в нов масив  
	let array1 = ['one', 'two', 'three'];
	let combine = [...array1, ...strArray2, "eggs"];
	console.log("обединява", combine);



	// Подаване на много променливи във функция - args
	const addNums = function (...nums) {
		let sum = 0;
		for (let i = 0; i<nums.length; i++)
			sum += nums[i];
		console.log(sum);
		}
	
	const n1 = 4;
	const n2 = 5;
	const n3 = 6;
	addNums(n1, n2, n3)

	const n = [1, 2, 3];
	addNums(...n)


	// Нацепване на iterables, раздробява стрингове 
	const stringName = 'Jonas';
	console.log(...stringName, '', 'S' );


	// Разопаковане в обект
	const objPerson = {
		firstName: 'Yasen',
		lastName: 'Sotirov'
	}

	const objPersonExtend = {
		...objPerson,
		email: 'mail@gmail.com',
		number: 123456,
	}
	console.log(objPersonExtend);




// -------- Coding Challenge #1

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

const game = {
  team1: "Bayern Munich",
  team2: "Borrussia Dortmund",
  players: [
    [
      "Neuer",
      "Pavard",
      "Martinez",
      "Alaba",
      "Davies",
      "Kimmich",
      "Goretzka",
      "Coman",
      "Muller",
      "Gnarby",
      "Lewandowski",
    ],
    [
      "Burki",
      "Schulz",
      "Hummels",
      "Akanji",
      "Hakimi",
      "Weigl",
      "Witsel",
      "Hazard",
      "Brandt",
      "Sancho",
      "Gotze",
    ],
  ],
  score: "4:0",
  scored: ["Lewandowski", "Gnarby", "Lewandowski", "Hummels"],
  date: "Nov 9th, 2037",
  odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
  },
};

// 1.
console.log("--- 1 ---");
const [players1, players2] = game.players;
console.log(players1, players2);

// 2.
console.log("--- 2 ---");
const [gk, ...fieldPlayers] = players1;

// 3.
console.log("--- 3 ---");
const allPlayers = [...game.players[0], ...game.players[1]];
console.log("3. all players: ", "\n", allPlayers, "\n");

// 4. Players1Final
console.log("--- 4 ---");
const players1Final = [...game.players[0], "Thiago", "Coutinho", "Perisic"];
console.log("Players 1 final:", "\n", players1Final, "\n");

// 5.
console.log("--- 5 ---");
const {
  odds: { team1, x: draw, team2 },
} = game;
console.log("team 1: ", team1, "draw", draw, "team 2:", team2, "\n");

//      това пак става, но не е по задание
//      const { team1, x, team2 } = game.odds;
//      console.log("team 1:", team1, "\n", "draw;", x, "\n", "team 2:", team2, "\n");

// 6.
console.log("--- 6 ---");
function printGoals(...players) {
  console.log(`${players.length} goals was scored.`, "\n");
}
printGoals("Lewandowski", "Gnarby", "Lewandowski", "Hummels");
printGoals(...game.scored);

// 7.
console.log("--- 7 ---");
team1 < team2 && console.log("Team 1 is more likely to win.");
team1 > team2 && console.log("Team 2 is more likely to win.");
