import datetime as DT
import matplotlib.dates as mdates
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib.ticker import AutoMinorLocator
interactive(True)


def fun_plot_ts_red_blue(dates, Y, ylbl, sp_mrkr):

    ax = plt.subplot(sp_mrkr)

    # --plot the time series, with positive shaded red and negative shaded blue
    plt.plot(dates, Y, linewidth=0.2, color='black')
    ax.fill_between(dates, 0, Y, where=Y >= 0, color='red',
                    linewidth=0.1, interpolate=True)
    ax.fill_between(dates, 0, Y, where=Y <= 0, color='blue',
                    linewidth=0.1, interpolate=True)

    # --set x-limits from first dates to December of the last year
    ax.set_xlim([dates[0], DT.datetime(dates[-1].year, 12, 31)])

    # --get rid of the top and right
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # --set format of the dates for the x-axis
    if int(sp_mrkr[2]) < int(sp_mrkr[0]):
        xfmt = mdates.DateFormatter('')
    else:
        xfmt = mdates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_formatter(xfmt)
    ax.set_xticks(dates[0::12 * 5])
    plt.xticks(rotation=0)

    # --add x-minor tick marks at intervals of 5, this will produce
    # --a tick mark at Jan of every year
    minorLocator = AutoMinorLocator(5)
    ax.xaxis.set_minor_locator(minorLocator)

    # --x&y tick fontsizes
    matplotlib.rc('xtick', labelsize=8)
    matplotlib.rc('ytick', labelsize=8)

    # --ylabel
    plt.ylabel(ylbl)

    # --vertical lines for the last three years
    ylm = ax.get_ylim()
    yy = np.arange(dates[-1].year - 2, dates[-1].year + 1)
    mm = np.ones(3, dtype=np.int)
    dd = np.ones(3, dtype=np.int)
    for j in range(0, len(yy)):
        plt.vlines(DT.datetime(yy[j], mm[j], dd[j]),
                   ylm[0], ylm[1], color=np.ones(3) * 0.6,
                   alpha=0.3, linewidth=0.5)
