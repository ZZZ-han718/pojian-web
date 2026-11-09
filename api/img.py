# -*- coding: utf-8 -*-
"""封面图代理：B 站 CDN 有防盗链，直接在浏览器里请求会挂，所以转发一层。"""
from flask import Flask, request, Response
import requests

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}


@app.route("/api/img")
def img():
    url = request.args.get("url", "")
    if not url:
        return ("", 400)
    if not url.startswith("http"):
        return ("", 400)
    try:
        r = requests.get(url, headers=HEADERS, timeout=8)
        resp = Response(
            r.content,
            content_type=r.headers.get("Content-Type", "image/jpeg"),
            headers={
                "Access-Control-Allow-Origin": "*",
                "Cache-Control": "public, max-age=86400",
            },
        )
        return resp
    except Exception:
        return ("", 502)
