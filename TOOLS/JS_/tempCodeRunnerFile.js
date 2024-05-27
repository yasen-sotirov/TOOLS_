const movements = [10, 20, 30, 40, 50];

// const balance = movements.reduce((acc, current, i, array) => acc + current, 0)
// console.log(`result: ${balance}`);

const max = movements.reduce((acc, curr) => {
  if (acc > curr) return acc;
  else return curr;
}, movements[0]);
console.log(max);
