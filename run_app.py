#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:49:35 2017

@author: scott
"""

import logging
logging.basicConfig(filename="logs/debug.log", filemode="w", level=logging.DEBUG, format="%(name)s %(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("MAIN")
logger.debug("Starting")

from counter import FlaskApp

if __name__ == "__main__":
    FlaskApp.run()