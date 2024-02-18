" API ПО ПРИНЦИПИТЕ НА REST"   #

'''
Пример на API, създадено в съответствие с принципите на REST 
Има следните функционалности:

    POST /items/: Създава нов артикул в инвентара.
    GET /items/: Връща списък с артикулите в инвентара.
    GET /items/{item_id}: Връща детайли за определен артикул по ID.
    PUT /items/{item_id}: Обновява детайлите на артикул по ID.
    DELETE /items/{item_id}: Изтрива артикул от инвентара по ID.
    
REST е архитектурен стил за разработка на системи за обмен на данни, 
който се базира на следните принципи:
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

inventory = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    inventory.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10):
    return inventory[skip : skip + limit]

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(inventory):
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(inventory):
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item
    return item

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(inventory):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = inventory.pop(item_id)
    return deleted_item
