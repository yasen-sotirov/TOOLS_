

const myCheckbox = document.getElementById("myCheckbox");
const visaBtn = document.getElementById("visaBtn");
const masterBtn = document.getElementById("masterBtn");
const payPalBtn = document.getElementById("payPalBtn");
const mySubmit = document.getElementById("mySubmit");
const subResult = document.getElementById("subResult");
const paymentResult = document.getElementById("paymentResult");


mySubmit.onclick = function() {
    if (myCheckbox.checked) {
        subResult.textContent = `You are subscribed!`;
    }
    else{
        subResult.textContent = `You are NOT subscribed!`
    }

    if(visaBtn.checked){
        paymentResult.textContent = `You are paying with Visa`
    }

    else if(masterBtn.checked){
        paymentResult.textContent = `You are paying with Marter card`
    }

    else if(payPalBtn.checked){
        paymentResult.textContent = `You are paying with PayPal`
    }

    else {
        paymentResult.textContent = `You must select payment type`
    }
}