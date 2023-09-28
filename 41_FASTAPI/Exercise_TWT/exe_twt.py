from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel  # създава Class


# СТАРТИРАНЕ НА СЪРВЪРА OT КОНЗОЛАТА - така reload-a работи
    # C:\ ... \demo_folder>uvicorn <file_name>:app --reload

app = FastAPI(title="Tech with Tim", description="https://www.youtube.com/watch?v=-ykeT6kk4bk&t=1s&ab_channel=TechWithTim")

class Item(BaseModel):
    name: str
    price: int
    brand: Optional[str] = None

inventory = {}


@app.get("/")    # дефинираме руута
def home():
    # всеки endpoint връща dict, който се превръща в JSON
    return {"Data": "test result ???"}


@app.get("/about")
def about():
    return {"Data": "About section"}


@app.get("/get_items/{id}")
# включва описание към заявката
def get_items(id: int = Path(description="The ID you like to view", gt=0)):
    return inventory[id]



@app.get("/all_items")
# включва описание към заявката
def get_items():
    return inventory



"ТЪРСЕНЕ ПО QUERY ПАРАМЕТЪР"
# ако не е описано какво търсим (примерно {id}), по подразбиране търси query
# 127.0.0.1:8000/get_by_name?name=Milk

@app.get("/get_by_name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"data": "Not found"}



# не изисква допълнително описване
@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item exist"}
    inventory[item_id] = item
    return inventory[item_id]



















# # ====================
# @app.get("/products/names")
# def get_product_names():
#     names = [p.names for p in inventory.items()]
#     return names
#
# @app.get('/products/average_price')
# def get_avg_price():
#     avg_price = sum([p.price for p in inventory] / len(inventory))
#     return avg_price