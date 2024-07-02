"DOM"     /* Document Object Model (много комплексен API)
  - чрез него JS достъпва и променя всички HTML елементи и атрибути, и CSS стилове в страницата
  - интерфейс между js и html
  - съдържа множество елементи и методи за манипулация
  - има различни типове nodes: html elements и text

ОРГАНИЗАЦИЯ DOM API
  - всеки note в DOM tree е от тип Node
  - всеки node е представен в JS като object
  - този обект има достъп до методите и property на node
  - node имат 'детски' различни детски типове
  - детските типове се отнасят за всеки html елемент

НАСЛЕДЯВАНЕ
  - всички деца типове наследяват методите и пропъртитата на родителските типове  

- DOM дървото се създава от браузъра при стартиране
- пълна репрезентация на html документа - съдържа всичките му елементи
- DOM и неговите методи са част от web APIs

- document e началната точка на дървото.
  за да селектираме елемент започваме с document.едикаквоси


https://www.w3schools.com/js/js_htmldom.asp */
const body = document.body;


"СЕЛЕКТИРАНЕ НА HTML ЕЛЕМЕНТИ"             // хваща:
// console.log(document.documentElement);    // целия html
// console.log(document.head);               
// console.log(document.body);
// console.log(document.URL);
// console.log(document.links);

// console.log(document.querySelector('.header'));
// console.log(document.querySelectorAll('.header'));  // връща node лист със всички елементи 

'връща live htmlCollection'     // автоматично се обновява при промяна
// console.log(document.getElementsByTagName('button'));
// console.log(document.getElementBysClassName('className'));
// document.getElementsById('elementId');


"ВМЪКВАНЕ НА ЕЛЕМЕНТИ"
// .insertAdjacentHTML    // ot bankist




"СЪЗДАВАНЕ НА ЕЛЕМЕНТИ"
// const message = document.createElement('div');    // създава контейнер
// message.classList.add('cookies-message');         // не знам какво прави
// message.innerHTML = 'We use cookies. <button class="btn">Got it!</button>';   // html елемент 


// body.prepend(message);                // закача в началото                       // закача ел в началото на бодито
// body.append(message)                  // закача накрая
// body.append(message.cloneNode(true))  // клонира и закача накрая
                             
// body.before(message)                  // преди и след елемент
// body.after(message)

// const header = document.querySelector('.header');
// header.remove();                      // трие елемент




"СЪЗДАВАНЕ НА СТИЛОВЕ"      // създава ги inline в html-а
// const message = document.createElement('div');    // създава контейнер
// message.classList.add('cookies-message');         // не знам какво прави
// message.innerHTML = 'We use cookies. <button class="btn">Got it!</button>';   // html елемент 
// body.after(message)

// message.style.backgroundColor = '#999';           // задава стил
// message.style.fontSize = '25px';

// console.log(getComputedStyle(message).backgroundColor);

// message.style.height = 
//   Number.parseFloat(getComputedStyle(message).height, 10) + 30 + 'px';




"ПРОМЯНА НА CSS ФАЙЛА"
// document.documentElement.style.setProperty('--color-primary', 'red');




"ДОСТЪПВАНЕ НА HTML АТРИБУТИ"
// const fav = document.querySelector('.favicon');
// console.log(fav.className);
// console.log(fav.href);                   // релативен път
// console.log(fav.getAttribute('href'));   // абсолютен път
// fav.href = 'https://media.istockphoto.com/id/1197784083/vector/pizza-slice-food-icon-logo.jpg?s=612x612&w=0&k=20&c=nz3TrQPpw-1LmcKogWsuPnAJYAcQyIrIpYFtLXNGKTc=';




"СЪЗДАВАНЕ НА АТРИБУТИ"                       // несвойствени за html-a
// body.setAttribute("designer", 'Yaskata');     
// console.log("дизайнер:", body.getAttribute('designer'));




"DATA ATTRIBUTES"   // специални атрибути започващи с data-
console.log(body.dataset.versionNumber);



"КЛАСОВЕ"
body.classList.add('cc', 'bb');
body.classList.remove('bb')
console.log(body.classList.contains('bb'));
console.log(body.classList.toggle('cc'));
console.log(body.classList.contains('cc'));













// // ДОСТЪПВАНЕ НА ЕЛЕМЕНТИ

// let p = document.querySelector('p');        // 'a' 'h' 
// p.textContent = "F12";                 // променя съдържанието
// p.innerHTML = '<strong>f12</strong>'   // достъпва html-a


 
// // ДОСТЪПВАНЕ НА АТРИБУТИ
// // let linkName = document.querySelector('a');
// // let linkAtt = linkName.getAttribute('href');          // в случая: "https://www.google.com/"
// // console.log(linkName);
// // console.log(linkAtt);

// // linkAtt.setAttribute('href', 'https://www.abv.bg/');
// // linkName.textContent('abv.bg');
// // console.log(linkAtt)
// // console.log(linkName)



// // EVENT LISTENER
// // https://www.w3schools.com/jsref/event_onmouseover.asp
// let headOne = document.querySelector('#one');

// headOne.addEventListener('mouseover', function(){
//     headOne.textContent = 'Mouse over me!';
//     headOne.style.color = 'red';
// });

// headOne.addEventListener('mouseout', function(){
//     headOne.textContent = 'HOVER ME!';
//     headOne.style.color = 'black';
// });



// //  хваща елемент      с класс  слуша когато прави   клик    изпълнява това
// document.querySelector('.check').addEventListener('click', function () {
//   console.log(document.querySelector('.guess').value);
// });




// // MODAL    Jonas: 06-Modal
// const modal = document.querySelector('.modal');
// const overlay = document.querySelector('.overlay');
// const btnCloseModal = document.querySelector('.close-modal');
// const btnOpenModal = document.querySelectorAll('.show-modal');



// // functions
// const closeModal = function () {
//   modal.classList.add('hidden');
//   overlay.classList.add('hidden');
// };

// const openModal = function () {
//   // премахване на CSS класове
//   // точка се ползва само при селекторите
//   modal.classList.remove('hidden');
//   // открива блъра
//   overlay.classList.remove('hidden');

//   // close button
//   btnCloseModal.addEventListener('click', closeModal);
// };

// // logic
// for (let i = 0; i < btnOpenModal.length; i++) {
//   btnOpenModal[i].addEventListener('click', openModal);
// }
// overlay.addEventListener('click', closeModal);

// // event - дава достъп до данните на event listener-a
// document.addEventListener('keydown', function (event) {
//   console.log(event.key);
//   if (event.key === 'Escape' && !modal.classList.contains('hidden'))
//     closeModal();
// });
