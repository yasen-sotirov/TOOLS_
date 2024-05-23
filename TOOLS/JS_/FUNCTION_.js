'use strict'
"FUNCTIONS "	/*
	- invoking, calling, running - извикване на функцията
	- parameters - параметрите, с които е дефинирана функцията
	- arguments - стойностите дето подаваме на фунцията, за да работи
	  self = this
	- може да приема обекти като аргументи
	- може да се пропусне подаването на default параметър като се подаде undefined 
	
	-	поддържа First class functions:
		- функциите могат да се третират като стойности	
		- arrow function
		- function in object	
		- това позволява писането на функции от висок ред. 
			водят се heigh order защото дават ниво на абстракция, 
			те са едно ниво нгоре, защото работят с др. фунцийте с ко
			Те позволяват:
			- функция да получава функция като аргумент;
			- функция която връща друга функция			*/
		

			

"ВИДОВЕ ПАРАМЕТРИ"		/*
	- Positional: (a, b, c) важен е реда на подаване. 
	- Key-word:  при извикване на функцията се изписва парам=стойност. 
		Mоже да бъдат разместени при извикване
	- Default: с предварително зададена ст-ст, която може да променим.		
	
	- */



"HEIGH ORDER FUNCTION"		// приема друга функция като аргумент
// const oneWord = function (str) {
// 	return str.replaceAll(" ", "")
// } 

// const upperFirstWord = function (str) {
// 	const [first, ...other] = str.split(" ");
// 	return [first.toUpperCase(), ...other].join(" ");
// }

// 	const transformer = function(str, func) {
// 		console.log(`Original string: ${str}`);
// 		console.log(`Transformed str: ${func(str)}`);
// 		console.log(`Transformed by: ${func.name}`);
// 	}

// const input = 'JavaScript is the Best!';
// console.log('----Results----');
// transformer(input, upperFirstWord)
// console.log('----===----');
// transformer(input, oneWord)






"FUNCTION DECLARATION" /* 
	- декларирана функция
	- може да бъде извикана преди да бъде декларирана  
	- default params ги има като в питон*/

// function calcAge1 (birthYear) {
// 	return 2024 - birthYear
// }

// console.log(calcAge1(1986));





"FUNCTION EXPRESSION"	/*  (израз)
	- функция без име
	- присъединява се директно към променлива
	- не може да бъде извикане преди да бъде написана
	- ползва методите apply, call, bind
	- може да бъде използвана като конструктор с оператора new
	- има prototype свойство
	- има достъп до arguments (съдържа всички аргументи, предадени на функцията)
	- трябва изрично да използвате return			*/

// const calcAge = function(birthYear) {
// 	return 2024 - birthYear
// }
// console.log(calcAge(1986))





"ARROW FUNCTION "	/* 
	- съкратено записване на Function expression - подходяща е за един ред
	- return е косвен (implicit)		
	- не могат да ползват This
	- не ползва методите apply, call, bind
	- няма prototype свойство
	- няма достъп до arguments
	- ако е само един израз, може без return и {  }	     */

// const calcAge2 = birthYear => 2024 - birthYear;
// console.log(calcAge2(1984));


// const yearUntilRetirement = (birthYear, firstName) => {
// 	const age = 2024 - birthYear;
// 	const retirement = 65 - age;
// 	return `${firstName} retires in ${retirement} years.`; 
// }
// console.log(yearUntilRetirement(1986, 'Yasen'))




"НЕЗАБАВНА ФУНКЦИЯ"		/* 
изпълнява се сама и веднъж
за скриване на променливи в скоупа на функцията
не се ползват вече. Със същият успех може кода да се 
изолира в блок { }		*/

// const a = 'const иначе не тръгва';
// (() => console.log('This will never run again'))();




"CLOSURE"
// https://www.youtube.com/watch?v=qnDxLcFMxJ4&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=128
const secureBooking = function () {
	let counter = 0;

	return function () {
		counter++;
		console.log(`${counter} passenger`);
	}
}

const booker = secureBooking();
booker();
booker();
booker();










" ...SPREAD - REST PARAMETER  (args)"
// const food1 = "eggs";
// const food2 = "meat";
// const food3 = "bread";
// const food4 = "ham";

// function makeSandwich(...args){
// 	console.log(args)
// };

// makeSandwich(food1, food2, food3, food4);


// пример 2 
// function sumNums(...numbers){
// 	let result = 0;
// 	for(let num of numbers){
// 		result += num;
// 	}
// 	return result;
// }

// const totalSum = sumNums(1, 2, 3, 4, 5, 6, 7, 8, 9)

// console.log(`The total is: ${totalSum}`);




"ARGUMENTS - не се ползва в последно време"
// const addExpr = function (a, b) {
// 	console.log(arguments);
// 	return a + b;
// };

// addExpr(2, 5);
// addExpr(2, 5, 6, 8, 7);
// console.log(addExpr(2, 5));






