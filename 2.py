# -*- coding: UTF-8 -*-
__author__ = "Zhao Zhicheng"

import numpy as np
import csv
import matplotlib.pyplot as plt

fig = 1

def pt(file_name):
    x = []
    y = []
    index = 0
    with open(file_name,'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if index == 0:
                index += 1
                pass
            else :
                x.append(row[0])
                y.append(row[1])
                pass
    
    
    plt.figure(fig)
    plt.plot(x,y,'red',linewidth = 3)
    plt.tilte(fig)
    plt.show()
    fig += 1
    return

pt('S parameter')
