# print(True and False)       # Проверяет оба значения и в случае одного False, выводит False
# print(True or False)        # Хватает одного True, чтобы вывело True

# print(4.25 // 2)        # // Результат деления выводит на целое число, но в float формате, так как 4.25 float число

# x = 23
# num = 0 if x > 10 else 11      # Можно писать функцию if else на одной строке
# print(num)                # Выводит 0, так как х > 10

# !!!for

# strl = "abcde"
# for char in strl:       # Числа не итерабельны.
#     print(char)

# strl = "abcde"
# integer_ = 123
# bol = True
# l = [1,2,3,4,5]
# float_ = 12.01
# for char in float_:     # float_ не работает (not iterable float number), bol не работает (not iterable boolean), integer_ не работает (not iterable integer number). strl работает (iterable string). l аботает (iterable list),
#     print(char)

# !!! while (condition)

# num = 10
# while num < 20:
#     print(num)      # Принтует бесконечно
#
# num = 10
# while num < 20:
#     num += 1
#     print(num)      # Принтует с 11 до 20. Он прописал 20 так как после 19ти он добавил 1 и потом вывел и                     проверил что 20 не меньше 20 и остановился

# num = 10
# while num < 20:
#     print(num)        # Принтует с 10 до 19 так как print прописан до добавления. Он проверил что 20 не                           меньше 20 и остановился
#     num += 1

# n = 5
# while n < 10:
#     print("Samat")        # Принтует Samat  5 раз, пока n значение меньше 10 (с 5 до 9)
#     n += 1

# list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(list_)):
#     for y in range(len(list_[i])):
#         if i == y:
#             list_[i][y] = 0
# # print((list_[i]))             # Принтуте только последний лист
# #     print((list_[i]))         # Принтует 3 листа в столбик как iterable обьект
# #         print((list_[i]))     #Принтует по 3 раза каждый лист(i0,y0;i0,y1;i0,y2;i1,y0;i1,y1;i1,                                           y2;i2y0;i2,y1;i2,y2)

# for i in range(3):
#     print("i:", i)
#     for j in range(3):
#         print("j:", j)