import numpy as np
from random import randrange

A = np.round(np.arange(5,-5.2,-0.2),2).tolist()

pow = np.round(np.arange(0,1.01,0.01),3)
B = np.round(np.power(10,pow),4).tolist()

C = np.reshape(np.arange(1,101),(10,10),order='F')

D = np.arange(1,13)*np.arange(1,13).reshape(12,1)

def E(X):
    e_array = X[0::2,0::2]
    return e_array

def F(X):
    f_array = X[1:-1,1:-1]
    return f_array

def G(X):
    g_array = np.vstack((np.diagonal(X,offset=-1),np.diagonal(X,offset=1))).T
    # The shape of return value will be (M, 2)
    return g_array


# Do NOT modifiy the main function
def main():
    print('A: \n', A, '\n')
    print('B: \n', B, '\n')
    print('C: \n', C, '\n')
    print('D: \n', D, '\n')

    M = randrange(3, 8)
    X = np.random.randint(10, size=(M, M))

    print('X: \n', X, '\n')
    print('E: \n', E(X), '\n')
    print('F: \n', F(X), '\n')
    print('G: \n', G(X), '\n')


if __name__ == "__main__":
    main()