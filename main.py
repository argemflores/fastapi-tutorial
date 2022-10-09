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
