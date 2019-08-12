import numpy as np

def make_matrix(M, i, j, length):
    newM = np.zeros([length - 1]*2)
    for x in range(length):
        if x != i:
            for y in range(length):
                if y != j:
                    newM[x - (x > i), y - (y > j)] = M[x, y]
    return newM

def get_determinant(M, det=0):
    if len(M) == 2:
        return M[0,0]*M[1,1] - M[1,0]*M[0,1]
    length = len(M)
    for i in range(length):
        det += M[0,i] * get_determinant(make_matrix(M, 0, i, length), det) * (-(i%2)*2+1)
    return det
