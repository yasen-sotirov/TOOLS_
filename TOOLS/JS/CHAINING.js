
let username = window.prompt("Enter your username:");

// ---- NO CHAINING

// username = username.trim();     // маха white spaces
// let firstLetter =  username.charAt(0);
// firstLetter = firstLetter.toUpperCase();

// let restChars = username.slice(1);
// restChars = restChars.toLocaleLowerCase();

// console.log(firstLetter + restChars);



// ---- CHAINING METHOD

username = username.trim().charAt(0).toUpperCase() + username.trim().slice(1).toLowerCase();

console.log(username);