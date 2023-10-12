from fastapi import FastAPI
import uvicorn
from routers_ctrl.product_rut import product_router
from routers_ctrl.categories_rut import category_router



app = FastAPI(title="From scratch")

app.include_router(product_router)
app.include_router(category_router)





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


"""
** ДЕЙСТВИЕ **
    main
        - зарежда FastAPI
        - зарежда routers
    routers
        - приема endpoint
        - проверява за логика на endpoint       
    services
        - открива логиката и изпраща заявка в питонски код        
    database
        - установява връзка с базата данни
        - отваря курсор
        - изпраща заявката към БД
        - връща резултата към питащия -> services        
    services
        - парсва получения лист към обект от клас
        - връща резултата към питащия -> router        
    router
        - праща резултата като json към клиента

    
    
    
** СЪЗДАВАНЕ **

1. в Models се създава обекта (class) - продукт, категория, поръчка ...
2. 


създава се файл папка router
    импорти:
        from fastapi import APIRouter
        from pydantic import  BaseModel
        from database_mod.models_project_el import Category
        from services_mod_fn import product_srv_fn
        
    префикс за съкратено писане:
        product_router = APIRouter(prefix='/products')
        
    създаване на endpoint (router)
        той работи с логика записана като функция в services
        тази логика ползва функция която се връзва с базата данни
        и връща необходимото инфо
        което се парсва като инстанция на клас

създава се router с endpoint 






"""






