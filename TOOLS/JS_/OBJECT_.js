/* OBJECTS - HASH TABLE (DICT)
  - ключът няма кавички
  - приема всякакъв тип обекти
  - редът няма значение   
  - в обекта може да се вложи функция, която да се извиква отвън      */



let person = { 
  firstName: "Jonas", 
  lastName: 'Stamatov', 
  birthYear: 1986, 
  friends: ['Johe', 'Ann', 'Stamat'], 
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
  friends: ['Johe', 'Ann', 'Stamat'], 
  location: 'Portugal'
};
person['email'] = 'jonas@gmail.com';
console.log(person.email)

// ПРИНТИРА ЦЕЛИЯ ОБЕКТ
console.dir(person);




// ИТЕРИРАНЕ ПРЕЗ ОБЕКТА - без ред
for (key in person) {
  console.log(key);
  console.log(person[key]);
}




// THIS METHOD - функция в обекта
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,

  fullName: function () {
    return this.firstName + " " + this.lastName;
  },
};

console.log(person.fullName());
