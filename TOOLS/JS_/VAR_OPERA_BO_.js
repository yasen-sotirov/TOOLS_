/* VARIABLES
  - camelCase
  - не се налага ръчно да описваме типа данни 
    дето ще се съхраняват в променливата   
    
    



ДЕКЛАРИРАНЕ - ако не са декларирани JS ще създаде global scope променлива
  let       - променливи, които ще бъдат прoменяни в бъдеще,  block scope
  const     - не се променят, не може да бъдат undefined
  var       - старият начин, да не се използва вече           functional scope  */




// VARIABLE TYPES
let w;              // undefined, после ще присъединим стойност към нея
let x = 5.0;        // number, not float
let y = 5;          // number, not int
let z = true;       // 
z = "John";         // reassign, mutation





// ctrl + alt + n
console.log(typeof x);
console.log(typeof y);
console.log(typeof z);




/* ===  ОПЕРАТОРИ  === 

  AND = &&
          t       f
  t     TRUE    FALSE
  f     FALSE   FALSE


  OR = ||
          t       f
  t     TRUE    TRUE
  f     TRUE    FALSE      
  
  
  NOT = !
  f == !true
  t == !false         */


  



// ВИНАГИ СЕ ПОЛЗВА ===
console.log(18=='18')     // свободно равенство, ползва TYPE COERCION 
console.log(18==='18')    // строго равенство, сравнява и типа 
console.log(18===18)




/* MATH + - * /
  ред на операторите  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence   */

let num = 4 + 6;
console.log(num + 10, num **2);







/* ===  BOOLEAN === */
// FALSY VALUES - при конвертиране ще станат на false
// 0, "", undefined, null, NaN 

let zero = 0;
let height;
console.log(Boolean(0));
console.log(Boolean(zero));
console.log(Boolean(undefined));
console.log(Boolean(height));
console.log(Boolean(null));
console.log(Boolean(NaN));



// SHORTY CIRCUITING
// ----- OR ----- връща първото truly value или последната, ако всички са falsy
console.log('Jonas' || 3);
console.log('' || 'Jonas');
console.log(true || 0);
console.log(false || 0 || undefined);
console.log(false || 0 || undefined || 23);

// ----- AND ----- връща първото falsy value или последната, ако всички са truly
console.log(0 &&'Jonas');
console.log(true && 0);
console.log(undefined || null);
console.log(30 && true && 'Hello' && 2);

// ----- ?? ------ nullish value: връща стойностите различни от undefined или '', или последния елемент
console.log(undefined ?? 10);
console.log(undefined ?? '');
console.log(undefined ?? 0 ?? 'aa');



// LOGICAL ASSIGN OPERATOR OR
const rest1 = {
  name: 'Capri',
  numGuests: 20,
  location: 0,
};

const rest2 = {
  name: 'La Piazza',
  owner: 'Giovanni'
};

  // ||= Добавяне на property към обекта, ако го няма, чрез OR
  //     ако първата стойност не е truly ще добави втората 
  rest2.numGuests = rest2.numGuests || 10;

  // За по-кратко. Ако пропъртито го има и е falsy, ще го пренапише
  rest1.owner ||= 'Leo';
  console.log(rest1);

  // rest1.location ||= 'Sofia';
  // console.log(rest1.location);



  // ??=  Добавяне на property към обекта, ако e undefined
  //      ако property е falsy, но все пак е дефинирано, нищо няма да бъде асайнато
  rest1.location ??= 'Plovdiv';
  console.log(rest1.location);


  // Пример short circuiting - ако property го има ще бъде заменено с втората стойност
  rest2.owner = rest2.owner && '<anonymous>';
  console.log(rest2.owner);


  // кратък вариант
  rest2.owner &&= '<ANONYMOUS>';
  console.log(rest2.owner);;




// EXPRESSION - израз, произвежда стойност

// STATEMENT - твърдение, цели изречения, които се изпълняват