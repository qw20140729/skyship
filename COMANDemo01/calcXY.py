# -*- encoding:utf-8 -*-
import re

def dealWithString(rootstr):
    leftvalue = re.findall('(\d+)', rootstr)
    return int(leftvalue[0]), int(leftvalue[1])