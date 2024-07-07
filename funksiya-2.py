# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:46:51 2024

@author: tursu
"""

# def foydalanuvchi_malumot(ism,familya,tugulgan_yil,email = '', tel_raqam = ''):
#     foydalanuvchi = {
#         'ism':ism,
#         'familya':familya,
#         'yoshi': f" 2024-{tugulgan_yil} ",
#         'tugulgan_yili':tugulgan_yil,
#         'email':email,
#         'telefon':tel_raqam
#         }
#     return foydalanuvchi 

# talaba = foydalanuvchi_malumot('Sherzod', 'Tursunov', 2002, tel_raqam= 906051775)
# print(f" foydalanuvchi haqida ma'lumotlar: {talaba} ")



def foydalanuvchi_malumot(ism,familya,tugulgan_yil,email = '', tel_raqam = ''):
    foydalanuvchi = {
        'ism':ism,
        'familya':familya,
        'yoshi': f" 2024-{tugulgan_yil} ",
        'tugulgan_yili':tugulgan_yil,
        'email':email,
        'telefon':tel_raqam
        }
    return foydalanuvchi 

while True:
    """Mijozlar haqida ma'lumot """
    mijozlar = []
    ismi = input("Ism kiriting:")
    familya = input("Familya kiriting:")
    tugulgan_yili = input("tug'ulgan yilini kiriting:")
    pochta = input("email kiriting:")
    telefoni = input("telefon raqam kiriting")
    
    mijozlar.append(foydalanuvchi_malumot(ismi,familya,tugulgan_yili, pochta,
                                          telefoni))
    key = input("Yana ma'lumot qo'shasizmi? (yes/no) ")
    if key == "no":
        break

for mijoz in mijozlar:
    print(mijozlar)






















