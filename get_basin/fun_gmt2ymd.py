import time
import numpy as np


def fun_gmt2ymd(var, time_wnt):

    nt = len(var)
    yy = np.zeros((nt, time_wnt[0]))
    for k in range(0, nt, 1):
        d1 = time.gmtime(var[k])
        for j in range(0, 3, 1):
            yy[k, j] = d1[j]

    return yy
