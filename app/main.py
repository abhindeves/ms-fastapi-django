from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib

app = FastAPI()
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

@app.get("/",response_class=HTMLResponse) # http GET
def home_view(request:Request):
    return templates.TemplateResponse("home.html",{"request":request, "abc":123} )

@app.post("/") # http POST
def home_detail_view():
    return {"hello": "world"}
