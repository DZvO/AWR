# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:58:10 2018

@author: Alex
"""

import random
import math
import numpy as np
random.seed(1)


def r_norm(µ, σ, tworet=False):
    U1 = random.random()
    U2 = random.random()
    x1 = math.sqrt(-2*math.log(U1))*math.sin(2*math.pi*U2)
    if tworet:
        x2 = math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)
        return (µ + σ*x1, µ + σ*x2)    
    return µ + σ*x1

def r_exp(λ):
    U = random.random()
    return -math.log(U)/λ

resultate = {}
for x in np.linspace(0, 10, 100):
    b = 10
    σ = 1.0
    wartezeit = []
    for i in range(10000):
        r = r_norm(b-x, σ)
        wz = b - r
        if r < 0: #vorherigen bus nehmen
            wz = -r
        wz = wz % b #auf bustakt mappen
        wartezeit.append(wz)
    
    resultate[x] = np.mean(wartezeit)
    print(str(x) + "  " + str(resultate[x]))

import matplotlib.pyplot as pl
lists = sorted(resultate.items())
x, y = zip(*lists)
pl.grid(color='grey')
pl.ylabel("durchschn. wartezeit")
pl.xlabel("geplant x min vor abfahrt")
pl.axis([-1, 11, 0, 9])
pl.plot(x, y)
pl.savefig("ausgabe1.svg", format="svg")

print()
print(min(resultate, key=resultate.get))
print(resultate[min(resultate, key=resultate.get)])