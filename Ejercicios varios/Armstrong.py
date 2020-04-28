#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:23:04 2020

@author: ciro
"""

# Números Armstrong

def is_Armstrong(num):
    length = len(str(num))
    total = 0
    for i in range(length):
        total += int(str(num)[i])**length
    if total == num:
        result = True
    else:
        result = False
    return result
43
try:
    num = int(input("Enter a number: "))
    
    if is_Armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} isn't an Armstrong number")
except ValueError:
    print("Only numbers are allowed")