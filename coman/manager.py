# -*- coding: utf-8 -*-

# @File    : manager.py
# @Date    : 2022-06-11
# @Author  : qyanls

from application import app, manager
from flask_script import Server, Command
from comanUrls import *

manager.add_command("runserver", Server(host="127.0.0.1", use_debugger=True, use_reloader=True))

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())

    except Exception as e:
        import traceback
        traceback.print_exc()


