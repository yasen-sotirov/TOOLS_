const workHours = {
  mon: {
    open: 9,
    close: 18,
  },
  wed: {
    open: 9,
    close: 18,
  },
}; 

const office = {
  location: 'Sofia',
  workers: 20,
  workHours,        // преди ЕS6:  workHours: workHours,
  callBack(time) {console.log(`Calling you at ${time}`);},
}
// console.log(office);




// OPTIONAL CHAINING    ще продължи по веригата ако tue го има
    // проверява за property 
    console.log(office.workHours.tue?.open);

    const days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
    for (const day of days) {
      const open = office.workHours[day]?.open;
      console.log(`On ${day} we open at ${open ?? 'not work'}.`);
    }

    // проверява за методи
    console.log(office.callBack('12:30'));
    console.log(office.check?.('check') ?? 'Method does not exist');



// ДОСТЪПВАНЕ на KEYS, VALUES, ENTRIES
// console.log(Object.keys(workHours));
 
// console.log( Object.values(workHours));
  
const entries = Object.entries(workHours);
for (const [key, {open, close}] of entries) {
  console.log(`On ${key} we open at ${open} and close at ${close}`);
};
