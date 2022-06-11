# -*- coding: utf-8 -*-

# @File    : index.py
# @Date    : 2022-06-11
# @Author  : qyanls

from flask import render_template

from flask import Blueprint
# 使用蓝图定义页面
index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    return render_template("index.html")

