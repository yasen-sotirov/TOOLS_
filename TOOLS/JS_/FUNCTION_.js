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
	- функция, която е присвоена към променлива;
	- извиква се посредством променливата, към която е придадена;
	- може да има име, но то би се ползвало само вътре във функцията, например за рекурсия
	- присъединява се директно към променлива
	- не може да бъде извикана преди да бъде написана
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









"CLOSURE" 		// функция комбинирана с нейното външно състояние
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

console.dir(secureBooking)

/*
https://www.youtube.com/watch?v=vKJpN5FAeF4&list=LL&index=2&ab_channel=Fireship

Closure се отнася до функция, която има достъп до стойности извън собственият си скоуп.

За да извика функцията, интерпретаторът (V8) трябва да знае за самата функция 
и всички други данни от заобикалящата среда, от които функцията зависи.
Всичко трябва да бъде затворен в „кутия“, преди да може да бъде въведен в engine-a.

Чиста функция - зависи само от собствените си аргументи и вътрешни данни. 
	Това е напълно самостоятелен затворен израз.
	Когато се извика, се насочва към call stack, където се изпълнява.
	Вътрешните му данни се съхраняват само в call stack.

Closure - при функция, която препраща към данни извън собствения си scope или връща отворен израз.
	за да може интерпретаторът да извика тази функция
	и също да знае стойността на тези външни променливи, 
	създава Closure. Съхранява се на място в паметта (HEAP MEMORY), 
	където могат да бъдат достъпни по-късно.

HEAP може да съхранява данни в паметта за неопределено време,
за разлика от Call stack, който е краткотраен.
Closure изисква повече памет и мощност за обработка, отколкото чиста функция.
Най-често се ползва за енкапсулация на данни - да се предотврати изтичането 
или а данни там, където не е необходимо,

Създаване:
можем да създадем Closure  чрез дефиниране на външна функция, 
която съдържа състоянието, след това вътрешна функция, 
която работи върху него. Съдържащите се тук данни няма да изтекат
в заобикалящата среда. Вътрешната функция има достъп до данни,
дефинирани в скоупа на външната функция, 
но външната функция няма достъп  към вътрешната функция

 */