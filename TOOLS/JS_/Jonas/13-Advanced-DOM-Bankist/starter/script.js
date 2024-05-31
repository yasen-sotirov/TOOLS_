'use strict';

///////////////////////////////////////
// Modal window

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.btn--close-modal');
// отговаря за два бутона
const btnsOpenModal = document.querySelectorAll('.btn--show-modal'); 

const openModal = function (event) {
  event.preventDefault();    // спира pop-up a
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

// отваря modal прозореца, от два бутона
btnsOpenModal.forEach(btn => btn.addEventListener 
  ('click', openModal));


btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});
