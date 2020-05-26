from fastapi import FastAPI
from pydantic import BaseModel

class painInfo(item):
    source: str
    painlevel: float

app = FastAPI()


@app.post("/img-upload")
async def read_root(info: painInfo):
    """ Some ML stuff """
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}