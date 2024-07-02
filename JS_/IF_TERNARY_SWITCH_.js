/* IF         */ 

// НА ЕДИН РЕД - изпълнява се при true
const years = 18;
if (years === 18) console.log(`You are adult!`)
if (years === 16) console.log(`You are not adult!`)   



// explicit (изрично) return  
const foo = () => {
  const baba = 'baba'
  return baba
}


// implicit (скрито, косвено)





/* === TERNARY OPERATOR  ===  
  вид  CONDITION OPERATOR - statemant на един ред */


let num = 5;
console.log(num % 2 == 0 ? "even" : "odd")


// присвоява се към променлива
let age = 21;
const message = age >= 18 ? "You are adult 🍷" : "You are a minor 💧";
console.log(message);



let purchase = 125;
let limit = 100;
let addDiscount = purchase > limit ? 0.1 : 0;
console.log(`Your discount is ${purchase * addDiscount}`) 


// ВКЛЮЧВАНЕ В TEMPLET LITERAL (F str representation)
age = 16
console.log(`I like to drink ${age >= 18 ? 'wine 🍷' : 'juice 🥤'}`)








/*  ===  SWITCH  === - може би е по-кратко, но напоследък се използва рядко */

let day = 'sunday'

switch (day) {
  case 'monday':
    console.log('1 drink')
    break                       // break иначе ще изпълни всички варианти

  case 'tuesday':
  case 'wednesday':
  case 'thirstday':
    console.log('2-3 drinks')
    break

  case 'friday':
  case 'saturday':
    console.log('5-7 drinks')

  case 'sunday':
    console.log('3-4 drinks')
  
  default:                            // else statemant
    console.log('Not a valid day')
  }   
