"""
# !!! dict_comprehesions
"""

# dict_comp = {i: i**2 for i in range(1, 11)}
# print(dict_comp)

# dollars_2019 = {'35': 209.7, '15': 69.7, '1005': 6970}
# dollar = 84.5 - 69.7
# dollars_2022 = {i:y+dollar for i,y in dollars_2019.items()}
# print(dollars_2022)

# dollars_2019 = {35: 209.7, 15: 69.7, 1005: 6970}
# dollar = 84.5
# dollars_2022 = {i: i * dollar for i in dollars_2019}
# print(dollars_2022)

# dollars_2019 = {3: 209.7, 1: 69.7, 100: 6970}
# for values in dollars_2019.values():
#     print(values)

# dollars_2019 = {3: 209.7, 1: 69.7, 100: 6970}
# gte_ = {key:value for key, value in dollars_2019.items() if 100 < value < 5000}
# print(gte_)

# lists = [1, 1, 4, 3, 6, 8, 6]
# for i in lists:
#     if lists.count(i) > 1:
#         lists.remove(i)
# print(lists)
# print(set(lists).intersection(lists))     #Делает тоже самое что сверху, но одной строкой
# print(set(lists))           # Делает тоже самое что сверху, но ещё проще


"""
# !!!Set Множества
"""

#Пишется также как и словарь, но нету ключей и значений

# sets = {1, 1, 3, 3, 5, 6, 7}
# # print(sets))
# # for i in sets:
# #     print(i)

# sets = {1, 1, 3, 3, 5, 6, 7}
# set1 = {'a', 'b'}
# set2 = {2, 5, 7}
# sets.update(set1)   # Объединяет списки в sets
# a = sets.union(set2, set1)
# print(sets)     # Выведет объединённый список
# print(set1)     # Выведет только set1
# print(a)        # Выведет объединённый список в рандомном порядке

# sets = {1, 1, 3, 3, 5, 6, 7}
# set1 = {'a', 'b'}
# set2 = {2, 5, 7}
# print(sets.isdisjoint(set1))    # isdisjoint выходит True в случае если сэты не пересекаются,
                                # если есть похожие элементы выйдет False

# sets = {1, 1, 3, 3, 5, 6, 7}
# set1 = {'a', 'b'}
# set2 = {2, 5, 7}
# if sets.isdisjoint(set1):       # Если нет похожих элементов выйдет True
#     sets.update(set1)           # Объединяет списки
# print(sets)     # Выведет объединённый список

# sets = {1, 1, 3, 3, 5, 6, 7}
# set1 = {2, 5, 7}
# # a = sets.difference(set1)     # Выводит разницу из списка sets
# # print(a)                      # Выведет {1, 3, 6}
# print(sets.difference(set1))    # Выводит разницу из списка sets

# print(sets.symmetric_difference(set1))  # Выводит разницу из сэтов
# print(sets.intersection(set1))            # Выводит схожие элементы из сэтов


# sets = {1, 1, 3, 3, 5, 6, 7}
# set1 = {2, 5, 7}
# sets.symmetric_difference_update(set1)      # Меняет sets сэт на числа которые не пересекаются в обоих                                                  списках
# print(sets)
