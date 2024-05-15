/* HTML DOM (Document Object Model
чрез него JS достъпва и променя всички HTML 
елементи и атрибути, и CSS стилове в страницата

- DOM дървото се създава от браузъра при стартиране
- пълна репрезентация на html документа - съдържа всичките му елементи
- DOM и неговите методи са част от web APIs

- document e началната точка на дървото.
  за да селектираме елемент започваме с document.едикаквоси


https://www.w3schools.com/js/js_htmldom.asp */



/* ДОСТЪПВАНЕ НА ЕЛЕМЕНТИ - хваща всичко от:

document.URL
document.body
document.head
document.links

document.getElementById();
document.getElementByName();
document.getElementByTagName();
document.getElementByClassName();   */



// ПРИХВАЩА КАТО CSS - прихваща първия елемент както css
document.querySelector('#id1');
document.querySelectorAll('.class1');    

myHeader = document.querySelector('h1');       
myHeader.style.color = 'red';



// ДОСТЪПВАНЕ НА ЕЛЕМЕНТИ
//селектирай елемент    с класс   от него вземи     и го направи на
document.querySelector('.message').textContent = 'Correct Number! 🎉';



let p = document.querySelector('p');        // 'a' 'h' 
p.textContent = "F12";                 // променя съдържанието
p.innerHTML = '<strong>f12</strong>'   // достъпва html-a


 
// ДОСТЪПВАНЕ НА АТРИБУТИ
// let linkName = document.querySelector('a');
// let linkAtt = linkName.getAttribute('href');          // в случая: "https://www.google.com/"
// console.log(linkName);
// console.log(linkAtt);

// linkAtt.setAttribute('href', 'https://www.abv.bg/');
// linkName.textContent('abv.bg');
// console.log(linkAtt)
// console.log(linkName)



// EVENT LISTENER
// https://www.w3schools.com/jsref/event_onmouseover.asp
let headOne = document.querySelector('#one');

headOne.addEventListener('mouseover', function(){
    headOne.textContent = 'Mouse over me!';
    headOne.style.color = 'red';
});

headOne.addEventListener('mouseout', function(){
    headOne.textContent = 'HOVER ME!';
    headOne.style.color = 'black';
});



//  хваща елемент      с класс  слуша когато прави   клик    изпълнява това
document.querySelector('.check').addEventListener('click', function () {
  console.log(document.querySelector('.guess').value);
});