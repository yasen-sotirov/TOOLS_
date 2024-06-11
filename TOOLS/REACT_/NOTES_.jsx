"REACT"; /* 
- библиотека - един инструмент, който създава user interfaces
- framework - сбор от инструменти за: routing, http, form validation, internationalization и др.
  казва ти кое и как да го ползваш;
- react не ти казва, кой инструмент да ползваш за тези неща и как
- използва virtual DOM, за да работи на една страница и да не презарежда
  - това позволява да се презареди само част от страницата  
  - return jsx <div>Hello</div>  реакт елемент, който показва как трябва да изглеждат нещата


"СТРУКТУРА"
  package.json - всички пакети
  src folder - цялата логика
  public folder - самата страница
  src/index.js  - 
   



https://www.youtube.com/watch?v=SqcY0GlETPk&ab_channel=ProgrammingwithMosh

npm create vite@4.1.0
project name: react_app

ts - за plain обикновени файлове
tsx -  за реакт компоненти

използва се PascalCasing - всяка дума е с главна буква



"СЪЗДАВАНЕ НА РЕАКТ КОМПОНЕНТИ"
  'чрез js класове или функции'
  'function-based components - по-популярни днес'


"BOOTSTRAP"
- npm i bootstrap@5.2.3
- трием всичко от app.css - те с от vite - не ми трябват вече
- трия файла main.css
- в main.css import 'bootstrap/dist/css/bootstrap.css' 

"COMPONENTS"
- създаваме папка където събирам всичко компоненти
- един компонент връща само един <tag>, затова обгръщаме с:
  - тагове <div>
  - fragment import { Fragment } from "react/jsx-runtime";
  - <> </>

"LOOP"
- в jsx няма loops, затова използваме map


mu.tate     - change
mu.ta.ble   - changeable
im.mu.table - unchangeable


PROPS
- input passed to component
- similar to function args
- immutable


STATE
- data managed by a component
- similar to local variables
- mutable -променят се
 */

"PORTFOLIO REACT APP";

"СЪЗДАВАНЕ НА АПП"; /* https://www.youtube.com/watch?v=hYv6BM2fWd8&ab_channel=webdecoded
npx create-react-app ./         // в същата директория
npm i react-bootstrap bootstrap
npm start



*/

"PROPS КОМПОНЕНТ В КОМПОНЕНТ";
// const Person = (props) => {
//   return (
//     <>
//       <h1>Name: {props.name}</h1>
//       <h2>Last name: {props.lastName}</h2>
//       <h2>age: 30</h2>
//     </>
//   );
// };

// const App = () => {
//   return (
//     <div className="App">
//       <Person name="Ivan" lastName={"Todorov"} />
//       <Person name="Yasen" lastName={"Sotirov"} />
//       <Person name="Toshko" lastName={"Petrov"} />
//     </div>
//   );
// };

"HOOK STATE";
// import { useState, useEffect } from "react"; // Hook

// const App = () => {
//   // елемент setElement
//   const [counter, setCounter] = useState(0);

//   //                какво се случва  кога се случва
//   useEffect(() => {
//     setCounter(100);
//   }, []);

//   return (
//     <div className="App">
//       <button onClick={() => setCounter((prevCounter) => prevCounter + 1)}>
//         +
//       </button>
//       <h1>{counter}</h1>
//       <button onClick={() => setCounter((prevCounter) => prevCounter - 1)}>
//         -
//       </button>
//     </div>
//   );
// };

"SRC FOLDER"; /*
  index.js
    import React from "react";
    import ReactDOM from "react-dom";
    import App from "./App";

    // вкарва App в root
    ReactDOM.render(<App />, document.getElementById("root"));


  App.js
    import React from "react";

    // main functional component
    const App = () => {
      return <h1>App</h1>;
    };

    export default App;


 */
