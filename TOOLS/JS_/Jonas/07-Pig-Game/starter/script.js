'use strict';

// select total player score
// и двете правят едно и също
const player0El = document.querySelector('.player--0');
const score0el = document.querySelector('#score--0');
let current0El = document.getElementById('current--0');

const player1El = document.querySelector('.player--1');
const score1el = document.getElementById('score--1');
let current1El = document.getElementById('current--1');

const diceEl = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

// подаваме int, но JS автоматично конв. в str
score0el.textContent = 0;
score1el.textContent = 0;
diceEl.classList.add('.hidden');

const scores = [0, 0];
let currentScore = 0;
let activePlayer = 0;

const swithPlayer = function () {
  document.getElementById(`score--${activePlayer}`).textContent = 0;
  currentScore = 0;
  activePlayer = activePlayer === 0 ? 1 : 0;
  player0El.classList.toggle('player--active');
  player1El.classList.toggle('player--active');
};

// Functionality Rolling dice
btnRoll.addEventListener('click', function () {
  // random dice
  const diceRandom = Math.trunc(Math.random() * 6) + 1;

  // Display dice pic
  diceEl.classList.remove('.hidden');
  diceEl.src = `dice-${diceRandom}.png`;

  // check if result is 1
  if (diceRandom !== 1) {
    currentScore += diceRandom;
    document.getElementById(`current--${activePlayer}`).textContent =
      currentScore;
  } else {
    swithPlayer();
  }
});

btnHold.addEventListener('click', function () {
  scores[activePlayer] += currentScore;

  document.querySelector(`#score--${activePlayer}`).textContent =
    scores[activePlayer];

  swithPlayer();
});

// 79
