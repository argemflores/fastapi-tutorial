"""Imports"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root

    Returns:
        json: Response
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    """Read item

    Args:
        item_id (str): Item ID

    Returns:
        json: Response
    """
    return {"item_id": item_id}
