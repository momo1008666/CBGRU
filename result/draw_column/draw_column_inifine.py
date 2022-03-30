# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/11 17:41
@Author  : Chen_Sir
@FileName: draw_column_inifine.py
@SoftWare: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

models = ('TMP', 'DR-GCN', 'AME', 'My-Hybrid')
ACC = [74.61, 68.34, 80.32, 93.16]
REC = [74.32, 67.82, 79.08, 89.15]
PRE = [73.89, 64.89, 78.69, 98.29]
F1 = [74.1, 66.32, 78.88, 93.5]
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
plt.ylim(60, 105)
plt.xticks(x, labels=models, fontsize=9)
plt.show()