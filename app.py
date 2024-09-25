from fastapi import FastAPI
from router import weather
app = FastAPI()


app.include_router(weather.router)
@app.get("/",tags=["home"])
def read_root():
    return {"message": "Hello, World!"}