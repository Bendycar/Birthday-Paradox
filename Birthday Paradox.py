# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:58:22 2023

@author: bendc
"""
import random
import matplotlib.pyplot as plt

def birthday(people, trials):
    count = 0
    for i in range(trials):
        birthday_dict = {}
        for i in range(people):
            birthday_dict[i] = random.randint(1,365)
        if len(birthday_dict.values()) != len(set(birthday_dict.values())):
            count += 1
    
    return count / trials
    
x = [i for i in range(1,100)]
y = [birthday(n, 10000) for n in x] 


plt.figure(figsize=(5, 2.7))
plt.plot(x, y, label='Average')
plt.xlabel('Number of people')
plt.ylabel('P')
plt.title("Probability 2 people in a given room will share a birthday")
plt.legend()

    
    
