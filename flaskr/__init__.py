#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project   : myflask_follow_offical_demo 
# File      : __init__.py.py
# Author    : Byron Zhao
# Email     : 330726651@qq.com
# C_Time    : 2020/7/29 15:33
# Version   : V1.0.0
# Info.     : 

import os
from flask import Flask

def creat_app():
    app = Flask(__name__, instance_relative_config=True)

    return app



if __name__ == '__main__':
    print("End of the story")


