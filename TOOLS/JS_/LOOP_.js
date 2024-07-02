"FOR LOOP"

//       брояч     до кога   брояч++
// for (let rep = 1; rep <=10; rep++) {
//     console.log(`Lifting weights repetition ${rep} 🏋️‍♂️ lift`);
// }



"ОБХОЖДАНЕ НА МАСИВ"
// let array1 = ['one', 'two', 'three'];

// console.log("обхождане 1");
// for (let i = 0; i < array1.length; i++) {
// 	console.log(array1[i]);
// };




"FOR OF"
// console.log("обхождане 2");
// for (let el of array1) {
// 	console.log(el);
// };




"FOR EACH"   /* 
  - heigh order function
	- не поддържа continue и break					*/
// const movements = [10, -5, 20, -10, 20, -5];

// movements.forEach(function (move) {
//   if (move > 0) console.log(`you deposit ${move}`);
//   else console.log(`you withdraw ${Math.abs(move)}`);
// })

// movements.forEach(function (mov, i) {
//     if (mov > 0) console.log(` deposit ${i}: ${mov}`);
//     else console.log(`withdraw ${i}: ${Math.abs(mov)}`);
//   })
  





"REVERSED"
// console.log("обратно обхождане");
// for (let i = array1.length -1; i >= 0; i--) {
// 	console.log(array1[i]);
// };




"ОБХОЖДАНЕ НА STRING"
// const word = "ABCDEFGHI"
// for (let i = 0; i < word.length; i++) console.log(word[i]); 





"CONTINUE и BREAK"
// let nums = [1, 2, 3, 'bug', 5, 6, 'dragon', 8, 9]
// for (i=0; i<nums.length; i++) {
//     if (nums[i] == 'bug') continue;
//     if (nums[i] == 'dragon') break;
//     console.log(nums[i]);
// }




"ENTRIES == ENUMERATE    "
// const menu = ['a', 'b', 'c', 'd', 'e'];
// for (const [i, el] of menu.entries()) console.log(`idx ${i}: ${el}`);







"===  WHILE  ==="
// let dice;

// while (dice !== 6) {
//     console.log(`dice result ${dice}`)
//     dice = Math.trunc(Math.random() * 6) +1;
// }




// var x = 0;

// while (x < 5) {
//     console.log(" X is currently: " + x);
//     if (x===3) {
//         console.log("X IS EQUAL TO THREE!")
//     }
//     console.log("x is still less than 5, adding 1 to x")
//     x += 1; 
// }



// var num = 2;

// while (num < 10) {
//     // if (num % 2 === 0) {
//         console.log(num)
//     // }
//     // num++   // добавя 1
//     num += 2;
// }



"DO WHILE LOOP"        // първо прави кода и после прави луупа
// let uname;
// do{uname = window.prompt('Enter your name')}
// while (uname === "" || username === null)
// console.log(`Hello ${username}!`)




// let loggedIn = false;
// let username;
// let password;

// while(!loggedIn) {
//     username = window.prompt("Type username");
//     password = window.prompt("Type password");

//     if(username === "username" && password === "password"){
//         loggedIn = true;
//         alert("You are loged in")
//     }
//     else{
//         alert("Invalid credentials! Try again")
//     }
// }


