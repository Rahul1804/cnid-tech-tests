import time
import os
from flask import Flask


@app.route('/')
def hello():
    return 'Hello World!'
