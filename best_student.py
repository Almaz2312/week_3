"""
Написать программу калькулятор оценок. Даны списки оценок с
предметами трех студентов. В каждом списке содержиться 7
предметов с оценками, необходимо сконвертировать в словарь и
найти средний балл оценок данных студентов. И выбрать лучшего
студента в группе.
Например:
ввод данных John = [[algebra“, 100], [„biologia“, 84], [„fizika“: 61]]
вывод: оценки

John   : {'algebra': 100, 'biologia': 84, 'fizika': 61}
Средний балл

John   : 81 балл
Лучшим студентом является: {имя студенто у которго больше всех
балл}
"""

Nurlan = [['Algebra', 95], ['Physics', 90], ['Biology', 89], ['Geometry', 95], ['History', 80], ['Chemistry', 82], ['P.E', 100]]
Nurlan_dict = {}
counter_nurlan = 0
Nurlan_av = 0
for i in range(len(Nurlan)):
    Nurlan_dict[Nurlan[i][0]] = Nurlan[i][1]
    counter_nurlan += Nurlan[i][1]
    Nurlan_av = counter_nurlan//len(Nurlan_dict)
print("Avarage of Nurlan's grades: ", Nurlan_av)


Aibek = [['Algebra', 85], ['Physics', 92], ['Biology', 79], ['Geometry', 75], ['History', 60], ['Chemistry', 62], ['P.E', 100]]
Aibek_dict = {}
counter_aibek = 0
Aibek_av = 0
for i in range(len(Aibek)):
    Aibek_dict[Aibek[i][0]] = Aibek[i][1]
    counter_aibek += Aibek[i][1]
    Aibek_av = counter_aibek//len(Aibek_dict)
print("Avarage of Aibek's grades: ", Aibek_av)

John = [['Algebra', 65], ['Physics', 50], ['Biology', 59], ['Geometry', 65], ['History', 51], ['Chemistry', 52], ['P.E', 100]]
John_dict = {}
counter_john = 0
John_av = 0
for i in range(len(John)):
    John_dict[John[i][0]] = John[i][1]
    counter_john += John[i][1]
    John_av = counter_john//len(John_dict)
print("Avarage of John's grades: ", John_av)

list_ = {}
list_['John'] = John_dict
list_['Nurlan'] = Nurlan_dict
list_['Aibek'] = Aibek_dict

print(list_)

if Nurlan_av > John_av and Nurlan_av > Aibek_av:
    print("Nurlan has the highest grade")
elif John_av > Nurlan_av and John_av > Aibek_av:
    print("John has the highest grade")
else:
    print("Aibek has the highest grade")