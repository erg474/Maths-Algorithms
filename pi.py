# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:21:15 2021

@author: euan.gethin
"""

from mpmath import mp
import time

mp.dps = 1000000
pi = list(str(mp.pi))

    
for i in range(1,1000):
    print(pi[i])
    time.sleep(0.05)

    