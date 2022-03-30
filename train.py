# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 9:47
@Author  : Chen_Sir
@FileName: train.py
@SoftWare: PyCharm
"""
from keras.callbacks import CSVLogger
from keras.layers import Dense, concatenate
from keras.models import Model
from keras.optimizers import Adam
from get_train_test import get_train_test
from get_dataset import get_df_1
from get_dataset import get_df_2
from Parser import parameter_parser
from models.cnn import get_cnn
from keras.utils.vis_utils import plot_model
from models.gru import get_gru
from models.lstm import get_lstm
from models.blstm import get_blstm
from models.BiGRU import get_bigru
import numpy as np
from sklearn.metrics import confusion_matrix

num_classes = 2
args = parameter_parser()


# 模型
def ClassiFilerNet(INPUT_SIZE, TIME_STEPS):
    # 左边输入
    input1 = get_cnn(INPUT_SIZE, TIME_STEPS)
    # 右边输入
    input2 = get_bigru(INPUT_SIZE, TIME_STEPS)
    for layer in input2.layers:
        layer.name = layer.name + str("_2")
    inp1 = input1.input
    inp2 = input2.input
    merge_layers = concatenate([input1.output, input2.output])
    fc1 = Dense(300, activation='relu')(merge_layers)
    fc2 = Dense(300, activation='relu')(fc1)
    fc3 = Dense(num_classes, activation='softmax')(fc2)
    class_models = Model([inp1, inp2], [fc3])
    return class_models


def train():
    df1, base = get_df_1()
    df2, = get_df_2()
    x_train, x_test, y_train, y_test = get_train_test(df1)
    x_train_2, x_test_2, y_train_2, y_test_2 = get_train_test(df2)
    model = ClassiFilerNet(x_train.shape[1], x_train.shape[2])
    plot_model(model, to_file="model.png")
    print(model.summary())
    adam = Adam(lr=args.lr)
    model.compile(optimizer=adam,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    csv_logger = CSVLogger('log\\' + base + '_log.txt', append=True, separator=',')
    history = model.fit(
        x=[x_train.reshape(-1, 1, 100, 300), x_train_2],
        y=y_train,
        validation_data=([x_test.reshape(-1, 1, 100, 300), x_test_2], y_test),
        batch_size=args.batch_size,
        epochs=args.epochs,
        callbacks=[csv_logger]
    )
    loss, accuracy = model.evaluate([x_test.reshape(-1, 1, 100, 300), x_test_2],
                                    y_test,
                                    batch_size=y_test.shape[0],
                                    verbose=False)

    print("test loss:", str(loss))

    print("test accuracy", str(accuracy))

    predictions = (model.predict([x_test.reshape(-1, 1, 100, 300), x_test], batch_size=y_test.shape[0])).round()

    tn, fp, fn, tp = confusion_matrix(np.argmax(y_test, axis=1), np.argmax(predictions, axis=1)).ravel()
    print('False positive rate(FP): ', fp / (fp + tn))
    print('False negative rate(FN): ', fn / (fn + tp))
    recall = tp / (tp + fn)
    print('Recall: ', recall)
    precision = tp / (tp + fp)
    print('Precision: ', precision)
    print('F1 score: ', (2 * precision * recall) / (precision + recall))

    with open('log\\' + base + '_log.txt', mode='a') as f:
        f.write("df: " + base + '\n')
        f.write("test loss:" + str(loss) + "\n")
        f.write("test accuracy:" + str(accuracy) + "\n")
        f.write('False positive rate(FP): ' + str(fp / (fp + tn)) + "\n")
        f.write('False negative rate(FN): ' + str(fn / (fn + tp)) + "\n")
        f.write('Recall: ' + str(recall) + "\n")
        f.write('Precision: ' + str(precision) + "\n")
        f.write('F1 score: ' + str((2 * precision * recall) / (precision + recall)) + '\n')
        f.write("-------------------------------" + "\n")


if __name__ == '__main__':
    for i in range(20):
        train()
