#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:22:16 2020

@author: ciro
"""
#%%
word = input("Introduzca la palabra a adivinar: ")
word1 = word
user_inp = ''
c = 0
for i in range(len(word)):
    user_inp += '*'
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' + user_inp)
while user_inp != word:
    letter = input()
    user_inp = list(user_inp)
    word1 = list(word1)
    if letter in word1:
        for i in word1:
            if i == letter:
                index = word1.index(letter)
                word1[index] = '*'
                user_inp[index] = letter
        user_inp = "".join(user_inp)
        print(user_inp)       
        print("Acierto")
        
    else: 
        c += 1
        user_inp = "".join(user_inp)
        print(user_inp)
        print("Perdiste una vida")
    if c > 4:
        print("Perdiste") 
        break 

if user_inp == word:
    print("Ganaste")