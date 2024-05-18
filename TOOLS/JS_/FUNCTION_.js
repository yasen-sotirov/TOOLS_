/* FUNCTIONS 
	- invoking, calling, running - извикване на функцията
	- parameters - параметрите, с които е дефинирана функцията
	- arguments - стойностите дето подаваме на фунцията, за да работи
	  self = this */



/* FUNCTION DECLARATION 
	- декларирана функция
	- може да бъде извикана преди да бъде декларирана  */

function calcAge1 (birthYear) {
	return 2024 - birthYear
}



/* FUNCTION EXPRESSION (израз)
	- функция без име
	- присъединява се директно към променлива
	- не може да бъде извикане преди да бъде написана			*/

const calcAge = function(birthYear) {
	return 2024 - birthYear
}
console.log(calcAge(1986))





/* ARROW FUNCTION 
	- съкратено записване на Function expression - подходяща е за един ред
	- return е косвен (implicit)		
	- не могат да ползват This     */

const calcAge2 = birthYear => 2024 - birthYear;
console.log(calcAge2(1984));


const yearUntilRetirement = (birthYear, firstName) => {
	const age = 2024 - birthYear;
	const retirement = 65 - age;
	return `${firstName} retires in ${retirement} years.`; 
}
console.log(yearUntilRetirement(1986, 'Yasen'))










// ...SPREAD - REST PARAMETER  (args)
const food1 = "eggs";
const food2 = "meat";
const food3 = "bread";
const food4 = "ham";

function makeSandwich(...args){
	console.log(args)
};

makeSandwich(food1, food2, food3, food4);



// пример 2
function sumNums(...numbers){
	let result = 0;
	for(let num of numbers){
		result += num;
	}
	return result;
}

const totalSum = sumNums(1, 2, 3, 4, 5, 6, 7, 8, 9)

console.log(`The total is: ${totalSum}`);




// ARGUMENTS - не се ползва в последно време
const addExpr = function (a, b) {
	console.log(arguments);
	return a + b;
};

addExpr(2, 5);
addExpr(2, 5, 6, 8, 7);
console.log(addExpr(2, 5));






