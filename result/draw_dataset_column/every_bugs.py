# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/13 12:02
@Author  : Chen_Sir
@FileName: every_bugs.py
@SoftWare: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt
from pyecharts import Pie
bugs_name = ['Callstack Depth Attack',
             'IntegerOverflow',
             'IntegerUnderflow',
             'Timestamp',
             'Reentry',
             'Infinite Loop',
             ]

bugs_numbers = [1378, 1640, 1988, 1779, 1671, 1317]
pie = Pie()
pie.add(
    "",
    bugs_name,
    bugs_numbers,
    is_label_show=True,
    is_more_utils=True,
)
pie.render(path="Bing2.html")