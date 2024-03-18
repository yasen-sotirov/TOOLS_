from fastapi import FastAPI
import uvicorn


app = FastAPI(title="FastAPI Exercise",
              description="https://www.youtube.com/watch?v=_AFwFvGnEpY&list=PLzigVHkYNcYHce76stBQeqBhj-hu8pJ2Z&index=3&ab_channel=MukulMantosh"
              )
            # docs_url=None - скрива от външния свят


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
