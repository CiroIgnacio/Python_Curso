#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:29:19 2020

@author: ciro
"""

asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
for (keys, values) in asignaturas.items():
    print(f"{keys} tiene {values} créditos")