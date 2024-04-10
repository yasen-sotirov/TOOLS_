// var x = 0;

// while (x < 5) {
//     console.log(" X is currently: " + x);
//     if (x===3) {
//         console.log("X IS EQUAL TO THREE!")
//     }
//     console.log("x is still less than 5, adding 1 to x")
//     x += 1; 
// }



// var num = 2;

// while (num < 10) {
//     // if (num % 2 === 0) {
//         console.log(num)
//     // }
//     // num++   // добавя 1
//     num += 2;
// }



// DO WHILE LOOP - първо прави кода и после прави луупа
// let username;
// do{username = window.prompt('Enter your name')}
// while (username === "" || username === null)
// console.log(`Hello ${username}!`)




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


