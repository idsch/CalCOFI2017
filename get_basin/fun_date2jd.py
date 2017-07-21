import numpy as np
from jdcal import gcal2jd, jd2gcal


def fun_date2jd(ymd):

    nt = len(ymd)
    jd = np.zeros((nt, 2))
    for k in range(0, nt, 1):
        d1 = gcal2jd(ymd[k, 0], ymd[k, 1], ymd[k, 2])
        jd[k, :] = d1

    return jd
