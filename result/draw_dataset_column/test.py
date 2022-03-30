# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/13 11:15
@Author  : Chen_Sir
@FileName: test.py
@SoftWare: PyCharm
"""

from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add(
    "",
    attr,
    v1,
    is_label_show=True,
    is_more_utils=True
)
pie.render(path="Bing1.html")