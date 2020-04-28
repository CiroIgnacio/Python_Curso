#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:19:40 2020

@author: ciro
"""

v1 = [1, 2, 3]
v2 = [-1, 0, 2]

prodEscalar1 = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]  # Forma 1
prodEscalar = 0

for i in range(3):  # Forma 2
    prod = v1[i]*v2[i]
    prodEscalar += prod

print(prodEscalar)
print(prodEscalar1)