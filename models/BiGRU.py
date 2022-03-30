# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/1 16:04
@Author  : Chen_Sir
@FileName: BiGRU.py
@SoftWare: PyCharm
"""
from keras.layers import Dropout, LSTM, Bidirectional, ReLU, Input, Dense,GRU
from keras.models import Model
from Parser import parameter_parser
args = parameter_parser()


def get_bigru(INPUT_SIZE, TIME_STEPS, dropout=args.dropout):
    inp = Input((INPUT_SIZE, TIME_STEPS))
    models = Bidirectional(
        GRU(300),
        input_shape=(INPUT_SIZE, TIME_STEPS)
    )(inp)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    models = Dense(300)(models)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    model = Model(inp, models)
    return model