from __future__ import unicode_literals
import youtube_dl

print('test')
def getinfo(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(url, download=False)
        return res
