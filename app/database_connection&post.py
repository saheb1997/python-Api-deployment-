from fastapi import FastAPI,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import HTTPException
class post(BaseModel):
    title: str
    content: str
    publish: bool=True
    rating : Optional[int]=None



mypost = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","content":"I like piza","id":2}]

app = FastAPI()
import psycopg2
from psycopg2.extras import RealDictCursor
import time
while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='abc@123',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was sucessfull")
        break
    except Exception as error:
        print("connection to database failled")
        print("error:",error)
        time.sleep(2)

@app.get("/post")
def get_posts():
    cursor.execute(
        """
            SELECT * FROM post where title = 'second post';
        """
        )
    posts = cursor.fetchall()
    print(posts)
    return { "data": posts}

@app.post("/post")
def create_posts(post:post):
    cursor.execute("""
    INSERT INTO post (title,content,publish) 
    VALUES(%s,%s,%s) RETURNING *""",
    (post.title,post.content,post.publish))

    newpost = cursor.fetchone()
    conn.commit()
    return {"data":newpost}

print("\nf")