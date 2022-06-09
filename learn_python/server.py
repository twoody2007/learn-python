###############################################################################
####    imports
###############################################################################
# std
import asyncio
import os
import traceback

# third party
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
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
async def get_root():
    page_data = template_index.render()
    return HTMLResponse(page_data)


@app.get("/js/{file_name}")
async def get_content(
    file_name: str,
) -> Response:
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "text/javascript",
    }
    try:
        data = None
        content_loc = os.path.join(root, "web/js")
        with open(f"{content_loc}/{file_name}", "rb") as f:
            data = f.read()
        return Response(data, headers=headers, status_code=200)
    except Exception:
        err_str = "Server Error! Info below:\n" + traceback.format_exc()
        print(f"Error: {err_str}")
        return Response(err_str, headers=headers, status_code=500)

@app.get("/do-thing")
async def get_do_thing():
    await do_thing()
    return JSONResponse({"hey": "there!"})
