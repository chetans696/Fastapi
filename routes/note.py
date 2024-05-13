from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/")
async def first():
  return "hello world"


@note.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
  return templates.TemplateResponse(request=request, name="index.html", context={"id": id})
