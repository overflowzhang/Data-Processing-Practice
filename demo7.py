#浮动车数据处理
#将其坐标显示在画布上

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

def get_list(name,sheet):
    df = pd.read_excel(name,sheet)
    print(df.count())
    count = df['经度'].count()
    x = df['经度']
    y = df['纬度']
    s = df['速度']
    plt.figure(dpi = 300)
    for i in range(0,count):
        if s[i] <= 20:
            plt.scatter(x[i],y[i],s=0.5,c = 'c')
        if s[i] > 20 and s[i] <= 40:
            plt.scatter(x[i],y[i],s=0.5,c = 'g')
        if s[i] > 40 and s[i] <= 60:
            plt.scatter(x[i],y[i],s=0.5,c = 'b')
        if s[i] > 60 and s[i] <= 80:
            plt.scatter(x[i],y[i],s=0.5,c = 'm')
        if s[i] > 80:
            plt.scatter(x[i],y[i],s=0.5,c = 'r')

    plt.show()
    %matplotlib inline
       
if __name__ == '__main__':
    
    get_list('浮动车3-25.xlsx','Sheet0')