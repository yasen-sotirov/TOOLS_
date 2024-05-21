// ===  FOR LOOP  ===



//       брояч     до кога   брояч++
for (let rep = 1; rep <=10; rep++) {
    console.log(`Lifting weights repetition ${rep} 🏋️‍♂️ lift`);
}





// ОБХОЖДАНЕ НА STRING и ARRAY
const word = "ABCDEFGHI"

for (let i = 0; i < word.length; i++) console.log(word[i]); 



const birthYear = [1963, 1984, 1985, 1986]
const ages = []

for (i = birthYear.length -1; i >= 0; i--) {
    currentAges = 2024 - birthYear[i];
    ages.push(currentAges)
}
console.log(ages)




// CONTINUE и BREAK
let nums = [1, 2, 3, 'bug', 5, 6, 'dragon', 8, 9]
for (i=0; i<nums.length; i++) {
    if (nums[i] == 'bug') continue;
    if (nums[i] == 'dragon') break;
    console.log(nums[i]);
}



// FOR-OF LOOP
for (const el of word) console.log(el);



// ENTRIES == ENUMERATE    
const menu = ['a', 'b', 'c', 'd', 'e'];
for (const el of menu.entries()) console.log(el);


/////////////////////////////////////////////////////
// ===  WHILE

let dice;

while (dice !== 6) {
    console.log(`dice result ${dice}`)
    dice = Math.trunc(Math.random() * 6) +1;
}





var x = 0;

while (x < 5) {
    console.log(" X is currently: " + x);
    if (x===3) {
        console.log("X IS EQUAL TO THREE!")
    }
    console.log("x is still less than 5, adding 1 to x")
    x += 1; 
}



// var num = 2;

// while (num < 10) {
//     // if (num % 2 === 0) {
//         console.log(num)
//     // }
//     // num++   // добавя 1
//     num += 2;
// }



// DO WHILE LOOP - първо прави кода и после прави луупа
let uname;
do{uname = window.prompt('Enter your name')}
while (uname === "" || username === null)
console.log(`Hello ${username}!`)




let loggedIn = false;
let username;
let password;

while(!loggedIn) {
    username = window.prompt("Type username");
    password = window.prompt("Type password");

    if(username === "username" && password === "password"){
        loggedIn = true;
        alert("You are loged in")
    }
    else{
        alert("Invalid credentials! Try again")
    }
}


