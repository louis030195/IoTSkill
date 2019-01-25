#!/usr/bin/python2
#coding: utf-8

from flask import *
import os
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def index():
    return """<!doctype html>
            <title>Hello from Flask</title>
            <img src="/static/img.JPG">"""

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')