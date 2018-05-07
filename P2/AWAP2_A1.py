# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:47:08 2018

@author: Alex
"""
import random
import math
random.seed(1)


def r_norm(µ, σ, tworet=False):
    U1 = 1 - random.random()
    U2 = 1 - random.random()
    x1 = math.sqrt(-2*math.log(U1))*math.sin(2*math.pi*U2)
    if tworet:
        x2 = math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)
        return (µ + σ*x1, µ + σ*x2)    
    return µ + σ*x1

def r_exp(λ):
    U = 1 - random.random()
    return -math.log(U)/λ

werte = []
for i in range(1000000):
    w = r_exp(1)
    #w = r_norm(0, 1)
    werte.append(w)
    
import numpy as np
from matplotlib import pyplot as pl
pl.grid()
pl.axis([-6, 6, 0, 2.25])
pl.title("N=" + str(len(werte)))
pl.hist(werte, 100, density=True)
pl.savefig("ausgabe1.svg", format="svg")
