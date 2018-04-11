# -*- coding:utf-8 -*-
"""
@author:Tian Sir
@file:sensor.py
@time:2018/4/49:02
"""

import numpy as np

class Preception:
    def __init__(self, x, y, a = 1):
        self.x = x
        self.y = y
        self.w = np.zeros((x.shape[1], 1))
        self.b = 0
        self.a = 1

    def Sign(self,w, b, x):
        result = 0
        y = np.dot(x, w) + b
        return int(y)

    def Step(self):
        flag = True
        length = len(self.x)
        while flag:
            count = 0
            for i in range(length):
                print('i',i,'self.x[i,:]',self.x[i,:])
                y1 = self.Sign(self.w, self.b, self.x[i,:])
                print('count', count, 'i', i, 'x[]', self.x[i, :], 'tmpY', y1)

                if (y1 * self.y[i] <= 0):
                    w1 = self.a * self.y[i] * self.x[i,:]
                    w1 = w1.reshape(self.w.shape)
                    self.w = self.w + w1
                    self.b = self.b + self.a * self.y
                    count += 1
            if count == 0:
                flag = False
        return self.w, self.b,

data = [[3,3],[4,3],[1,1]]
xArray = np.array([3, 3, 4, 3, 1, 1])               #产生数组
x1 = xArray.reshape((3,2))
#print(x1)
y1 = np.array([1,1,-1])

P1 = Preception(x=x1, y=y1)
xn,yn =P1.Step()