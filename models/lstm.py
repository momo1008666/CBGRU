# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 20:05
@Author  : Chen_Sir
@FileName: lstm.py
@SoftWare: PyCharm
"""
from keras.layers import LSTM, Input, ReLU, Dropout
from keras.models import Model
from Parser import parameter_parser

args = parameter_parser()


def get_lstm(INPUT_SIZE, TIME_STEPS, dropout=args.dropout):
    """
    获得LSTM模型
    :param INPUT_SIZE: 生成矩阵的长
    :param TIME_STEPS: 生成矩阵的宽
    :param dropout: 损失率
    :return:
    """
    inp = Input((INPUT_SIZE, TIME_STEPS))
    models = LSTM(
        units=300,
        input_shape=(INPUT_SIZE, TIME_STEPS),
    )(inp)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    models = ReLU()(models)
    model = Model(inp, models)
    return model