/* OBJECTS - HASH TABLE (DICT)
  - ключът няма кавички
  - приема всякакъв тип обекти
  - редът няма значение   
  - в обекта може да се вложи функция, която да се извиква отвън
  - представлява object literal, а не code block със собствен scope      */
  


let person = { 
  firstName: "Jonas", 
  lastName: 'Stamatov', 
  birthYear: 1986, 
  friends: ['John', 'Ann', 'Stamat'], 
  location: 'Portugal',
  calacAge: function () {                  
    this.age = 2024 - this.birthYear;     // вмести self
    return this.age},                       // пази калкулацията в age, за да не я пресмята
 
  haveDrivingLicense: true,              
  summary: function() {
    return `${this.firstName} is a ${this.calacAge()}-years old and he has 
    ${this.haveDrivingLicense ? 'a' : 'no'} driver's license.`
  },
};

console.log(person.summary())


const midName = person.midName || 'St.'
console.log(midName);



// ИЗВИКВАНЕ НА ФУНКЦИЯ ОТ ОБЕКТА

console.log(person.calacAge());     // трябва да го пресметне за да може да го върне после
console.log(person.age);            // връща калкулираният резултат 
console.log(person['age']);       // задължително трябват () 
console.log(person.summary())



// СЪКРАТЕНО ЗАПИСВАНЕ НА ФУНКЦИЯ В ОБЕКТ
// https://youtu.be/Mge8gj_J4hI?list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&t=213
const train = {
  speed: 140,
  distance (time){return this.speed * time}
}

console.log(train.distance(1));




// ИЗВИКВАНЕ - с кавички
console.log(person.firstName)
console.log(person["firstName"]);
console.log(person["friends"][1]);


// const infoFor = prompt('ask about: firstName, lastName, ages, friends')
// if (person[infoFor]) {
//   console.log(person[infoFor]);
// } else {
//   console.log('wrong value, try again');
// }





// ПРОМЯНА
console.log(person.years += 2);
console.log(person.location = 'Madrid')

person = { 
  firstName: "Jonas", 
  lastName: 'Stamatov', 
  years: 33, 
  friends: ['John', 'Ann', 'Stamat'], 
  location: 'Portugal'
};
person['email'] = 'jonas@gmail.com';
console.log(person.email)
console.dir(person);





// КЛОНИРАНЕ НА ОБЕКТ
Object.assign({}, person)




// ОТ ОБЕКТ В МАП
console.log('в мап', new Map(Object.entries(person)));



// ДОБАВЯНЕ НА PROPERTY КЪМ ОБЕКТ - нужно е само да се запише променливата
const workHours = {
  mon: {
    open: 9,
    close: 18,
  },
  wed: {
    open: 9,
    close: 18,
  },
}; 

const office = {
  location: 'Sofia',
  workers: 20,
  workHours,        // преди ЕS6:  workHours: workHours,
  callBack(time) {console.log(`Calling you at ${time}`);},
}
// console.log(office);




// OPTIONAL CHAINING    ще продължи по веригата ако tue го има
    // проверява за property 
    console.log(office.workHours.tue?.open);

    const days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
    for (const day of days) {
      const open = office.workHours[day]?.open;
      console.log(`On ${day} we open at ${open ?? 'not work'}.`);
    }

    // проверява за методи
    console.log(office.callBack('12:30'));
    console.log(office.check?.('check') ?? 'Method does not exist');



// ДОСТЪПВАНЕ на KEYS, VALUES, ENTRIES
console.log(Object.keys(workHours));
 
console.log( Object.values(workHours));
  
const entries = Object.entries(workHours);
for (const [key, {open, close}] of entries) {
  console.log(`On ${key} we open at ${open} and close at ${close}`);
};

 
 



// ИТЕРИРАНЕ ПРЕЗ ОБЕКТА - без ред
for (key in person) {
  console.log(key);
  console.log(person[key]);
}






/* THIS METHOD 
  - не може да се ползва в arrow function	
  - функция в обекта       */

const JonDoe = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function () {return this.firstName + " " + this.lastName;},
};

console.log(JonDoe.fullName());




// https://www.youtube.com/watch?v=1amgLpnANaM&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=91

console.log(this);		    // когатп е отвън, дава достъп до window object-a
var matilda = 'matilda';  // връзва променливата към global scope







// METHOD BORROWING  https://www.youtube.com/watch?v=GNLHi6lcW6w&list=PLOmL3sL-afbRVTvedkIrQcDwg2UY0JGTF&index=90
// НЕ РАБОТИ - ТРЯБВА ОЩЕ ИНФО

const jonas = {
  year: 1990,
  job: 'teacher',
  calcAge: function () {
    console.log(2024 - this.year);
  },
}
jonas.calcAge();



const maria = {
  year: 1994,
  job: 'instructor',
}

maria.calacAge = jonas.calcAge();   // заема метода от jonas
maria.calcAge();





const yasen = {
  lastName: 'Sotirov',
  year: 1986,
  job: 'developer',
  calcAge: function () {console.log(2024 - this.year);},
  greet: () => console.log(`Greetings ${this.lastName}`),
}

jonas.calcAge();






/* ========= /\ ==========
ДЕСТРУКТУРИРАНЕ НА ОБЕКТ 
  - присвоява стойности от обекта към променливи
  - същото както масива, но с {}   
  - редът няма значение     */

const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  orderDelivery: function ({starterIndex, mainIndex, time, address, paying = 'cash'}){
    console.log( `Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}. Paying method ${paying}. `)
  },

  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
};

// присвоява към променливи елементи от обекта 
const {name, openingHours, categories} = restaurant;    
console.log(
  'name: ', name, '\n',
  'opening hours: ', openingHours, '\n',
  'categories: ', categories
);


// промяна имената на елементите
const {
  name: restaurantName,
  openingHours: hours,
  categories: tags,
} = restaurant

console.log(tags);




/* Присвояване на дефоутна стойност на деструкториран обект
  - ще се приложи ако обектът няма такава стойност
  - не променя обекта  */

const objStr = {
  value: 'abc',
  type: 'str',
}

const {
  type: objType, 
  id = 1000, 
} = objStr;

console.log(objType, id);




// ДЕКОНСТРУИРАНЕ НА ПРОМЕНЛИВИ В ОБЕКТ
let a = 111;
let b = 222;
console.log(a, b);

const mutObj = {a: 1, b:2};
({a, b} = mutObj);
console.log(a, b);




// ДЕКОНСТРУИРАНЕ НА ПРОМЕНЛИВИ ВЪВ ВЛОЖЕН ОБЕКТ
const objDict = {
  value: {open: 8, close: 20},
  type: 'dict',
}


const {value: {open: op, close: cl}} = objDict
console.log(op, cl);




// ДЕКОНСТРУИРАНЕ НА ПАРАМЕТРИ ВЪВ ФУНКЦИЯ
restaurant.orderDelivery({
  time: '13:10',
  address: 'Sofia 1000',
  mainIndex: 2,
  starterIndex: 2,
})


// Вижте повече в [NUM_.js](NUM_.js#L20)





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