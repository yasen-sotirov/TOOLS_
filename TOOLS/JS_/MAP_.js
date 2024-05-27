/* MAP  
  - връзва стойности към ключове;
  - данните се съхраняват в key-value pairs;
  - ключът може да бъде от всякакъв тип (при обектите винаги е str); 
  - итерабъл       */


"СЪЗДАВАНЕ"     // пълни се с вложен списък / матрица
// const rest = new Map([
//   ['name', 'Classico Italiano'], 
//   [1, 'Sofia'],
//   [2, 'Plovdiv'],
// ]);



"ПЪЛНЕНЕ СЪС СТОЙНОСТИ + CHAINING"
// rest
//   .set(true, 'we are open')
//   .set(false, 'we are closed')
//   .set('open', 11)
//   .set('closed', 23);

// console.log(rest);





"ИЗВИКВАНЕ ПО КЛЮЧ"
// console.log(rest.get('name'));

// const time = 21;
// //                   21          open=>11        21       closed=>23
// console.log(rest.get(time > rest.get('open') && time < rest.get('closed')));




"ДОСТЪПВАНЕ НА ВСИЧКИ КЛЮЧОВЕ, СТОЙНОСТИ"
// console.log('entries', rest.entries());
// console.log('keys', rest.keys());
// console.log('values', rest.values());
// console.log('values in array', [...rest.values()]);



"FOR EACH"
// const currencies = new Map([
//   ['USD', 'United States dollar'],
//   ['EUR', 'Euro'],
//   ['GBP', 'Pound sterling'],
// ]);

// currencies.forEach(function(value, key, map) {
//   console.log(`${key}: ${value}`);
// })



"ИЗТРИВАНЕ ПО КЛЮЧ"
// rest.delete(2)



"ИМА ЛИ ГО В МАП-А"
// console.log('има ли го', rest.has(2));



"РАЗМЕР"
// console.log(rest.size);



"ИТЕРИРАНЕ ПРЕЗ МАП"
// const quiz = new Map([
//   ['question', 'What is the best programming language in the world? C / Java / JavaScript'],
//   [1, 'C'],
//   [2, 'Java'],
//   [3, 'JavaScript'],
//   ['correct', 3],
//   [true, 'Correct 🎉'],
//   [false, 'Try again!'],
// ]);

// console.log(quiz.get('question'));
// for (const [key, value] of quiz) {
//   if (typeof key === 'number') console.log(`Answer ${key} : ${value}`);
// };
// const answer = Number(prompt('Your answer'))
// console.log(quiz.get(quiz.get('correct') === answer));




"ОТ MAP В ARRAY"
// console.log([...quiz]);



"ИЗПРАЗВАНЕ НА КОЛЕКЦИЯТА"
// console.log('има ли нещо в обекта:', rest.clear());
