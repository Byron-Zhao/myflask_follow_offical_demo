#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project   : myflask_follow_offical_demo 
# File      : hello.py
# Author    : Byron Zhao
# Email     : 330726651@qq.com
# C_Time    : 2020/7/29 15:27
# Version   : V1.0.0
# Info.     : 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello work"


if __name__ == '__main__':
    app.run()
    print("End of the story")


