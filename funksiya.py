# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:17:35 2024

@author: tursu
"""

# def ism_yosh_chiqar(ism, yosh):
#     """Foydalanuvchisini ism yoshini so'rab uning tug'ulgan yilini
#         chiqarib beryvchi dastur"""
#     print(f" Assalom Aleykum {ism.title()} siz {2024-yosh} yilda tug'ulgansiz ")
    
# ism_yosh_chiqar('sherzod' , 22)

# def sonning_kvadrati(son):
#     """foydalanuvchi kiritgan sonni kvadrati va kubini chiqarib beruvchi funksiya"""
#     print(f" {son} ning kvadrati {son**2}ga kubi esa {son**3}ga teng ")
# sonning_kvadrati(9)

def songa_qoldiqsiz(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
    sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya """
    a = list(range(2,11))
    for key in a:
        if son%key == 0:
            print(f" {son} {key}ga qoldiqsiz bo'linadi ")
        
            
songa_qoldiqsiz(20)