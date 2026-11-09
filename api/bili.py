# -*- coding: utf-8 -*-
"""B站 API 代理：浏览器不能直接跨域调 api.bilibili.com，所以走这里转发。"""
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BILI_HOST = "https://api.bilibili.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}


@app.route("/api/bili")
def bili():
    sub = request.args.get("path", "").strip("/")
    if not sub:
        return jsonify({"code": -1, "message": "missing path"}), 400

    # 除 path 外，其余查询参数（ps/pn 等）原样转发给 B 站
    params = {k: v for k, v in request.args.items() if k != "path"}

    try:
        r = requests.get(f"{BILI_HOST}/{sub}", params=params, headers=HEADERS, timeout=8)
        body = r.content
        ctype = r.headers.get("Content-Type", "application/json; charset=utf-8")
        return (body, r.status_code, {"Content-Type": ctype, "Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return jsonify({"code": -1, "message": str(e)}), 502
