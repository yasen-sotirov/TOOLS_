let dice;

while (dice !== 6) {
    console.log(`dice result ${dice}`)
    dice = Math.trunc(Math.random() * 6) +1;
}

