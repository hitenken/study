import numpy as np

def show(A):
    print("配列\n", A)
    print("次元数", np.ndim(A))
    print("形状", A.shape)
    print(A.shape[0],"\n")

A = np.array([1, 2, 3, 4])
show(A)
B = np.array([[1, 2], [3, 4], [5, 6]])
show(B)