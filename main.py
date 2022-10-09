"""Imports"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root

    Returns:
        json: Hello World
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Read item

    Args:
        item_id (int): Item ID

    Returns:
        json: Item ID
    """
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    """Read user me

    Returns:
        json: User ID
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    """Read user

    Args:
        user_id (int): User ID

    Returns:
        json: User ID
    """
    return {"user_id": user_id}
