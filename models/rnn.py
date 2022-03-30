# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 20:42
@Author  : Chen_Sir
@FileName: rnn.py
@SoftWare: PyCharm
"""
from keras.layers.recurrent import SimpleRNN
from keras.layers import Dropout, ReLU, Input, Dense
from Parser import parameter_parser
from keras.models import Model
args = parameter_parser()


def get_rnn(INPUT_SIZE, TIME_STEPS, dropout=args.dropout):
    inp = Input((INPUT_SIZE, TIME_STEPS))
    models = SimpleRNN(
        units=300,
        input_shape=(INPUT_SIZE, TIME_STEPS)
    )(inp)
    models = ReLU()(models)
    models = Dropout(dropout)(models)
    models = Dense(300)(models)
    models = ReLU()(models)
    model = Model(inp, models)
    return model