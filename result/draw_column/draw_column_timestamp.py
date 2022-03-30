# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/11 14:21
@Author  : Chen_Sir
@FileName: draw_column_timestamp.py.py
@SoftWare: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

models = ('DeeSCVHunter', 'AME', 'TMP', 'DA-GCN', 'My-Hybird')
ACC = [80.5, 86.52, 83.45, 87.54, 93.02]
REC = [74.86, 86.23, 83.82, 82.25, 97.45]
PRE = [85.53, 82.07, 75.05, 87.15, 89.47]
F1 = [79.93, 84.1, 79.19, 84.83, 93.29]
bar_width = 0.2
y_major_locator = MultipleLocator(5)
x = np.arange(len(models))
acc = x - 1.5 * bar_width
rec = x - 0.5 * bar_width
pre = x + 0.5 * bar_width
f1 = x + 1.5 * bar_width
# 使用两次 bar 函数画出两组条形图
plt.bar(acc, height=ACC, width=bar_width, color='c', label='ACC', alpha=0.5, linewidth=10)
plt.bar(rec, height=REC, width=bar_width, color='b', label='REC', alpha=0.5, linewidth=10)
plt.bar(pre, height=PRE, width=bar_width, color='r', label='PRE', alpha=0.5, linewidth=10)
plt.bar(f1, height=F1, width=bar_width, color='orange', label='F1', alpha=0.5, linewidth=10)
for a, b in zip(acc, ACC):
    plt.text(a, b + 0.1, '%.2f' % b, ha='center', va='bottom', fontsize=9, rotation=90)
for a, b in zip(rec, REC):
    plt.text(a, b + 0.1, '%.2f' % b, ha='center', va='bottom', fontsize=9, rotation=90)
for a, b in zip(pre, PRE):
    plt.text(a, b + 0.1, '%.2f' % b, ha='center', va='bottom', fontsize=9, rotation=90)
for a, b in zip(f1, F1):
    plt.text(a, b + 0.1, '%.2f' % b, ha='center', va='bottom', fontsize=9, rotation=90)
plt.legend()  # 显示图例
ax = plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
ax.set_xticklabels(labels=models, rotation=40)
plt.ylim(70, 105)
plt.xticks(x, labels=models, fontsize=9)
plt.show()