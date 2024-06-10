// https://www.youtube.com/watch?v=G0jO8kUrg-I&list=PLjwm_8O3suyOgDS_Z8AWbbq3zpCmR-WE9&index=3

const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask() {
  if(inputBox.value === "") alert("You must write something");
  else{
    let li = document.createElement("li");
    li.innerHTML = inputBox.value;
    listContainer.appendChild(li);

    let span = document.createElement("span");
    span.innerHTML = "\u00d7";
    li.appendChild(span);
  }  
  inputBox.value = "";
  saveData()
};


listContainer.addEventListener("click", function(event) {
  if(event.target.tagName === "LI") {
    event.target.classList.toggle("checked");
    saveData();
  }
  else if(event.target.tagName === "SPAN") {
    event.target.parentElement.remove();
    saveData();
  }
}, false)


// SAVE STORAGE
function saveData() {
  localStorage.setItem("data", listContainer.innerHTML);
}

// GET SAVED DATA
function showTask(){
  listContainer.innerHTML = localStorage.getItem("data");
};
showTask();