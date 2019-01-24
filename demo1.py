# 三阶马尔科夫短时交通预测

import re
import pandas as pd
import numpy as np
from pylab import *

def get_list(name,sheet):
    list = []
    df = pd.read_excel(name,sheet)
    speed_max = 54.4                            # 通过excel得出的该路段一天中的最大速度
    
    for one in df['行程速度']:
        ratio = one / speed_max                 #行程速度占最大速度比值
        
        if ratio > 0 and ratio <= 0.1857:
            list.append(5)
        elif ratio > 0.1857 and ratio <= 0.3761:
            list.append(4)
        elif ratio > 0.3761 and ratio <= 0.5829:
            list.append(3)
        elif ratio > 0.5829 and ratio <= 0.7234:
            list.append(2)
        else:
            list.append(1)

    return list


def f():
    list = []

    for i in range(1,6):
        for j in range(1,6):
            for k in range(1,6):
                for m in range(1,6):
                    list.append([i,j,k,m])
    #print(list)
    return list


if __name__ == '__main__':
    list = get_list('traffic含最大速度比.xlsx','Sheet1')
    #print(size(list))
    #print(list)
    list2 = f()
    flag = 0
    m = [] 
    list_flag = [0,0,0,0,0]    #用来剔除掉全是零的情况
    list_a = []                #排列数
    list_b = []                #状态转移矩阵
    result = []
    for l in list2:
        count = 0
    
        flag += 1
        for i in range(0,664):
            if list[i:i+4] == l:
                count += 1
        #print(count)
        m.append(count)
        
        if flag % 5 == 0:
            result.append(m)
            m  = []
    
    for i in range(1,6):
        for j in range(1,6):
            for k in range(1,6):
                    list_a.append([i,j,k,'*'])
                    
    for i in range(0,125):
        
        if result[i] != list_flag:
            add = 0
            list_c = []    #概率列表
            print(list_a[i], ' ---> ' , result[i])
            for j in range(0,5):
                add += result[i][j]      #求出每行的和
            for k in range(0,5):
                list_c.append('%.4f' % (result[i][k]/add))    #计算每个数占总数的比值
            list_b.append(list_c)
    
    for b in list_b:
        print(b)