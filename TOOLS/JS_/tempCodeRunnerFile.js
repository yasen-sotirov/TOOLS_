/* IF */ 


// НА ЕДИН РЕД - изпълнява се при true
const age = 18;
if (age === 18) console.log(`You are adult!`)

if (age === 16) console.log(`You are not adult!`)   


// explicit return
const foo = () => {
  const baba = 'baba'
  return baba
}

// implicit return
const bar = () => age === 16 ? 'baba' : 'dedo'

// console.log(foo())
console.log(bar())