let firstName = prompt("Enter first name:");
let lastName = prompt("Enter last name");
let age = prompt("How old are you");
let hight = prompt("Gow height are you");
let petName = prompt("What is your pet name");
alert("Thank you!")


let nameCond;
let ageCond;
let heightCond;
let petCond;


// NAME CONDITION
if (firstName[0] === lastName[0]) {
    nameCond = true;
} else {
    nameCond = false;
}


// AGE CONDITION
if (age > 20 && age < 30) {
    ageCond = true;
} else {
    ageCond = false;
}


// HEIGHT CONDITON
if (heightCond >= 170) {
    heightCond = true;
} else {
    heightCond = false;
}


// PET NAME
if (petName[petName.length -1] === "y") {
    petCond = true;
} else{
    petCond = false;
}


//ALL CONDITIONS
if (nameCond && ageCond && heightCond && petCond) {
    console.log("Welcome spy!")
} else {
    console.log("Nothing to show here")
}