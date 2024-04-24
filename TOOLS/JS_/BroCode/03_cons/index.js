// CONST = A VARIABLE THAT CAN'T BE CHANGED

const PI = 3.1415;
let radius;
let circumference;

// radius = Number(window.prompt(`Enter the radius of a circle:`));

document.getElementById("button").onclick = function() {
    radius = document.getElementById("inp").value;
    radius = Number(radius);
    circumference = 2 * PI * radius;
    document.getElementById("h3").textContent = circumference + "cm";
}

