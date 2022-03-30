# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/11 10:41
@Author  : Chen_Sir
@FileName: draw_column_reentrancy.py
@SoftWare: PyCharm
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

models = ('DeeSCVHunter', 'Peacuilar', 'BLSTM-ATT', 'TMP', 'DR-GCN', 'AME', 'DA-GCN', 'My-Hybrid')
ACC = [93.02, 92.37, 88.47, 84.48, 81.47, 90.19, 91.15, 93.16]
REC = [83.46, 92.4, 88.48, 82.63, 80.89, 89.69, 82.00, 85.95]
PRE = [90.70, 91.80, 88.5, 74.06, 72.36, 86.25, 89.84, 96.30]
F1 = [86.87, 92.10, 88.26, 83.82, 76.39, 87.94, 85.43, 90.92]
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
plt.ylim(65, 100)
plt.xticks(x, labels=models, fontsize=9)
plt.show()
