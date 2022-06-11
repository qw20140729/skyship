# -*- coding: utf-8 -*-

# @File    : application.py
# @Date    : 2022-06-11
# @Author  : qyanls

from flask import Flask
from flask_script import Manager

app = Flask(__name__)

# 载入配置文件
app.config.from_pyfile("config/base_setting.py")

manager = Manager(app)



