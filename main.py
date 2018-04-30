#!/usr/bin/env python3
# coding: utf-8

from bottle import Bottle, request, HTTPResponse, run
import json
from lib.furigana_converter import FuriganaConverter


app = Bottle()

@app.get('/furigana')
def furigana():
    text = request.params.q
    converter = FuriganaConverter()
    body = json.dumps({
        'text': text,
        'furigana': converter.get_furigana(text)
    }).encode().decode("unicode_escape")
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    return r

run(app, host="localhost", port=8000, debug=True)
