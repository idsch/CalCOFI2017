import datetime as DT
import numpy as np
import scipy.io as sio
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib import interactive
from fun_gmt2ymd import fun_gmt2ymd
from fun_date2jd import fun_date2jd
from fun_plot_ts_red_blue import fun_plot_ts_red_blue
# from matplotlib.ticker import MultipleLocator
# from matplotlib.ticker import AutoMinorLocator
interactive(True)


# -------------------------------------------------------
# -- Input variables, change these
name_wnt = ['ONI', 'PDO', 'NPGO']

mon_wnt1 = 1
mon_wnt2 = 5

yr_bgn = 1980
yr_end = 2017

file_type = 'mat'

ext_wnt = 'eps'

# --construct a datetime list for all possible months between yr_bgn and yr_end
strt_dt = DT.datetime(yr_bgn, 1, 1)
end_dt = DT.datetime(yr_end, 12, 1)

dates_all = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]

# --create output ndarray with the first two columns the year and month
data_all = np.zeros((len(dates_all), 2 + num_name_wnt))
data_all[:, 0] = dates_all.year
data_all[:, 1] = dates_all.mon()

# --the data was downloaded in this directory
dir_mat = '/Users/IsaacSchroeder/mat_files/Work/TS/data/python_erddap/oni_pdo_npgo/'

# --loop over name_wnt and get data from mat_files
num_name_wnt = len(name_wnt)

plt.clf()


for i in range(0, num_name_wnt):
    # for i in range(0, 1):
    # --the final directory name has the name_wnt in it
    dir_final = dir_mat + name_wnt[i]
    # --build filename
    fn = dir_final + '/ts_{}_{}_{:02d}_{}_{:02d}.{}'.format(
        name_wnt[i], yr_bgn, mon_wnt1, yr_end, mon_wnt2, file_type)

    # --read the filename and get variable names
    struct_name = 'cciea_OC_{}'.format(name_wnt[i])
    mat_contents = sio.loadmat(fn)
    oct_struct = mat_contents[struct_name]
    field_names = oct_struct.dtype.names

    # --now, place all variables of the structure into a dictionary
    val = oct_struct[0, 0]

    var = {}
    for j in field_names:
        var[j] = val[j]

    # --year, mon, day, in "time" the epoch starts on 1970,1,1
    var_time = var['time']
    time_wnt = [3]
    ymd = fun_gmt2ymd(var_time, time_wnt)
    jd1 = fun_date2jd(ymd)

    dates = [DT.datetime.strptime('{}{:02d}{:02d}'.format(
        int(ddd[0]), int(ddd[1]), int(ddd[2])), '%Y%m%d') for ddd in ymd]

    ndates = [np.datetime64('{}{:02d}{:02d}'.format(
        int(ddd[0]), int(ddd[1]), int(ddd[2]))) for ddd in ymd]

    # dates = [DT.datetime.strptime(str(int(date)), '%Y%m%d') for date in year]

    # --

    # --Y data are the field_names of the dictionary
    Y = np.squeeze(var[field_names[-1]])

    # --place Y data in Y_all, for CSV

    if i == 0:
        Y_all = Y
        mrkr_all = np.ones(
    else:
        Y_all=np.concatenate((Y_all, Y))

    # --make as many subplots as field_names
    sp_mrkr='{}{}{}'.format(num_name_wnt, 1, i + 1)

    fun_plot_ts_red_blue(dates, Y, name_wnt[i], sp_mrkr)

# --save the figure
name_str='_'.join(name_wnt)
fn_save='plots/{}_{}_{:02d}_{}_{:02d}.{}'.format(
    name_str, yr_bgn, mon_wnt1, yr_end, mon_wnt2, ext_wnt)

plt.savefig(fn_save, dpi=300)

# --create CSV file
fn_csv='plots/{}_{}_{:02d}_{}_{:02d}.{}'.format(
    name_str, yr_bgn, mon_wnt1, yr_end, mon_wnt2, ext_wnt)

header='year,mon,' + ','.join(name_wnt)

# yc = np.reshape(yrs, (-1, 1))
# catch_mn_std = np.concatenate(a
#                              (ymd[0, :], ymd[1, :], catch_std.transpose())).transpose()


# np.savetxt(fn_csv, catch_mn_std, delimiter=',',
#           fmt='%5.3f', header=header)
