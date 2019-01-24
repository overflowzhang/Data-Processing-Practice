# 时间-分钟-车流量-三维图像

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

def get_list(name,sheet):
    list = [0 for i in range(1,1441)]
    df = pd.read_excel(name,sheet)
    for one in df['过车时间']:
        t = re.split('[:\s]',str(one))
        minute = int(t[-3]) * 60 + int(t[-2])
        list[minute] += 1
    return list
       
def get_view(list):
    fig = plt.figure(dpi = 300)
    ax = fig.add_subplot(111,projection='3d')
    for ys in range(1,7):
        z = list[ys-1]
        xs = range(1,1441)  
        ax.bar(xs, z, ys, zdir='y',  alpha=0.8)

    ax.set_xlabel('Minute')
    ax.set_ylabel('Date')
    ax.set_zlabel('Num of Car')
    plt.show()
    %matplotlib inline

if __name__ == '__main__':
    list1 = get_list('02010137香蜜湖路市委党校路段北行2018-3-18.xlsx','Sheet0')
    list2 = get_list('02010137香蜜湖路市委党校路段北行2018-3-26.xlsx','Sheet0')
    list3 = get_list('02010137香蜜湖路市委党校路段北行2018-3-27.xlsx','Sheet0')
    list4 = get_list('02010137香蜜湖路市委党校路段北行2018-3-28.xlsx','Sheet0')
    list5 = get_list('02010137香蜜湖路市委党校路段北行2018-3-28.xlsx','Sheet0')
    list6 = get_list('02010137香蜜湖路市委党校路段北行2018-3-30.xlsx','Sheet0')
    list7 = get_list('02010137香蜜湖路市委党校路段北行2018-3-31.xlsx','Sheet0')
    list = [list1,list2,list3,list4,list5,list6,list7]
    get_view(list)