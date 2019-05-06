import numpy as np

def nearest_point(P, Q):
    P = np.array(P)
    Q = np.array(Q)
    dis = np.zeros(P.shape[0])
    index = np.zeros(Q.shape[0], dtype = np.int)

    for i in range(P.shape[0]):
        minDis = np.inf
        for j in range(Q.shape[0]):
            tmp = np.linalg.norm(P[i] - Q[j], ord = 2)
            if minDis > tmp:
                minDis = tmp
                index[i] = j
        dis[i] = minDis
    return np.sum(dis), index


