"""
Sets - Множества
"""
# Сэты не принимают листы, только не изменяемые объекты. Integer, strings, кортежы. Unhashable это не хэшируемые объекты(изменяемые объекты), типа листов

# str_ = "python"
# sets = set(str_)
# print(sets)         # Из стрингов можно сделать сэт. Выведет по дной букве в сэт

"""
!!! Frozenset
"""

# seta = {"ss", (1, 2, 3, 4)}
# print(type(seta))
# frozen = frozenset(seta)
# print(frozen)

"""
!!! Функции
"""

# def add(x, y):
#     return x + y
# print(add(2, 5))      # Выйдет 7 (2+5)

# from lesson_5 import add    # Можно вызвать из другого питон файла таким образом. Т дальше уже просто вызывать обычным способом. Должно быть в одной директории (папке).

zarplata = [10000, 50000, 60000, 25000, 214521]
# dohod = sum(zarplata)
procent = 0.2
# pribyl = dohod - (dohod * procent)
# print(pribyl)


# def shop(list, procent):        # В скобках просто определяется что будет два элемента. Их название не                                    важно, главное прописать функцию снизу
#     dohod = sum(zarplata)
#     pribyl = dohod - (dohod * procent)
#     return  pribyl
#
#
# print(shop(zarplata, 0.2))

# def S(x,y):
#     s = x*y
#     return s
#
#
# print(f'Площадь равна - {S(5,4)} метров в квадрате')

# def hello_world(str):
#     print(f"hello {str}")
#
#
# print(hello_world("Nazik"))



# lists = [10, 18, 13, 3, 7]
# def factorial(x):
#     fact = []
#     for i in x:                   # Проходится по всем числам листа
#         counter = 1
#         for y in range(1, i+1):   # y равна числам с 1го до числа в в листе(i+1 потому-что i                                                  заканчивается на числе в листе -1)
#             counter = counter * y    # counter = 1 и умножается по всем числам в y(от 1 до числа в листе)
#         fact.append(counter)         # добавляет в fact
#     return fact                   # Делает факториал задаваемого листа
#
#
# print(factorial(lists))


# Задача 1

# height = int(input("Enter a height: "))
# width = int(input("Enter a width: "))
#
#
# def rect(x, y):
#     star = '*'
#     for i in range(x):
#         print(star * y)
#
#
# rect(height, width)


# Задача 2

# w = ['good', 'great', 'wow']
#
#
# def exclamation(list):
#     for i in range(len(list)):
#         list[i] = list[i] + '!'
#     print(list)
#
#
# exclamation(w)


# #Задача 3

# l = [1, 6, 5, 11, 10]
# n = 8
#
#
# def lesser(list, number):
#     l.sort()
#     least = []
#     for i in l:
#         if i < number:
#             least.append(i)     # Нужно было добавить лист чтобы выбрать последнюю цифру
#     print(least[-1])
#
#
# lesser(l, n)

# Задача 4
# Написать свою функцию len

