#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:22:16 2020

@author: ciro
"""
#%%
import random
import unicodedata
def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

Word_file = "/home/ciro/Desktop/Ciro/Programacion/Python/Python_Curso/dict/Untitled Document 1"
WORDS = open(Word_file).read().splitlines()
play = 'Y'
computer = 0
player = 0
while play == 'Y':
    word = random.choice(WORDS).lower()
    word = elimina_tildes(word)
    word1 = word
    user_inp = ''
    c = 0
    letters = []
    for i in range(len(word)):
        if word[i] == ' ':
            user_inp += ' '
        else:
            user_inp += '*'
    print(user_inp)
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
            
        else: 
            c += 1
            user_inp = "".join(user_inp)
            print(user_inp)
        # Info user
        letters.append(letter)
        print("Letras usadas:", end = " ")
        for i in letters:
            print(i, end = "-")
        print(f"\nVidas restantes: {5-c}")
        if c > 4:
            computer += 1
            print("Perdiste") 
            break 
        

    if user_inp == word:
        player += 1
        print("Ganaste")
    print(f"La palabra era: {word}")
    print(f"SCORE\nComputer: {computer}\nPlayer: {player}")
    play = input('Do you want to play again? (Y/N): ').upper()
