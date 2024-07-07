# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:26:30 2024

@author: tursu
"""
# amaliyot 1
buyurtma = []
n = 1
while True:
    savol = (f" iltimos {n}-buyurtmangizni kiriting \n>>")
    buyurtma1 = input(savol)
    buyurtma.append(buyurtma1)
    javob = input(f"yana buyurtma berasizmi (ha/yo'q)") 
    if javob != 'ha':
        break
    else:
        n+=1 
        continue
for k in buyurtma:
    print(f"sizning buyurtmalaringiz ro'yxati: {k}" )
    
    
 