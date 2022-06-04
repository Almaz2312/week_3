# !!! list comprehensions - генераторы списков

# list_a = []
# for i in range(1, 101):
#     list_a.append(i)
# print(list_a)

# list_b = [i**2 for i in range(1,101)]  # Создаёт лист от 1 до 100 и возводит их в квадрат
# print(list_b)

# lists_numbers = [1024, 4, 36]
# list_b = [i**2 for i in range(1, 101) if i in lists_numbers]    #Выводит номера входящие в lists_numbers                                                                возведённый в квыдрат
# print(list_b)   #Выводит 16, 1296. 4 и 36 в квадрате, т.к эти числа есть в обоих списках

# string_list = ["banana", "pineapple", "apple", "orange"]
# lists_c = [i for i in string_list if i.endswith('e')]     # endswith выбирает последнюю букву
# ap_list = [i for i in string_list if i.startswith('ap')]    # startswith выбирает первые буквы
# print(ap_list)

# import math
# lists = [math.sqrt(i) for i in range(1, 60)]    #Получаю квадратный корень всех чисел
# print(lists)

# from datetime import datetime
# before = datetime.now()
# lists = []
# for i in range(1, 10000):
#     lists.append(i)
# after = datetime.now() - before
# print(after, "loop")
# b = datetime.now()
# list_comp = [i for i in range(1, 10000)]    # Вычисляет быстрее чем когда цикл отдельно прописан
# af = datetime.now() - b
# print(af, "list_comp")

# numbers_ = ['+996555123345', '+996555124235', '+996700123234', '+996700124235', '+996777123234', '+996777124235']
# megacom = [i for i in numbers_ if i.startswith('+996555')]
# beeline = [i for i in numbers_ if i.startswith('+996777')]
# o = [i for i in numbers_ if i.startswith('+996700')]
# print('Megacom:', megacom, '; Beeline:', beeline, '; O:', o)    # Принтует переменную и после список

# numbers_ = ['+996555123345', '+996555124235', '+996700123234', '+996700124235', '+996777123234', '+996777124235']
# megacom = ['Megacom: ' + i for i in numbers_ if i.startswith('+996555')]    # Прописывем строку и +
# beeline = [f'Beeline: {i}' for i in numbers_ if i.startswith('+996777')]    # Пишем строку через f'                                                                                   вместо i
# o = ["O!: {0}".format(i) for i in numbers_ if i.startswith('+996700')]      #В {0} вставляет i
# print(megacom, beeline, o)

## Задача 1

# products = {}
# for i in range(5):
#     product_name = input("Enter a product name: ")
#     product_price = input("Enter a price: ")
#     products[product_name] = f'{product_price}$'
# print(products)

## Задача 2

# username = input("Username: ")
# password = input("Password: ")
# users = {1: {username: 'Almaz',
#              password: 'qwerty1'},
#          2: {username: 'Ermek',
#              password: 'qwerty2'},
#          3: {username: 'Talgat',
#              password: 'qwerty3'},
#          4: {username: 'Marat',
#              password: 'qwerty4'},
#          5: {username: 'Murat',
#              password: 'qwerty5'}
#          }
#
# for i in users:
#     if users[i][username] == username and users[i][password] == password:
#         print("Добро пожаловать")
#     else:
#         print("Не верный пароль или логин")
# """Здесь проверяет все 5 циклов и сверяет с каждым, выводит 5 циклов и 4 из них выходят не правильный. А на тот цикл на который приходится правильным принимает его"""


users = {1: {'username': 'Almaz',
             'password': 'qwerty1'},
         2: {'username': 'Ermek',
             'password': 'qwerty2'},
         3: {'username': 'Talgat',
             'password': 'qwerty3'},
         4: {'username': 'Marat',
             'password': 'qwerty4'},
         5: {'username': 'Murat',
             'password': 'qwerty5'}
         }
username = input("Username: ")
password = input("Password: ")
message = ""
for i in users:
    if username in users[i].values():
        if password == users[i]['password']:
            message = 'Successfully logged in'
            break
        else:
            message = 'Incorrect password'
            break
    else:
        message = 'User not found'
print(message)




## Задача 3