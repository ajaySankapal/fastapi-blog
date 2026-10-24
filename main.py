from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get('/',include_in_schema=False)
@app.get('/posts',include_in_schema=False) # we can stack the routes also, the same response can be returned from this both the routes
# if we do include_in_schema=False this will be not included in the swagger api documentation
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"Home"})


@app.get("/api/posts")
def get_posts():
    return posts

