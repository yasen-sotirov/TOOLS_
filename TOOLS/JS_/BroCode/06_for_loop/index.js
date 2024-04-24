

const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("resultElement");
let age;

mySubmit.onclick = function() {

    age = Number(myText.value);

    if(age >= 100){
        resultElement.textContent = `You are too old`;
    }

    else if(age == 0){
        resultElement.textContent = `You were just born`;
    }

    else if(age >= 18){
        resultElement.textContent = `You can ente`;
    }

    else if(age < 0){
        resultElement.textContent = `Negative value`;
    }

    else{
        resultElement.textContent = `You must be 18+`;
    }
};