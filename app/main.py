from fastapi import FastAPI,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import HTTPException

app = FastAPI()
 
# here "/" refer for root directory and if we give "/user" then for get the acess then after url need to give "/user" then able to see the output\
# get ---> method
#"/" path 
# root ---> fucntion

# It try to match when it get the first match it stop the search and give the output
# @app.get("/")
# def root():
#     return { "message": "hellow World new project"}







# @app.get("/post")
# def post1():
#     return {"message":"post1 called"}

# @app.get("/post2")
# def post2():
#     return {"message":"post2 called"}

# post request 
# @app.post("/createpost")
# def create_posts(payload: dict =Body(...)):
#     print(payload)
#     return {"title":payload['title'],
#             "content":payload['content']}
#title str , content str , bool


class post(BaseModel):
    title: str
    content: str
    publish: bool=True
    



mypost = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","content":"I like piza","id":2}]

# @app.get("/post")
# def send_post():
#     return {"data":mypost}

# @app.post("/post",status_code=status.HTTP_201_CREATED)
# def create_posts(post:post):
#     post_dict = post.model_dump()
#     post_dict['id']=randrange(0,10000000)
#     mypost.append(post_dict)
#     return {"data":post_dict}



# this is for geting last post 

# @app.get("/posts/latest")
# def latest():
#     post =mypost[len(mypost)-1]
#     return {"detail":post}

# # getting the post based on id


# def find_post(id):
#     for p in mypost:
         
#         if(p["id"]==id):
#             print("inside")
#             return p
   


# # id:int use that id must be a intiger
# @app.get("/posts/{id}")
# def get_post(id:int,response:Response):
#     post = find_post(id)
#     if(not post):
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'message':f"post with id:{id} not found"}

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with if:{id} was not found")
#     return {"post_detail":post}


# def find_index_post(id):
#     for i , p in enumerate (mypost):
#         if p['id']==int(id):
#             # print("inside")
#             return i

# # delete post
# @app.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     index=find_index_post(id)
#     print(index)
#     if(not index):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id:{id} was not found")

#     mypost.pop(index)
#     return {'message':'post was deleted'}


# @app.put("/post/{id}")
# def update_post(id:int,Post:post):
#     print(post)
#     index=find_index_post(id)
#     # print(index)
#     # print(index)
#     if index==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id:{id} was not found")
#     post_dict = Post.model_dump()
#     post_dict['id']= id
#     mypost[index]=post_dict
#     return {'data':post_dict}



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