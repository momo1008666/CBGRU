# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/17 11:57
@Author  : Chen_Sir
@FileName: cnn.py
@SoftWare: PyCharm
"""
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten, Input, Dropout
from Parser import parameter_parser
from keras.models import Sequential
from keras.models import Model
args = parameter_parser()


def get_cnn(INPUT_SIZE, TIME_STEPS):
    model = Sequential()
    model.add(
        Convolution2D(
            filters=32,
            kernel_size=5,
            padding="same",
            batch_input_shape=(None, 1, 100, 300)
        )
    )
    model.add(Activation('relu'))
    model.add(MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2),
        padding='same',
    ))
    model.add(Convolution2D(filters=64, kernel_size=5, padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(Flatten())
    model.add(Dropout(args.dropout))
    return model