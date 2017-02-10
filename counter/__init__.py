#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:41:40 2017

@author: scott
"""

import logging
logger = logging.getLogger(__name__)
logger.debug("Starting")

from autologging import logged, traced

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
#from flask_marcopolo import MarcoPolo
from flask_mongoengine import MongoEngine
from flask_restful import Api as RESTApi

from counter.config import Prod, Dev

FlaskApp = Flask(__name__)
FlaskApp.config.from_object(Dev)

DB = MongoEngine(app)
ToolBar = DebugToolbarExtension(app)
Api = RESTApi(self.app)

from counter.views import hello_world
