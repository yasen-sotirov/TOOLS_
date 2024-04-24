// restart game button
let restart = document.querySelector('#b');

//grads all the squares
let squares = document.querySelectorAll('td');

// clear all the squares
function clearBoard() {
    for (let i=0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}

restart.addEventListener('click', clearBoard);



// check square markers

// ВАРИАНТ 1
// var cellOne = document.querySelector('#one')
// 
// cellOne.addEventListener('click', function() {
//     if (cellOne.textContent === '') {
//         cellOne.textContent = 'X';
//     }
//     else if (cellOne.textContent === 'X') {
//         cellOne.textContent = 'O';
//     }
//     else  {
//         cellOne.textContent = '';}
// })


// ВАРИАНТ 2 - THIS
function changeMarker() {
    if (this.textContent === ''){
        this.textContent = 'X';
    }
    else if (this.textContent === 'X'){
        this.textContent = 'O';
    }
    else {
        this.textContent = '';
    }
}


for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker)
}




// forloop to add event listener0