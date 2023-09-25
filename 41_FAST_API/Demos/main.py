import uvicorn
from fastapi import FastAPI
from data import Product, data


app = FastAPI()     # инстанция на Fastapi - за да ползваме наготово

# 127.0.0.1:8000 /

@app.get('/')       # end point които ползваме наготово, za da namapnem един урл адрес
def root():
    return {
        'description': 'Product API',
        'routes': [
            ('GET', '/products', 'List of products')
        ]
    }


@app.get('/products')
def get_products():
    return data


@app.post('/products')
def create_products(p: Product):
    max_id = max(p.id for p in data)
    p_id = max_id + 1
    data.append(p)

    return p

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
# пускане на сървър: uvicorn main:app --reload      - вдига сървъра



# pip list - показва инсталираните пкети
# postman - софтуер за разработка на бекедн приложения: тестване на заявки