// STRINGS 




// ДЪЛЖИНА НА СТРИНГ
console.log("Django".length);
console.log("four four".length);




// БУКВА НА ИНДЕКС И ИНДЕКС НА БУКВА
let userName = "BroCode";
console.log(userName.charAt(3));
console.log(userName.indexOf("o"));         // първо появяване
console.log(userName.lastIndexOf("o"));     // последно появяване



// ПРЕМАХВА ПРАЗО - STRIP
let testStr = "  BroCode  ";
console.log(testStr.trim())
console.log(testStr.trimEnd())
console.log(testStr.trimStart())



// ГЛАВНИ И ИМАЛКИ БУКВИ
let textCase = "abCDefj";
console.log(textCase.toLowerCase());
console.log(textCase.toUpperCase());



// ПОВТАРЯ СТРИНГА
console.log("repeat! ".repeat(3));



// ДАЛИ ЗАПОЧВА ЗАВЪРШВА С
console.log(" BroCode".startsWith(" ")); 
console.log(" BroCode".endsWith(" ")); 



// СЪДЪРЖА ЛИ
console.log("'mail@abv.bg' съдържа ли @");
console.log("mail@abv.bg".includes("@"));



// ЗАМЕНЯ СИМВОЛИ
console.log("ЗАМЕНЯ СИМВОЛИ:", "0886-800-800".replace("-", ""))
console.log("0886-800-800".replaceAll("-", ""))



// ДОБАВЯ ЕЛЕМЕНТИ ПРЕДИ и СЛЕД СТРИНГА - PADDING
console.log("PADDING", "886-800-800".padStart(13, "0"));
console.log("PADDING", "886-800-800".padEnd(13, "0"));



// SLICING
console.log("отрязък: ", "BroCode!".slice(0, 4));
console.log("последен: ", "BroCode!".slice(-1));

let fullName = "Bro Code"
console.log("first name: ", fullName.slice(0, fullName.indexOf(" ")));
console.log("last name: ", fullName.slice(fullName.indexOf(" ") + 1));




// РАЗОПАКОВАНЕ - SPRED OPERATOR
let string1 = "Bro Code";
let letters = [...string1];
console.log(letters);






