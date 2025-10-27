from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    return {"item_id": item_id, "q": q}

