# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/10 11:56
@Author  : Chen_Sir
@FileName: draw_all.py
@SoftWare: PyCharm
"""
import csv
import matplotlib.pyplot as plt


def draw(plt, csv_file, num):
    epoch = []
    accuracy = []
    loss = []
    accuracy_1 = []
    loss_1 = []
    for info in csv_file:
        if csv_file.line_num == 1:
            continue
        epoch.append(int(info[0]) + 1)
        accuracy.append(float(info[1]) * 100)
        loss.append(float(info[2]) * 100)
        accuracy_1.append(float(info[3]) * 100)
        loss_1.append(float(info[4]) * 100)

    plt.subplot(2, 3, num)
    plt.plot(epoch, accuracy, lw=1.5, color='b', label='train acc', marker='', markevery=1,
             mew=1)
    plt.plot(epoch, loss, lw=1.5, color='r', label='train loss', marker='', markevery=1,
             mew=1)
    plt.plot(epoch, accuracy_1, lw=1.5, color='y', label='train val-acc', marker='', markevery=1,
             mew=1)
    plt.plot(epoch, loss_1, lw=1.5, color='g', label='train val-loss', marker='', markevery=1,
             mew=1)
    plt.xlabel("epochs", fontsize=10)
    plt.ylabel("Accuracy", fontsize=10)
    plt.legend(fontsize=7)
    csv_file = ["Infinite Loop", "Reentry", "Integer Overflow", "Callstack Depth Attack",
                "Timestamp Dependency", "Integer Underflow"]
    plt.title(csv_file[i - 1])


csv_file_infinite = csv.reader(open("../infinite_dataset.CSV"))
csv_file_reentrancy = csv.reader(open("../reentrancy_dataset.CSV"))
csv_file_integer = csv.reader(open("../Integer_dataset.CSV"))
csv_file_CDAV = csv.reader(open("../CDAV_dataset.CSV"))
csv_file_timeStamp = csv.reader(open("../timestamp_dataset.CSV"))
csv_file_integer_underflow = csv.reader(open("../Integer_UnderFlow.CSV"))
fig = plt.figure()
csv_file_names = [csv_file_infinite, csv_file_reentrancy
                  , csv_file_integer, csv_file_CDAV, csv_file_timeStamp, csv_file_integer_underflow ]

i = 1
for csv_file in csv_file_names:
    print(csv_file)
    draw(plt, csv_file, i)
    i = i + 1

plt.show()

