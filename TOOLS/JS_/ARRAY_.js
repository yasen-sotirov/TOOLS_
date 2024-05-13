// ARRAY
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


let array1 = ['one', 'two', 'three'];
let numArray = new Array(1, 2, 3, 4, 5);



// ДОБАВЯНЕ
array1.push('four', 'five');    // добавя накрая
array1[6] = 'seven';            // добавя накрая + празен слот
array1.unshift('zero');         // добавя в началото




// ПРЕМАХВАНЕ
console.log(array1.pop());       // премахва последния и го пази
array1.shift();                  // премахва първия елемент



// ВРЪЩА ДЪЛЖИНАТА НА МАСИВА
console.log("дължина:", array1.length);



// ПОКАЗВА НА ИНДЕКС
console.log("елемент на индекс 1:", array1[1]);
console.log("индекс на елемент 'three':", array1.indexOf("three"));




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