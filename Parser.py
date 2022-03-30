import argparse


def parameter_parser():
    # Experiment parameters
    parser = argparse.ArgumentParser(description='Smart Contracts vulnerability Detection')

    parser.add_argument('-D', '--dataset', type=str, default='train_data/infinite_loop_1317.txt',
                        choices=['train_data/infinite_loop_1317.txt', 'train_data/reentrancy_1671.txt'
                                 'train_data/timestamp.txt','dataset_Integeroverflow.txt', 'dataset_Integer.txt'
                                 ,'dataset_integer_big.txt', 'dataset_reency.txt', 'dataset_IntegerUnderFlow.txt'])
    parser.add_argument('-M', '--model', type=str, default='BLSTM_Attention',
                        choices=['BLSTM', 'BLSTM_Attention', 'LSTM_Model', 'Simple_RNN', 'Baseline_FC'])
    parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
    parser.add_argument('-d', '--dropout', type=float, default=0.5, help='dropout rate')
    parser.add_argument('--vector_dim', type=int, default=300, help='dimensions of vector')
    parser.add_argument('--epochs', type=int, default=50, help='number of epochs')
    parser.add_argument('-b', '--batch_size', type=int, default=128, help='batch size')
    parser.add_argument('-th', '--threshold', type=float, default=0.5, help='threshold')
    parser.add_argument('--embedding', type=str, default="word2vec",
                        choices=['word2vec', 'FastText'])

    return parser.parse_args()
