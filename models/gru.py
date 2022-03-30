# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/20 9:08
@Author  : Chen_Sir
@FileName: gru.py
@SoftWare: PyCharm
"""
from Parser import parameter_parser
from keras.layers import Input, ReLU, Dropout
from keras.layers.recurrent import GRU
from keras.models import Model

args = parameter_parser()


def get_gru(INPUT_SIZE, TIME_STEPS, dropout=args.dropout):
    """
    获得GRU最基础模型
    :param INPUT_SIZE: 输入的长度
    :param TIME_STEPS: 输入的宽度
    :param dropout: 损失率
    :return: GRU模型
    """
    inp = Input((INPUT_SIZE, TIME_STEPS))
    models = GRU(
        units=300,
        input_shape=(INPUT_SIZE, TIME_STEPS)
    )(inp)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    models = ReLU()(models)
    model = Model(inp, models)
    return model
