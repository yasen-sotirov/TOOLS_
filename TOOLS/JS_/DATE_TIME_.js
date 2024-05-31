"DATE"    /*
  - "2024-05-29T10:37:02.766Z" - стандарт за време. По гринуич, без лятната добавка
  - връща времето по гринуич т.е -3ч    */

// console.log(new Date());    // now

// console.log(new Date('Aug 02 2024 20:44:22'));   // този метод не винаги връща коректни резултати
//                   год  мес ден ч  мин сек
// console.log(new Date(2024, 0, 5, 15, 30, 10));    // месеците започват от 0
// console.log(new Date(2024, 0, 35));               // конвертира деня 


"СЕГА"
// console.log(new Date());    // датата и времето сега, по гринуич
// console.log(Date.now());    // time stamp на сега. Мили сек от 1970г



"ИЗВАЖДАНЕ НА ЕЛЕМЕНТИ ОТ ДАТА"
// const future = new Date(2037, 0, 21, 12, 55);
// console.log('година: ', future.getFullYear());
// console.log('месец: ', future.getMonth());           // 0 == януари
// console.log('ден: ', future.getDate());              // номер на деня       
// console.log('ден от седмицата', future.getDay());    // 3 == сряда
// console.log(future.toISOString());                   // връща времето в ISO стандарт
// console.log(future.getTime());                       // връща timestamp на времето в мили сек, спрямо 1970г 



"ПРОМЯНА НА ЕЛЕМЕНТИ ОТ ДАТА"
// const now = new Date(2024, 4, 29);
// now.setFullYear(2025);
// now.setMonth(8);
// console.log(now);



"КОНВЕРТИРАНЕ ОТ ДНИ В МИЛИ СЕКУНДИ"
// const days = 3;
// console.log(new Date(3 * 24 * 60 * 60 * 1000));



"ФОРМАТИРАНЕ ДАТА"
// const now = new Date();
// const day = `${now.getDate()}`.padStart(2, 0);      // ще добави 0 докато станат общо 2 знака
// const month = `${now.getMonth()}`.padStart(2, 0);
// const year = now.getFullYear();

// console.log(`${day}.${month}.${year}г.`);



"ИЗВАЖДАНЕ НА ДНИ"
// const calcDaysPassed = (date1, date2) => Math.round((date2 - date1) / (1000 * 60 * 60 * 24));
// const days1 = calcDaysPassed(new Date(2024, 0, 1), new Date(2024, 3, 10));
// console.log(days1);



"МЕЖДУНАРОДНО ФОРМАТИРАНЕ"    // кодове: http://www.lingoes.net/en/translator/langcode.htm
// console.log(new Intl.DateTimeFormat('bg').format(new Date()));
// console.log(new Intl.DateTimeFormat('en-GB').format(new Date()));

'options'
// const options = {
//   hour: 'numeric',
//   minute: 'numeric',
//   day: 'numeric',
//   month: 'long',      // 2-digit
//   year: 'numeric',
//   weekday: 'long'     // short
// };
// console.log(new Intl.DateTimeFormat('bg', options).format(new Date()));



"ТАЙМЕР"   // работи асинхронно, изпълнява действие след определено време
// const ingredients = ['olives', 'mozzarella']
// setTimeout((ing1, ing2) => console.log(`Here is your pizza with ${ing1} and ${ing2} 🍕`), 
//   3000, ...ingredients);


"ИНТЕРВАЛ"  // изпълнява действие през определено време
// setInterval(function () {
//   const now = new Date();
//   console.log(now);
// }, 2000)



"СПИРАНЕ НА ТАЙМЕРА"
// clearTimeout()