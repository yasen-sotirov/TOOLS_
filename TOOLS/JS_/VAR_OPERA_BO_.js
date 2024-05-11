/* VARIABLES
  - camelCase
  - не се налага ръчно да описваме типа данни 
    дето ще се съхраняват в променливата   
    
    



ДЕКЛАРИРАНЕ - ако не са декларирани JS ще създаде global scope променлива
  let       - променливи, които ще бъдат прпменяни в бъдеще,  block scope
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



console.log(18=='18')     // свободно равенство, ползва TYPE COERCION 

// ВИНАГИ СЕ ПОЛЗВА ===
console.log(18==='18')    // строго равенство, сравнява и типа 
console.log(18===18)




/* MATH + - * /
  ред на операторите  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence   */

let num = 4 + 6;
console.log(num + 10, num **2);







/* ===  BOLEAN === */
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





// EXPRESION - израз, произвежда стойност

// STATEMANT - твърдение, цели изречения, които се изпълняват