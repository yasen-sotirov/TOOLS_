// NUMBER GUESSING GAME

const min = 1;
const max = 100;
const answer = Math.floor(Math.random()*(max-min+1)) +min;

let attempts = 0;
let guess;
let running = true;

while(running){
    guess = Number(window.prompt("Guess a number in range 1-100"));
    
    if(isNaN(guess)){
        window.alert("Pleace type a valid nubmer");
    }
    else if(guess < min || guess > max){
        window.alert("Pleace enter number in range 1-100");
    }
    else{
        attempts++;
        if(guess < answer){
            window.alert("Too low! Try again.");
        }
        else if (guess > answer){
            window.alert("Too high! Try again.");
        }
        else{
            window.alert(`Correct! The answer is ${answer}. It took you ${attempts} attempts.`)
            running = false
        }
    }

};
