###############################################################################
####    imports
###############################################################################
# std
import asyncio
import os

# third party
from fastapi import FastAPI, WebSocket, Form, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse, JSONResponse, FileResponse
from jinja2 import Environment, FileSystemLoader

# your project!
from .doing_things import do_thing



###############################################################################
####    globals
###############################################################################
# web page templates
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, "web/templates")
env = Environment(loader=FileSystemLoader(templates_dir))
template_index = env.get_template("index.html")

# webserver objects
app = FastAPI()



###############################################################################
####    fast api events
###############################################################################
@app.on_event("startup")
async def startup():
    print(f'SERVER STARTING UP')


@app.on_event("shutdown")
async def shutdown():
    print(f'SERVER SHUTTING DOWN')



###############################################################################
####    fast api routes
###############################################################################
@app.get("/")
async def root():
    page_data = template_index.render()
    return HTMLResponse(page_data)


@app.get("/do-thing")
async def get_do_thing():
    await do_thing()
    return JSONResponse({"hey": "there!"})
