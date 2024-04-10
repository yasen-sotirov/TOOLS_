// HOISTING - извикване на функцията преди да е декларирана

one()
two()
three()

function one(){
    let one = 1;
    console.log(one)
}

function two(){
    let two = 2;
    console.log(two)
}

function three(){
    let three = 3;
    console.log(three)
}




// ...SPRED - REST PARAMETER  (args)
const food1 = "eggs";
const food2 = "meat";
const food3 = "bread";
const food4 = "ham";

function makeSandwich(...args){
    console.log(args)
};

makeSandwich(food1, food2, food3, food4);


// пример 2
function sumNums(...numbers){
    let result = 0;
    for(let num of numbers){
        result += num;
    }
    return result;
}

const totalSum = sumNums(1, 2, 3, 4, 5, 6, 7, 8, 9)

console.log(`The total is: ${totalSum}`);