
'''Программа расчёта возраста по году рождения:'''
# import time
# from datetime import date

# current_year: int = date.today().year

# def calc_age(first_year: int, second_year: int):
#     result: int = first_year - second_year

#     if result <= -1:
#         result = -1

#     return result

# while True:
#     try:
#         user_year: int = int(input('Введите свой год рождения: '))
#     except:
#         print('Неправильный тип данных, введите ЦЕЛОЕ число')

#     else:
#         user_age: int = calc_age(current_year, user_year)
#         print(f'Ваш возраст: {user_age}')
#         time.sleep(0.8)


'''Программа расчёта площади треугольника по формуле Герона:'''
# import time
# from math import sqrt

# def get_square(a, b, c):
#     p = (a + b + c) / 2
#     s = sqrt(p*(p-a)*(p-b)*(p-c))
#     return s

# while True:
#     print('Введите длины сторон треугольника (с новой строки)')
#     try:
#         a = int(input())
#         b = int(input())
#         c = int(input())
#     except:
#         print('Неправильный тип данных, введите число')

#     else:
#         S = get_square(a, b, c)
#         print(f'Площадь треугольника равна {S} \n')
#         time.sleep(0.8)

'''Почему 0.1 + 0.2 != 0.3?'''
# Python использует стандарт IEEE 754, который хранит приближенные значения
# Например:
print(0.1 + 0.2)    # 0.30000000000000004

import math
print(0.1+0.2 == 0.3)               # False
print(math.isclose(0.1+0.2, 0.3))   # True