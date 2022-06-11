# -*- coding: utf-8 -*-

# @File    : comanUrls.py
# @Date    : 2022-06-11
# @Author  : qyanls

from application import app

# 导入debug工具
from flask_debugtoolbar import DebugToolbarExtension
# 设定debug工具为True
app.debug =True
toolbar = DebugToolbarExtension(app)


# 蓝图定义
from controllers.index import index_page
# 注册蓝图
app.register_blueprint(index_page, url_prefix="/")



