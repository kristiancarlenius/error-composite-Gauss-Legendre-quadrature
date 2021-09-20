# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:58:02 2021

@author: Kristian
"""
from numpy import *
from matplotlib.pyplot import *
from math import factorial
import matplotlib.pyplot as plt
newparams = {'figure.figsize': (8.0, 4.0), 'axes.grid': True,
'lines.markersize': 8, 'lines.linewidth': 2,
'font.size': 14}
plt.rcParams.update(newparams)
import math

def enminus(a, b, end, i):
        x1 = a + i*((b-a)/(end))
        x0 = a + (i-1)*((b-a)/(end))
        x12 = (x1+x0)/2
        h = (x1-x0)/6
        return h*(math.sqrt(1-(x0**2))+ 4*math.sqrt(1-(x12**2)) + math.sqrt(1-(x1**2)))

def tanexp(a, b, end, i):
        x1 = a + i*((b-a)/(end))
        x0 = a + (i-1)*((b-a)/(end))
        x12 = (x1+x0)/2
        h = (x1-x0)/6
        return h*(math.tan((math.pi*x0)/4) + 4*math.tan((math.pi*x12)/4) + math.tan((math.pi*x1)/4))

x = []
y = [4, 8, 16, 32, 64, 16384]
for k in y:
    print("oppgave b: antall m: ", k)
    x.clear()
    for i in range(k):
        x.append(tanexp(0, 1, k, i))
    print("oppgave b: summen: ", sum(x))
    print("oppgave b: feilmarginen: ", ((2*math.log(2))/math.pi) - sum(x))
    #print("sjekke", ((2*math.log(2))/math.pi))

print("\n")
x = []
y = [4, 8, 16, 32, 64, 16384]
for k in y:
    print("oppgave d: antall m: ", k)
    x.clear()
    for i in range(k):
        x.append(enminus(0, 1, k, i))
    print("oppgave d: summen: ", sum(x))
    print("oppgave d: feilmarginen: ", (math.pi/4) - sum(x))