

const decreaceBtn = document.getElementById("decriceID");
const resetBtn = document.getElementById("resetID");
const increaceBtn = document.getElementById("incriceID");
const countLabel = document.getElementById("countLabel");

let count = 0;


increaceBtn.onclick = function() {
    count++;
    countLabel.textContent = count;
}


decreaceBtn.onclick = function() {
    count--;
    countLabel.textContent = count;
}


resetBtn.onclick = function() {
    count = 0;
    countLabel.textContent = count;
}