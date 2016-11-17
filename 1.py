# -*- coding: UTF-8 -*-
__author__ = 'Zhao Zhicheng'

import numpy as np
from matplotlib import pyplot as plt
import openpyxl
import csv

index = 0
x = []
y = []
with open('S parameter.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if index == 0:
            index += 1
        else:
            x.append(row[0])
            y.append(row[1])
            index += 1
            pass
        pass
    pass

plt.figure(1)
plt.title('S Parameter',fontsize = 24)
plt.plot(x,y,'red',linewidth = 4)
plt.xlabel('Freq (GHz)')
plt.ylabel('S Parameter')
plt.show()

