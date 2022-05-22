# %%
import numpy as np

x = np.array([1, 2, 3])
print(x.__class__) # 클래스 이름 표시
# <class 'numpy.ndarray'>

print(x.shape)
# (3,)

print(x.ndim)
# 1

W = np.array([[1,2,3],[4,5,6]])
print(W)
# [[1 2 3]
#  [4 5 6]]

print(W.shape)
# (2, 3)

print(W.ndim)
# 2

X = np.array([[0, 1 ,2], [3, 4, 5]])

# 1.1.2 행렬의 원소별 연산
print(W + X)
print(X * W)

# 1.1.3 브로드캐스트

A = np.array([[1, 2], [3, 4]])
print(A * 10)




