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
    return this.age                       // пази калкулацията в age, за да не я пресмята
  },
  haveDrivingLicense: true,
  summary: function() {
    return `${this.firstName} is a ${this.calacAge()}-years old and he has 
    ${this.haveDrivingLicense ? 'a' : 'no'} driver's license.`
  }
};




// ФУНКЦИЯ ОТ

console.log(person.calacAge());     // трябва да го пресметне за да може да го върне после
console.log(person.age);            // връща калкулираният резултат 
console.log(person['age']());       // задължително трябват () 
console.log(person.summary())




// ИЗВИКВАНЕ - с кавички
console.log(person.firstName)
console.log(person["firstName"]);
console.log(person["friends"][1]);


const infoFor = prompt('ask about: firstName, lastName, ages, friends')
if (person[infoFor]) {
  console.log(person[infoFor]);
} else {
  console.log('wrong value, try again');
}





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



// ИТЕРИРАНЕ ПРЕЗ ОБЕКТА - без ред
for (key in person) {
  console.log(key);
  console.log(person[key]);
}








/* THIS METHOD 
  - не може да се ползва в arrow function	
  - функция в обекта       */

const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function () {return this.firstName + " " + this.lastName;},
};

console.log(person.fullName());




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



const matilda = {
  year: 1994,
  job: 'instructor',
}

matilda.calacAge = jonas.calcAge();   // заема метода от jonas
matilda.calcAge();





const yasen = {
  lastName: 'Sotirov',
  year: 1986,
  job: 'developer',
  calcAge: function () {console.log(2024 - this.year);},
  greet: () => console.log(`Greetings ${this.lastName}`),
}

jonas.calcAge();
