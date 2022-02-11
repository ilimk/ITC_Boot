# Problem0
# a1 = (1, 2, 3, 4)
# a2 = (5, 6, 7, 8)
# a3 = (9, 10, 11, 12)
# a4 = (13, 14, 15, 16)
# a5 = (17, 18, 19, 20)
# a_list = []
# a_list.append(a1)
# a_list.append(a2)
# a_list.append(a3)
# a_list.append(a4)
# a_list.append(a5)
# print(a_list)

# print(a_list)


# Problem1

# a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# print(a_tuple[0: len(a_tuple): 1])

# Problem2
# a = []
# a.append('Ilim')
# a.append(1996)
# a.append(True)
# a.append(14.2)
# a.append(('1996-05-14'))
# print(a)

#Proble3
# a = ['rthrth','hrthrt','trhrth','trhrt']
#
# b = ','
#
# print(len(b.join(a)))
# print(b.join(a))


# Problem4
# a = []
# b = []
# a.append('ilim')
# a.append('nur')
# a.append('tima')
# a.append('urik')
# a.append('edik')
#
# b.append(1)
# b.append(2)
# b.append(3)
# b.append(4)
#
# print(a)
# print(b)
#
# print(a.extend(b))
# problem4
# a = [23,27.93,'mura', 'itc']
# b = [100, 123.56,'grgr','egre']
# a.extend(b)
# print(a)

# Problem5
# names = ['Jack', 'Oskar', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# print(names.count('Jack'))

# Problem6
# print('count of Oskar :', names.count('Oskar'))
# names.remove('Oskar')
# print('count of Oskar :', names.count('Oskar'))
# print(names.count('Oskar'))

#Problem7

# a = []
#
# a.append('Ilim')
# a.append('1996-05-14')
# a.append('I love Python!!!')
# print(a)

#Problem8
# PythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# print(PythonList)
# PythonList.pop(PythonList.index('loop'))
# print(PythonList)
#Problem9
# numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# print(n[0]*n[1]*n[2])

# print(numbers[1:5:1])

# a.extend(numbers)





#Problem10
numbers = []
letters = []
#
# # numbers
#
# #Proble10
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
if type(spisok_1[0]) == 'int':
    letters.append(spisok_1[0])
if type(spisok_1[0]) == 'str':
    numbers.append(spisok_1[0])

if type(spisok_1[1]) == 'int':
    letters.append(spisok_1[1])
if type(spisok_1[1]) == 'str':
    numbers.append(spisok_1[1])
if type(spisok_1[2]) == 'int':
    letters.append(spisok_1[2])
if type(spisok_1[2]) == 'str':
    numbers.append(spisok_1[3])
if type(spisok_1[3]) == 'int':
    letters.append(spisok_1[3])
if type(spisok_1[3]) == 'str':
    numbers.append(spisok_1[4])
if type(spisok_1[4]) == 'int':
    letters.append(spisok_1[4])
if type(spisok_1[5]) == 'str':
    numbers.append(spisok_1[5])
if type(spisok_1[5]) == 'int':
    letters.append(spisok_1[6])
if type(spisok_1[6]) == 'str':
    numbers.append(spisok_1[6])
if type(spisok_1[6]) == 'int':
    letters.append(spisok_1[7])
if type(spisok_1[7]) == 'str':
    numbers.append(spisok_1[7])

if type(spisok_1[3]) == str:
    print('fdgd')

print(numbers)

#pROBLEM11
# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# print(pythonList[1:3])