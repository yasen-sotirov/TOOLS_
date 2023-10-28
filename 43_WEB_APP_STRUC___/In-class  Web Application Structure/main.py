from fastapi import FastAPI, Response
from routers.product import product_router
from routers.categories import categories_router
from routers.orders_ro import order_router
import uvicorn

app = FastAPI()
app.include_router(product_router)
app.include_router(categories_router)
app.include_router(order_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)