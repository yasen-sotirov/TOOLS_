// трием всичко от файла и започвам отначало
import ListGroup from "./components/ListGroup";

function App() {
  let items = ["Sofia", "Plovdiv", "Varna", "Burgas", "Veliko Tarnovo"];

  const handleSelectItem = (items: string) => console.log(items);

  return (
    <div>
      <ListGroup
        items={items}
        heading="Cities"
        onSelectItem={handleSelectItem}
      />
    </div>
  );
}

export default App;
