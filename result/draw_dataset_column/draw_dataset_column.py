# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/13 10:50
@Author  : Chen_Sir
@FileName: draw_dataset_column.py
@SoftWare: PyCharm
"""
import numpy as np
from pyecharts import Pie
import matplotlib.pyplot as plt
bugs_name = ['Callstack Depth Attack',
             'IntegerOverflow',
             'IntegerUnderflow',
             'Transaction Ordering Dependence',
             'Reentry',
             'Timestamp',
             ]
bugs_number = ['882', '30991', '23642', '4305','306', '1454']

pie = Pie()
pie.add(
    "",
    bugs_name,
    bugs_number,
    is_label_show=True,
    is_more_utils=True,
    legend_pos="right",
)
pie.render(path="Bing1.html")