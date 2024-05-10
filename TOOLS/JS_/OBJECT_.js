// OBJECTS - HASH TABLE (DICT)
// ключът няма кавички
// приема всякакъв тип обекти

let carInfo = { make: "Toyota", year: 2010, codes: [21, 33, 15] };
let family = { name: ''}

family.codes = [1]
family['foo'] = [2]
console.log(family)

// ИЗВИКВАНЕ - с кавички
console.log(carInfo["make"]);
console.log(carInfo.make)
console.log(carInfo["codes"][1]);

console.log(carInfo.make);

let PI = 3.1415;

// ПРОМЯНА
carInfo["year"] += 2;
console.log(carInfo["year"]);

// ПРИНТИРА ЦЕЛИЯ ОБЕКТ
console.dir(carInfo);

// ИТЕРИРАНЕ ПРЕЗ ОБЕКТА - без ред
for (key in carInfo) {
  console.log(key);
  console.log(carInfo[key]);
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
