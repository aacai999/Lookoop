# coding:UTF-8
# 2018-10-25
# https://blog.csdn.net/zchshhh/article/details/78215087

import numpy as np 
from regression import *
from threshed import loadData
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def getThreshed(file):
    """
    从数据集中获得标准阈值
    """
    pass


if __name__ == '__main__':
    print("loading data ...")
    feature, label = loadData("new_daaaa.txt")
    # 训练
    print ("traing...")
    method = ""  # 选择的方法
    if method == "bfgs":  # 选择BFGS训练模型
        print("using BFGS...")
        w0 = bfgs(feature, label, 0.5, 50, 0.4, 0.55)
    elif method == "lbfgs":  # 选择L-BFGS训练模型
        print("using L-BFGS...")
        w0 = lbfgs(feature, label, 0.5, 50, m=20)
    else:  # 使用最小二乘的方法
        print("using LMS...")
        w0 = ridgeRegression(feature, label, 0.5)

    a_x = []
    for i in label:
        a_x.append(int(i))
    a_y = a_x # a_x.copy()
    # 得到预测值
    predition = getPrediction(feature, w0)
    y = []
    for i in predition:
        y.append(i[0])
    x = y # y.copy()
    color = np.arctan2(y, x)
    print(len(x))
    # 绘制散点图
    plt.scatter(x, y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim((20, 30))
    plt.ylim((20, 30))

    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(a_x, a_y)
    plt.savefig('result')
    plt.show()


