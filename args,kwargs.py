# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:22:17 2024

@author: tursu
"""

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def multiple(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma

# print(multiple(2,2,3))

# Talaba haqida ma'lumot

# def talaba(ism,familya,**malumotlar):
#     malumotlar['ism']=ism
#     malumotlar['familya']=familya
#     return malumotlar
# talaba1 = talaba('sherzod', 'tursunov', yoshi =22, tugulgan_joy= 'Samarqand')
# talaba2 = talaba('diyor', 'hakimov', yoshi=23, tel_raqam=998906051775)
# print('talabalar haqida malumot:')
# print(talaba1)