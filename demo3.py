# 多项式拟合

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def get_list(name,sheet):
    list = [0 for i in range(1,1441)]
    df = pd.read_excel(name,sheet)
    for one in df['时间']:
        t = re.split('[:\s]',str(one))
        minute = int(t[-3]) * 60 + int(t[-2])
        list[minute] += 1
    return list
       
def get_view(list):
    fig = plt.figure(dpi = 300)
    t = range(1,1441)
    z = np.polyfit(t,list,15)
    print(z)
    y = [0 for i in range(1,1441)]
    for i in range(1,1441):
        temp = z[0]*pow(i,15) + z[1]*pow(i,14) + z[2]*pow(i,13) +  z[3]*pow(i,12) +  z[4]*pow(i,11) +  z[5]*pow(i,10) +  z[6]*pow(i,9) +  z[7]*pow(i,8) + z[8]*pow(i,7)+  z[9]*pow(i,6)+  z[10]*pow(i,5)+  z[11]*pow(i,4)+  z[12]*pow(i,3)+  z[13]*pow(i,2)+  z[14]*pow(i,1)+  z[15]
        y[i-1] = temp
    plt.scatter(t,list,s=0.5)
    print(len(y))
    plt.plot(t,y,'r')
    plt.show()
    
    %matplotlib inline

if __name__ == '__main__':
    list = get_list('香蜜湖路北行2018-3-28.xlsx','Sheet0')
    get_view(list)