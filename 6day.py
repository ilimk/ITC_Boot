#Problem0
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,7}
# dates_of_birth.remove(7)
# print(dates_of_birth)
#Problem1
# dates_of_birth = {"dog", 3,10,11,13,31,21,1,10,3,5,6,6}
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# print(dates_of_birth.intersection(farm_1))
#Problem2
# set № 1:
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
#
# # set № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
#
# # set 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#
# print(farm_2.difference(farm_1))
# Proble3
# a = {1,2,3,4,5}
# a.add(6)
# print(a)
# a.pop()
# print(a)
# Problem 000
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({'beshbarmak': 130})
# print(menu)
# menu['lagman'] = 135
# print(menu)
#Problem10
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu.update({'drinks': ['Coca-Cola', 'Sprite', 'Fanta']})
# print(menu)
# Problem 10
# sett = {'add', 'update', 'intersection', 'remove', 'difference', 'intersection_update', 'clear', 'discard', 'pop'}
# print('sets', sett)
# dictionaryy = {'clear', 'get', 'keys', 'values', 'items', 'update'}
# print('dictionaryy ', dictionaryy )
# print(sett.intersection(dictionaryy))
#Problem 31
# a = {}
# print(a)
# for i in range(3):
#     a.update({input('Введите имя'): input('Введите пароль')})
# print(a)
#Problem 27

# a = {'Ilim': 'SQL Developer', 'Azat' : 'Pythonist', 'Tima': 'JavaScripter', 'Ilyas': 'DevOps', 'Vlad': 'Lan Spec'}
# for i in a:
# print('Здравствуйте :', i , 'Прекрасная профессия :',  a[i])
# problem 22
# b = {}
# a = set(b)
# # print(type(set(a))
# for i in range(10):
#     a.add(input('Пишите только число!!!'))
# print(tuple(a))
#Problem 11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# print(list(set(south_american_countries)).count('Suriname'))
#Problem 101
# suit_case = []
# for i in range(5):
#     suit_case.append(input(f'Вещь номер : {i}'))
# print(suit_case)
# suit_case.pop()
# print(suit_case)
#Problem 001
# # set1
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# #Set2
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1.intersection(farm_2))
#Problem 100
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1_list = list(farm_1)
farm_2_list = list(farm_2)
diff = []
print(farm_2.difference(farm_1))
for i in farm_1_list:
    for j in farm_2_list:
        if i == j:
            diff.append(j)

for i in diff:
    farm_2_list.remove(i)
print(farm_1)
print(farm_2)
print(farm_2_list)
# if 'ilim' == 'ilim':
#     print('ilim')