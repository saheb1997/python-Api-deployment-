# python-Api-deployment-

<!-- Topic -> CRUD(Create,Read,Update,Delete) -->

Create -> post -> /post -> @app.post("/posts)

read -> Get -> /post/:id -> @app.get("/post/{id})
-> Get -> /post -> @app.get(/post)

update -> PUT/PATCH -> @app.put("/post/{id})

Delete -> Delete -> /post/:id ->@app/delete("/post/{id})

<!-- for raise 440 error -->

from fastapi import HTTPException
@app.get("/posts/{id}")
def get_post(id:int,response:Response):
post = find_post(id)
if(not post):
raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
detail=f"post with if:{id} was not found")
return {"post_detail":post}
