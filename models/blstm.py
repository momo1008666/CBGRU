# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 20:23
@Author  : Chen_Sir
@FileName: blstm.py
@SoftWare: PyCharm
"""
from keras.layers import Dropout, LSTM, Bidirectional, ReLU, Input, Dense
from keras.models import Model
from Parser import parameter_parser
args = parameter_parser()
print(args.dropout)


def get_blstm(INPUT_SIZE, TIME_STEPS, dropout=args.dropout):
    inp = Input((INPUT_SIZE, TIME_STEPS))
    models = Bidirectional(
        LSTM(300),
        input_shape=(INPUT_SIZE, TIME_STEPS)
    )(inp)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    models = Dense(300)(models)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    model = Model(inp, models)
    return model