function Message() {
  // JSX: това е JavaScript XML код който ще се компилира до JavaScript 
  const name = 'Yaskata';
  return <h1>Hello {name}</h1>
}

// за да се ползва трябва да се експортне като обикновен компонент
export default Message;