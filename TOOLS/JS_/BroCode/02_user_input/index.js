// ACCEPT USER INPUT


// by window prompt
// let username;

// username = window.prompt("What is your username?");

// console.log(username)



// by HTML
let username;


document.getElementById("mySubmit").onclick = function () {
    username = document.getElementById("inp").value;
    document.getElementById("h1").textContent = `Welcome ${username}!`
}
