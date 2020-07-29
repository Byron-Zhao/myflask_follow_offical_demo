#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project   : myflask_follow_offical_demo 
# File      : auth.py
# Author    : Byron Zhao
# Email     : 330726651@qq.com
# C_Time    : 2020/7/29 17:18
# Version   : V1.0.0
# Info.     : 


import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

if __name__ == '__main__':
    print("End of the story")


