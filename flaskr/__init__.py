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


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # 进行缺省设置：
    app.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"))

    if test_config is None:  # 未人为传参则从配置文件中读取配置
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)  # 否则以传入的参数为准

    # 确保数据库SQlite的文件夹存在，数据库文件会被保存在里面
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello world!"

    from . import db
    db.init_app(app=app)

    return app



if __name__ == '__main__':
    print(__name__)

    print("End of the story")


