from __future__ import unicode_literals
from sanic import Sanic
from sanic.response import json
import youtube_dl
app = Sanic()


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    info = getinfo('https://www.youtube.com/watch?v=BaW_jenozKc')
    return json(info)

def getinfo(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(url, download=False)
        return res