# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:16:40 2024

@author: tursu
"""
# mashina = ['merc', 'bmw', 'audi', 'GM']
# for car in mashina:
#     print('Hi ',car)

# sonlar = list(range(1,20,2))
# for son in sonlar:
#     print(f'{son}ning kubi {son**3} ga teng')

# the best teachers
# teachers = []
# print('Who is the best teachers in your school ? Please write teachers')
# for t in range(3):
#     teachers.append(input(f"Choose {t+1} teacher:"))
# print(teachers)

# sonlar = list(range(11))
# for son in sonlar:
#     if son == 2:
#         print(son**3)
#     else:
#         print(son**2)

# yosh = int(input('Yoshingizni kiriting \n>>>'))
# if yosh >= 18:
#     print('Xush kelibsiz')
# else:
#     print('Uzr jiyan hali yoshlik qilasan')

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car =='gm':
        print(car.upper())
    else:
        print(car.title())