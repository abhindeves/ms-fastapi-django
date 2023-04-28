from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from functools import lru_cache
import pathlib

class Settings(BaseSettings):
    debug: bool = False

    class config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()

DEBUG = get_settings().debug
app = FastAPI()
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

@app.get("/",response_class=HTMLResponse) # http GET
def home_view(request:Request, settings:Settings = Depends(get_settings)):
    print(settings.debug)
    return templates.TemplateResponse("home.html",{"request":request, "abc":123} )

@app.post("/") # http POST
def home_detail_view():
    return {"hello": "world"}
