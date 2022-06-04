"""
Найдите три ключа с самыми высокими значениями в
словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
после чего эти ключи сохраните в какой либо переменной и удалите
из предыдущего словаря
"""

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
highest3 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
for i in highest3:
    del my_dict[i]
print(my_dict)
print(highest3)