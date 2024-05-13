// ARRAY
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


let array1 = ['one', 'two', 'three'];
let numArray = new Array(1, 2, 3, 4, 5);



// ДОБАВЯНЕ
array1 = ['one', 'two', 'three'];
console.log('преди: ', array1);

array1.push('four', 'five');        // добавя накрая
array1[12] = 'seven';               // добавя na индекс + празени слотове ако масива не е толкова пълен

array1.unshift('zero');             // добавя в началото
array1.shift('zero');               // добавя в началото
console.log('след: ', array1)




// EXPRESSION - изрази в масива
let firstName = "Stamat";
let age = 1986;
let numbesrs = new Array(1, 2, 3);
let description = new Array(firstName, 2024-age, numbesrs);
console.log(description)




// ПРЕМАХВАНЕ
array1 = ['one', 'two', 'three'];
console.log(array1)
console.log('подледен елемент: ', array1.pop());       // премахва последния и го пази
console.log('първи елемент: ', array1.shift());     // премахва първия елемент и го пази
console.log('в масива остана ', array1)




// ВРЪЩА ДЪЛЖИНАТА НА МАСИВА
array1 = ['one', 'two', 'three'];
console.log("дължина:", array1.length);




// ПОКАЗВА НА ИНДЕКС
array1 = ['one', 'two', 'three'];
console.log("елемент на индекс 1: ", array1[1]);
console.log("индекс на елемент 'three': ", array1.indexOf("three"));    // -1 ако го няма
console.log('елемент на последен индекс', array1[array1.length-1])



// ИМА ЛИ ГО В МАСИВА
array1 = ['one', 'two', 'three'];
console.log('има ли four: ', array1.includes('four'))



// ОБХОЖДАНЕ НА МАСИВ
// let array1 = ['one', 'two', 'three'];

console.log("обхождане 1");
for (let i = 0; i < array1.length; i++) {
    console.log(array1[i]);
};


console.log("обхождане 2");
for (let el of array1) {
    console.log(el);
};


console.log("oбратно обхождане");
for (let i = array1.length -1; i >= 0; i--) {
    console.log(array1[i]);
};





// СОРТИРАНЕ
console.log(array1.sort());
console.log(array1.sort().reverse());





// ОБРЪЩА РЕДА
console.log(array1.reverse());



// РАЗОПАКОВА - SPRED OPERATOR
let maximum = Math.max(...numArray);
console.log(maximum);



// ОБЕДИНЯВА ЕЛЕМЕНТИТЕ НА МАСИВА
let strArray = ['a', 'b', 'c', 'd'];
console.log(strArray.join());
console.log(strArray.join("-"));


// ...SPRED - REST PARAMETER

    // ОБЕДИНЯВА ДВА МАСИВА
    let combine = [...array1, ...strArray, "eggs"];
    console.log("обединява", combine);



    // ОБЕДИНЯВА В МАСИВ - ARGS
    const food1 = "eggs";
    const food2 = "meat";
    const food3 = "bread";
    const food4 = "ham";

    function makeSandwich(...args){
        console.log(args)
    }

    makeSandwich(food1, food2, food3, food4)


    // РАЗОПАКОВА
    let strArray2 = ['a', 'b', 'c', 'd', 'e'];
    console.log(...strArray2);