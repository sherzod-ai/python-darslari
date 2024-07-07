# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:48:18 2024

@author: tursu
"""
buxoriy = {
    'ism' :'Abu Abdulloh Ibn Ismoil',
    'tyil' : 810,
    'vyil': 870,
    'tjoy':'Buxoro'
    }

qodiriy = {
    'ism' : 'Abdulla Qodiriy',
    'tyil' : 1894,
    'vyil' : 1938,
    'tjoy' : 'Toshkent'
    }

vohidov = {
    'ism' : 'Erkin Vohidov',
    'tyil' : 1936,
    'vyil' : 2016,
    'tjoy' : "Farg'ona"
    }

navoiy = {
    'ism' : 'Alisher Navoiy',
    'tyil' : 1441,
    'vyil':1501,
    'tjoy':'Xirot'
    }

insonlar = [buxoriy, qodiriy, vohidov, navoiy]
for inson in insonlar:
    print(f" {inson['ism'].title()}, ",
          f" tug'ulgan yili: {inson['tyil']} ",
          f" tug'ulgan joyi: {inson['tjoy']}"   )














