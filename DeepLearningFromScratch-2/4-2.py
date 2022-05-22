import numpy as np


def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)


# 정답은 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
c = sum_squares_error(np.array(y), np.array(t))
print("2로 예측했을 경우" ,c)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
d = sum_squares_error(np.array(y), np.array(t))
print("7로 예측했을 경우" ,d)


import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
