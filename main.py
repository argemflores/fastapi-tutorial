"""Imports"""
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


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


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Get model

    Args:
        model_name (ModelName): Model name

    Returns:
        json: Model
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
