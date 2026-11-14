"""Fetch The Treat: a Git quiz game with Max and Loony.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the game state is kept
- templates/   the HTML page
- static/      the stylesheet
"""


from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Fetch The Treat")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):
    """The start page: shows the current game state."""
    return templates.TemplateResponse(
        request, "index.html",storage.get_state()
    )


@app.post("/help")
def help_route():
    storage.help_used()
    return RedirectResponse("/", status_code=303)

@app.post("/restart")
def restart_route():
    storage.restart()
    return RedirectResponse("/", status_code=303)

@app.post("/answer")
def answer(choice: int = Form(...)):
    storage.answer(choice)
    return RedirectResponse("/", status_code=303)
