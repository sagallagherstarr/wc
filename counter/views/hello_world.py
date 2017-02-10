#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 20:04:05 2017

@author: scott
"""

import flask
from flask_classy import FlaskView

from counter import FlaskApp

class HelloWorldView(FlaskView):
    def index(self):
        return "<h1>Hello World!</h2>"

HelloWorldView.register(FlaskApp)
    
