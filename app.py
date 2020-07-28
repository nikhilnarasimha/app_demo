# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:15:24 2020

@author: malat
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Nikhil Narasimha"

app.run(port=5000)


































