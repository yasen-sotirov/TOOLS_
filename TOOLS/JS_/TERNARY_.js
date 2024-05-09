// TERNARY OPERATOR


let num = 5;
console.log(num % 2 == 0 ? "even" : "odd")


let age = 21;
let message = age >= 18 ? "You are adult" : "You are a minor";
console.log(message);



let time = 11;
let greeting = time < 12 ? "Good morning" : "Good afternoon";
console.log(greeting);


let isStudent = true;
let mesg = isStudent ? "Go to school" : "Go to work";
console.log(mesg);


let purchase = 125;
let limit = 100;
let addDiscount = purchase > limit ? 0.1 : 0;
console.log(`Your discount is ${purchase * addDiscount}`) 
