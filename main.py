from typing import Union
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})