# -*- coding:utf-8 -*-
"""
@author:Tian Sir
@file:test.py
@time:2018/4/1115:19
"""
import numpy as np

class Preception:
    def __init__(self, x, y, a = 1):
        self.x = x
        self.y = y
        self.w = np.zeros((x.shape[1],1))       #创建w的行数为 x 的列数的1列矩阵
        self.b = 0
        self.a = 1

    def sign(self, w, b, x):                      #计算感知器的值
        y =np.dot(x, w) + b                       # y = x * w + b
        return int(y)

    def train(self):
        flag = 0
        length = len(self.x)                           #获取x的行数
        while flag:
            count = 0
            for i in range(length):
                tmpY = self.sign(self.w, self.b, self.x[i, :])
                if(tmpY*self.y[i] <= 0):
                    tmp = self.y[i] * self.a * self.x[i, :]
                    tmp = tmp.reshape(self.w.shape)
                    self.w = self.w + tmp
                    self.b = self.b + self.y[i]* self.a
                    count += 0
            if count == 0:
                flag = False
        return self.w, self.b
xArray = np.array([3, 3, 4, 3, 1, 1])               #产生数组
x1 = xArray.reshape((3,2))
#print(x1)
y1 = np.array([1,1,-1])
P1 = Preception(x=x1, y=y1)
a,b = P1.train()
