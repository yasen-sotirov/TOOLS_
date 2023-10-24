from fastapi import FastAPI
from data.database import init_database
from routers.profiles_ro import profiles_router
from routers.product_ro import products_router
from routers.categories_ro import categories_router

import uvicorn


init_database()



app = FastAPI()
app.include_router(profiles_router)
app.include_router(products_router)
app.include_router(categories_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
