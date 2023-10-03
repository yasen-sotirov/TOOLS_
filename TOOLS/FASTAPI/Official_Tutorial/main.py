from fastapi import FastAPI
from enum import Enum


app = FastAPI(title="Official Tutorial", description="https://fastapi.tiangolo.com/tutorial/path-params/")

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



@app.get("/items/{item_id}")
async def read_items(item_id):
    return {"item_id": item_id}

@app.get("/user/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


"ENUM"
@app.get("models/{model_name}")
def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


"QUERY"

