"""Imports"""
from enum import Enum
from typing import Union
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    """Model

    Args:
        str (name): Name
        Enum (Enum): Enumeration
    """
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


@app.get("/")
async def root():
    """Root

    Returns:
        json: Hello World
    """
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     """Read item

#     Args:
#         item_id (int): Item ID

#     Returns:
#         json: Item ID
#     """
#     return {"item_id": item_id}


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
    if model_name is ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Read file

    Args:
        file_path (str): File path

    Returns:
        json: File path
    """
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_fake_item(skip: int = 0, limit: int = 10):
    """Read fake item

    Args:
        skip (int, optional): Skip index. Defaults to 0.
        limit (int, optional): Limit number. Defaults to 10.

    Returns:
        json: Fake item
    """
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_default_item(item_id: str, q: Union[str, None] = None):
    """Read default item

    Args:
        item_id (str): Item ID
        q (str, optional): Query parameter. Defaults to None.

    Returns:
        json: Item ID
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
