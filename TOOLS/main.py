from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def view():
    a = 'a'
    b = 'b' + a
    return {'Hello': b}

if __name__ == "__main__":
    uvicorn.run("main:app", host = '127.0.0.1', port=8000)
