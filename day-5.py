# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 22:21:08 2024

@author: tursu
"""
# sinf = int(input('nechanchi sinfda o\'qiysiz ? \n>>> '))
# if sinf <= 4:
#     price = 10000
# elif sinf <= 8:
#     price = 15000
# else:
#     price = 20000
# print(f'siz uchun bilet narxi {price} ming so\'m')

# amaliyot 1
# son = int(input('iltimos juft son kiriting \n>>>'))
# if son % 2 == 0:
#     print('Rahmat')
# else:
#     print('bu toq son')

# amaliyot 2
# son1 = int(input('iltimos ikkita son kiriting \n >>>'))
# son2 = int(input('ikkinchi son >>>'))
# if son1 > son2 :
#     print(f'{son1} {son2}dan katta')
# elif son2 < son1:
#     print(f'{son2} {son1}dan katta')
# else: print('bu ikki son teng')

# amaliyot 3
# mahsulotlar = ['sichqoncha', 'klaviatura', 'monitor', 'keys', 'kalonka', 'fleshka',
#             'hdd', 'web-camera', 'protsessor', 'kabel']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni kiriting \n>>>'))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'do\'konimizda {mahsulot} bor')
#     else:
#         print(f'do\'konimizda {mahsulot} yo\'q')

# amaliyot 4
foydalanuvchilar = ['sherzod', 'bek', 'shaxzod', 'diyorbek', 'daler']
login = input('yangi login kiriting \n>')
if login.lower() not in foydalanuvchilar:
    print('Login qabul qilindi')
else:
    print('bu login band boshqa login tanlang')
