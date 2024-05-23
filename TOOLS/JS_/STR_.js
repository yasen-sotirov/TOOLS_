"STRINGS" 
/*  - примитив
    - методите работят върху стринг, защото зад сцената 
      JS превръща примитива в обект и тогава прилага метода
      този процес се нарича boxing. След приключване на метода 
      стринга пак се конвертира в примитив     
    
    още методи: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String  */


// console.log(new String('new string method'));
// console.log(typeof new String('new string method'));



"SPLIT"
console.log('a+very+nice+string'.split('+'));

const paragraph = `This is a
  simple, multiline 
  text on JavaScript`
console.log(paragraph.split('\n'));


[first, last] = 'John Smit'.split(" ");
console.log(first, last);



"JOIN"
// const fullName = ['mr.', 'Yasen', 'Chavdarov', 'Sotirov'];
// console.log(fullName.join(" "));
// console.log(fullName.join("_"));



"PADDING - добавя символи до опр дължина"
// console.log('banana'.padStart(10, '+-'));
// console.log('banana'.padEnd(10, '+'));



"REPEAT"
console.log('sunny weather '.repeat(3), '\n');



"TEMPLATE LITERALS  от ES6+.  Като f стринга"
// const birthday = 1986;
// let yearNow = 2024;
// const job = 'teacher'
// console.log(`I'm ${yearNow - birthday} years old 
// and my job is ${job}.`)




"ДЪЛЖИНА НА СТРИНГ"
// console.log("Django".length);
// console.log("four four".length);




"КОНВЕРТИРАНЕ В СТРИНГ"
// const year = 2024
// console.log(typeof String(year))




"БУКВА НА ИНДЕКС И ИНДЕКС НА БУКВА"
// let userName = "Bro Code tut";
// console.log(userName[0]);
// console.log('BroCode'[1]);

// console.log(userName.charAt(3));
// console.log(userName.indexOf("o"));         // първо появяване
// console.log(userName.lastIndexOf("o"));     // последно появяване
// console.log(userName.lastIndexOf("tut"));     // последно появяване




"ПРЕМАХВА ПРАЗНО - STRIP"
// let testStr = "  BroCode  ";
// console.log("трие от ляво и дясно", testStr.trim())
// console.log("трие от дясно", testStr.trimEnd())
// console.log("трие от ляво", testStr.trimStart())




"ГЛАВНИ И И МАЛКИ БУКВИ"
// let textCase = "abCDefj";
// console.log(textCase.toLowerCase());
// console.log(textCase.toUpperCase());




"ПОВТАРЯ СТРИНГА"
// console.log("repeat! ".repeat(3));




"ДАЛИ ЗАПОЧВА ЗАВЪРШВА С"
// console.log(" BroCode".startsWith(" ")); 
// console.log(" BroCode".endsWith(" ")); 




"СЪДЪРЖА ЛИ"
// console.log("съдържа ли @", "mail@abv.bg".includes("@"));




"ЗАМЕНЯ СИМВОЛИ - на практика създава нов стринг"
// const price = '288.97$';
// const phone = "+359-886-800-800";
// console.log("заменя един", price.replace(".", ",").replace('$', '€'))
// console.log("заменя всички", phone.replaceAll("-", " "));
// console.log("заменя всички с regex", phone.replace(/-/g, "  "));





"ДОБАВЯ ЕЛЕМЕНТИ ПРЕДИ и СЛЕД СТРИНГА - PADDING"
// console.log("PADDING", "886-800-800".padStart(13, "0"));
// console.log("PADDING", "886-800-800".padEnd(13, "0"));



"SLICING"
// const str1 = 'Working with strings tutorial'
// console.log("отрязък", "BroCode!".slice(2));                    // събстринг от- до края: 
// console.log("отрязък: ", "BroCode!".slice(0, 4));
// console.log("последните 3: ", "BroCode!".slice(-3));                
// console.log('първа дума', str1.slice(0, str1.indexOf(' ')));    // първа дума

// let fullName = "Bro Code"
// console.log("first name: ", fullName.slice(0, fullName.indexOf(" ")));
// console.log("last name: ", fullName.slice(fullName.indexOf(" ") + 1));




"РАЗОПАКОВАНЕ - SPREAD OPERATOR"
// let string1 = "Bro Code";
// let letters = [...string1];
// console.log(letters);



"КЪМ МАЛКИ И ГЛАВНИ БУКВИ"
// console.log('TO LOWER CASE'.toLowerCase());
// console.log('to upper case'.toUpperCase());




"ПРИМЕР AIRPLANE"
const flights =
  "_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30";

// 🔴 Delayed Departure from FAO to TXL (11h25)
//              Arrival from BRU to FAO (11h45)
//   🔴 Delayed Arrival from HEL to FAO (12h05)
//            Departure from FAO to LIS (12h30)

// const getCode = (str) => str.slice(0, 3).toUpperCase();

// for (const flight of flights.split("+")) {
//   const [type, from, to, time] = flight.split(";");

//   const output = `${type.startsWith("_Delayed") ? "🔴" : ""} 
//   ${type.replaceAll("_", " ")} 
//   from ${getCode(from)} 
//   to ${getCode(to)} 
//   (${time.replace(":", "h")})`.padStart(36);
//   console.log(output);}
