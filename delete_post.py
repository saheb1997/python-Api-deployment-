from fastapi import FastAPI,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import HTTPException


app = FastAPI()

id=2
@app.get("/posts")
def delete_post():
   return {"hellow world"}
    