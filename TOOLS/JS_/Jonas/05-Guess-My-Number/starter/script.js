'use strict';

const secretNum = Math.trunc(Math.random() * 100) + 1;
let score = 10;

// check number of guesses function
function checkScore() {
  document.querySelector('.message').textContent = '💥 You lost!';
  document.querySelector('.score').textContent = 0;
}

// game logic
document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);

  // where there is no input
  if (!guess) {
    document.querySelector('.message').textContent = '❌ No number';
  }

  // when player win
  else if (guess === secretNum) {
    document.querySelector('.message').textContent = '🎉 Correct Number!';
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';
    document.querySelector('.number').textContent = secretNum;
  }

  // when guess is too high
  else if (guess > secretNum) {
    if (score > 1) {
      document.querySelector('.message').textContent = '🔼 Too high!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      checkScore();
    }
  }

  // when guess is too low
  else if (guess < secretNum) {
    if (score > 1) {
      document.querySelector('.message').textContent = '🔽 Too low!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      checkScore();
    }
  }
});
