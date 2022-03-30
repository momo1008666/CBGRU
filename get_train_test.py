# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/17 10:09
@Author  : Chen_Sir
@FileName: get_train_test.py
@SoftWare: PyCharm
"""
from Parser import parameter_parser
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
args = parameter_parser()


def get_train_test(dataset):
    vectors = np.stack(dataset.iloc[:, 0].values)
    labels = dataset.iloc[:, 1].values
    positive_index = np.where(labels == 1)[0][:1988]
    print(len(positive_index))
    negative_index = np.where(labels == 0)[0][:]
    print(len(negative_index))
    undersampled_negative_idxs = np.random.choice(negative_index, len(positive_index), replace=False)
    resampled_idxs = np.concatenate([positive_index, undersampled_negative_idxs])
    x_train, x_test, y_train, y_test = train_test_split(vectors[resampled_idxs], labels[resampled_idxs],
                                                        test_size=0.2, stratify=labels[resampled_idxs])
    return x_train, x_test, to_categorical(y_train), to_categorical(y_test)
