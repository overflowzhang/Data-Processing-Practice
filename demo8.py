# 灰度预测模型

import numpy as np
import math

if __name__ == '__main__':
    history_data = [2.874,3.278,3.337,3.390,3.679]
    n = len(history_data)
    X0 = np.array(history_data)
    print(n)
    print(X0)

    #累加生成
    history_data_agg = [sum(history_data[0:i+1]) for i in range(n)]
    X1 = np.array(history_data_agg)
    print('累加结果：',X1)

    #计算数据矩阵B和数据向量Y
    B = np.zeros([n-1,2])
    Y = np.zeros([n-1,1])
    for i in range(0,n-1):
        B[i][0] = -0.5*(X1[i] + X1[i+1])
        B[i][1] = 1
        Y[i][0] = X0[i+1]
    
    print('矩阵B:',B)
    print('矩阵Y：',Y)
    
    #计算GM(1,1)微分方程的参数a和u
    #A = np.zeros([2,1])
    A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
    a = A[0][0]
    u = A[1][0]
    print('微分方程参数 ：')
    print('a = ',a)
    print('u = ',u)
    
    #建立灰色预测模型
    XX0 = np.zeros(n)
    XX0[0] = X0[0]
    for i in range(1,n):
        XX0[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i));
    
    #模型精度的后验差检验
    e = 0      #求残差平均值
    for i in range(0,n):
        e += (X0[i] - XX0[i])
    e /= n
    print('模型精度的后验差检验：e = ',e)
    
    #求历史数据平均值
    aver = 0;     
    for i in range(0,n):
        aver += X0[i]
    aver /= n
    print('历史数据平均值：',aver)
    
    #求历史数据方差
    s12 = 0;     
    for i in range(0,n):
        s12 += (X0[i]-aver)**2;
    s12 /= n
    print('历史数据方差：',s12)

    #求残差方差
    s22 = 0;       
    for i in range(0,n):
        s22 += ((X0[i] - XX0[i]) - e)**2;
    s22 /= n
    print('残差方差：',s22)

    #求后验差比值
    C = s22 / s12   
    print('后验差比值：',C)

    #求小误差概率
    cout = 0
    for i in range(0,n):
        if abs((X0[i] - XX0[i]) - e) < 0.6754*math.sqrt(s12):
            cout = cout+1

    P = cout / n
    print('小误差概率：',P)

    if (C < 0.35 and P > 0.95):
        #预测精度为一级
        m = 10   #请输入需要预测的年数
        print('往后m负荷为：')
        f = np.zeros(m)
        for i in range(0,m):
            f[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i+n))
        print(f)
    else:
        print('灰色预测法不适用')