# str = strings (alphanumeric/alphabetical/special char/numbers as text)
#                farhan123     haris          @amin&!       '23435'
# int = integers (numeric values)
#               12 55 1000  9999
# float = numeric values with decimal points
#               99.99  9.8 17.9 78.3
# Variables = it stores or contains any value i.e str, int, float
# contants = fixed values
# from itertools import count
# import math
# Name = 'Haris'
# Marks = 99
# Percentage = 99.0
# ================ input() ======================

# it takes the desired user input
# name = str(input('Enter your name: '))
# marks = int(input('Enter your marks: '))
# percentage = float(input('Enter your percentage: '))

# ============== print() ===================
# it gives the output of executed program
# print(name, marks, percentage)

# ===============  Syntax ===============
# it is the grammer of programming language
# this_is_programming_language = 123, 1123

# =============== Comments ===============
# we use hashtag # to write a comment which is ignored by python

# ================ Spacing ===================
# python is space sensitive because space is considered as character in python
# IndentationError

# ali = 10


# def sami(): print(123)


# # sami()
#
# # =============== Writing Strings ====================
# a = 'Farhan'
# print(a)
#
# name = "Bilal is a Good Boy"
# print(name)
#
# my_sent = "python is a programming language and it's easy to use"
# print(my_sent)
#
# my_sent2 = 'python is a programming language and it"s easy to use'
# print(my_sent2)
#
# my_sent3 = '''python is a programming language and it's easy to use'''
# print(my_sent3)
#
# my_sent4 = """python is a programming language and it"s easy to use"""
# print(my_sent4)

# my_para = """python is a programming language and
# it"s easy to use
# haris is comfortable with it"""
# print(my_para)
#
# my_para2 = '''this is fact that
# python is a programming language and
# it's easy to use
# haris is comfortable with it's working'''
# print(my_para2)
#
# my_para3 = "this is fact that \npython is a programming language and \nit's easy to use and \nharis is comfortable with it's working"
# print(my_para3)
#
# ================ Slicing Strings =======================

# index     01234567891123456789212345678931 # addressing
# greeting = 'Hello World Bilal Khuchru muchru'
# print(greeting)

# ============index to item==============
# print(greeting[0])
# print(greeting[6])
# print(greeting[10])
# print(greeting[23])
# [(starting point):(limit)] # limit = 10 stops at 9th index
# print(greeting[:])
# print(greeting[2:])
# print(greeting[:19])
# print(greeting[0:11])
# print(greeting[4:25])
#
# # ============item to index==============
# index()
# index     012345678910
# greeting = 'Hello World'
# print(greeting)
# print(greeting.index('W'))
# print(greeting.index('H'))
# print(greeting.index('ell'))
# print(greeting.index('ld'))

# =================== String Methods =======================

#           012345678910


# greeting = 'Hello Hello World'

# ============ count() ===========
# print(greeting.count('Hello'))
# print(greeting.count('World'))
# print(greeting.count('H'))
# print(greeting.count('o'))
# print(greeting.count('l'))
# print(greeting.count('world'))
# print(greeting.count('farhan'))

#           012345678910
# greeting = 'Hello World'
#
# ============ upper() ===========
# print(greeting.upper())
#
# #           012345678910
# greeting = 'Hello World'
#
# # ============ lower() ===========
# print(greeting.lower())

#           012345678910
# greeting = 'hello world my name is Amin'

# ============ capitalize() ===========

# print(greeting.capitalize())
#
# #         0123456789112345678921234567
# greeting = 'hello world my name is haris'

# ============ find() ===========
# print(greeting.find('haris'))
# print(greeting.find('hello'))
# print(greeting.find('my'))
#
# #         012345678911234567892123
# greeting = 'hello world my name is farhan'

# ============ index() ===========
# print(greeting.index('world'))
# print(greeting.index('is'))
# print(greeting.index('my'#))

# 012345678911234567892123
# greeting = 'hello world my name is farhan'

# # ============ replace() ===========
# print(greeting.replace('world', 'universe'))
# print(greeting.replace('is', 'to'))
# print(greeting.replace('my', 'your'))#
#
# # #         012345
# greeting = 'HARIS'

# # ============ join() ===========
# print('_'.join(greeting))
# print('|'.join(greeting))
# print('-'.join(greeting))
# print(' - '.join(greeting))
# print('+'.join(greeting))
# print(' . '.join(greeting))
#

# =========== Split() ==========
# greeting = 'HARIS'
# number = '45'
# print(greeting.split(' '))
# print(greeting.split('R'))
#
# print(greeting.isnumeric())
# print(number.isnumeric())

# ================== concatenation ===================
#name_1 = 'Haris and Amin '
#name_2 = 'Bilal and Usman'
#print(name_1+' '+name_2)
# print(name_1+name_2)

# ============ Formatting String ===================

# .format(), %s, f''

# name = str(input('Enter Your Name: '))
# age = int(input('Enter Your Age: '))
# ID = int(input('Enter Your ID: '))
# obtained_Marks = int(input('Enter Your Obtained Marks: '))
# percentage = math.floor((obtained_Marks/250)*100)
# print('--------------------\nReport Card\n--------------------\nHello {} \nYour Age: {} yrs \nYour Roll Number: {} \nObtained Marks: {} \nYour Percentage: {}%\n----------------------'.format(name, age, ID, obtained_Marks, percentage))
# print('%s is your name' % (name))

# print('----------\nReport Card\n---------------\nHello %s\nyour age: %s yrs\n your Roll Number: %s \n Obtained Marks: %s \nyour percentage: %s\n-------------------' % (name, age, ID, obtained_Marks, percentage))

#print(f'your name is {name} and percentage is {percentage}')

#print(f'--------------------\nReport Card\n--------------------\nHello {name} \nYour Age: {age} yrs \nYour Roll Number: {ID} \nObtained Marks: {obtained_Marks} \nYour Percentage: {percentage}%\n----------------------')

#print(f'My name is {name} \nI am {age} years old \nMy roll number is {ID} \nThe marks which I have obtained are {riobtained_Marks} \nMy obtained percentage is {percentage}% ')


# =================== Integers ============================
# str = strings (alphanumeric/alphabetical/special char/numbers as text)
#                farhan123     haris          @amin&!       '23435'
# int = integers (numeric values)
#               12 55 1000  9999
# float = numeric values with decimal points
#               99.99  9.8 17.9 78.3
# Variables = it stores or contains any value i.e str, int, float
# contants = fixed values

# my_number = int(input('Enter your number: '))
# print(my_number)
# print(type(my_number))
#
# my_float = float(input('Enter your number: '))
# print(my_float)
# print(type(my_float))

# my_complex = complex(input('Enter your number: '))
# print(my_complex)
# print(type(my_complex))

# ============== Arithmetic Operators================
# + - * /  //  **  %
# print(6+9)
# print(6-9)
# print(6*9)
# print(9/9)

# floor division
# print(6//9)
# print(81/9)
# print(81//9)

# power **
# print(5**2)
# print(5**3)
# print(9**2)
# print(2**5)
#
# # modulus %
# print(9 % 3)
# print(9 % 2)
# print(16 % 3)
# print(30 % 7)  # 30 =7*4=28+2 => 2

# =============== Assignment Operators =================
# += -= *= /= //= **= %= &= |= ^= >>= <<=
# a = 15
# a += 5
# print(a)

# b = 20
# b -= 10
# print(b)

# c = 5
# c *= 3
# print(c)

# d = 50
# d /= 5
# print(d)

# e = 66
# e //= 7
# print(e)

# f = 6
# f **= 2
# print(f)

# g = 50
# g %= 7
# print(g)
# myCount = '0000000000000000000000000000000000000000000000000000000000000000'
# print(myCount.count('0'))
# 0  0000
# 1  0001
# 2  0010
# 3  0011
# 4  0100
# 5  0101
# 6  0110
# 7  0111
# 8  1000
# 9  1001
# 10 1010
# 11 1011
# 12 1100
# 13 1101
# 14 1110
# 15 1111

# AND &= intersection/common
# 0.0=0 f.f=f
# 0.1=0 f.t=f
# 1.0=0 t.f=f
# 1.1=1 t.t=t

# h = 10  # 1010
# h &= 4  # 0100
# print(h)  # 0000 = 0

# i = 6   # 0110
# i &= 8  # 1000
# print(i)  # 0000 = 0

# j = 6   # 0110
# j &= 8  # 1000
# print(j)  # 0000 = 0

# k = 12   # 1100
# k &= 5   # 0101
# print(k)  # 0100 # ans 4

# OR |= union
# 0+0=0 f+f=f
# 0+1=1 f+t=t
# 1+0=1 t+f=t
# 1+1=1 t+t=t

# l = 7    # 0111
# l |= 8   # 1000
# print(l) # 1111 # ans 15

# XOR ^=
# 0+0=0 f+f=f
# 0+1=1 f+t=t
# 1+0=1 t+f=t
# 1+1=0 t+t=f

# m = 4    # 0100
# m ^= 9   # 1001
# print(m)  # 1101 # 13

# >>= (its name is Shift towards right)
# n = 10
# n >>= 2
# print(n)
#   ____
#   1010
#   --____
#     1010
#   --__
#   0010 = 2

# n = 10
# n >>= 3
# print(n)
#   ____
#   1010
#   ---____
#      1010
#   ---_
#   0001 = 1

# n = 15
# n >>= 1
# print(n)
#   ____
#   1111
#   -____
#    1111
#   -___
#   0111 = 7

# <<= (its name is shift towards left)
# o = 6
# o <<= 2
# print(o)
# converts to 8 bit code
# 00000110
# 00011000

# p = 10
# p <<= 3
# print(p)
# converts to 8 bit code
# 00001010
# 01010000

# ============== Comparisons Operators =================
# Equal to                  : ==
# Not Equals to             : !=
# Greater Than              : >
# Less Than                 : <
# Greater Than or Equals to : >=
# Less than or Equals to    : <=

# a = 5
# b = 6
# print(a == b)  # f
# print(a != b)  # t
# print(a > b)  # f
# print(a < b)  # t
# print(a >= b)  # f
# print(a <= b)  # t a<b a==b
#
# print(5 == 6)  # f
# print(5 != 6)  # t
# print(5 > 6)  # f
# print(5 < 6)  # t
# print(5 >= 6)  # f
# print(5 <= 6)  # t
#
# ============== Logical Operators =================
# AND
# ------------
# a . b = c
# ------------
# 0 . 0 = 0 f.f=f
# 1 . 0 = 0 t.f=f
# 0 . 1 = 0 f.t=f
# 1 . 1 = 1 t.t.t
# ------------
# my_number = 5
# print(my_number > 4 and my_number < 6)
# print(my_number > 4 and my_number == 6)

# OR
# ------------
# a + b = c
# ------------
# 0 + 0 = 0 f+f=f
# 1 + 0 = 1 t+f=t
# 0 + 1 = 1 f+t=t
# 1 + 1 = 1 t+t=t
# ------------
# my_number2 = 5
# print(my_number2 > 4 or my_number2 < 6)
# print(my_number2 > 4 or my_number2 == 6)
# print(my_number2 < 4 or my_number2 == 6)
# print(5 > 3 or 5 == 5)
# print(5 < 3 or 5 == 5)
# print(5 == 3 or 5 != 5)

# NOT
# a = b
# 1 = 0
# 0 = 1

# my_number3 = 5
# print(not my_number3)

# ============== Identity Operators =================
# is
# # is not
# a = 5
# b = 5
# print(a is b)
# print(a is not b)

# ============== Membership Operators =================
# in
# not in
# list = [1, 2, 3]
# print(1 in list)
# print(5 in list)
# print(5 not in list)
# print(3 not in list)
#
# ============== Bitwise Operators =================
# & AND
# print(1 & 6)
# print(1 & 1)
#
# # | OR
# print(1 | 6)
# print(1 | 1)
#
# # ^ XOR
# print(1 ^ 6)
# print(1 ^ 1)
#
# # ~ NOT
# print(~6)
# print(~1)
#
# # << Zero fill left shift
#
# # >> right shift
# #

# ================== Casting ================
# name = str(input('Enter your name: '))
# ID = int(input('Enter your ID: '))
# percentage = float(input('Enter your percentage: '))
# print(name)
# print(ID)
# print(percentage)

# ================== Booleans ================
# print(4 > 2)
# print(5 == 8)
# a = 'Hello World'
# print(bool(a))
# print(bool('Hello World'))
# b = 555
# print(bool(b))
# c = None
# print(bool(c))
#
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool({}))

# ================== Indexing ================
#         0  1  2  3  4  5  6  7  8  9  10
# numbers = 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(numbers.count(4))
# print(numbers.count(44))
# print(numbers.index(9))
# print(numbers.index(3))

# ================== Math Module ================

# print(math.sqrt(64))
# print(math.ceil(99.99))
# print(math.floor(99.99))
# print(math.pow(5, 3))
# print(math.floor(math.pow(5, 3)))
# print(math.ceil(math.pow(5, 3)))
# print(math.log(9988))
# print(math.exp(155))
# print(math.cos(155))
# print(math.sin(155))
# print(math.tan(155))
# print(math.degrees(155))
# print(math.radians(155))
# print(math.cos(155.556))


# ==================== arrays =====================

# EVERYTHING USED IN LISTS IS USED IN ARRAYS

# arrays are used for storing multiple values in a single variable

# from audioop import reverse
# from cgi import print_form


# array_1 = ['haris', 'bilal', 'farhan', 'amin', 'rehan']
# print(array_1)

# array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(array_2)

# array_3 = [1.5, 54.7, 7.7, 2.9]
# print(array_3)

# array_4 = [3j, 5j, 9j, 1j, 2j]
# print(array_4)

# array_5 = ['haris', 'bilal', 1, 2, 3, 2.5, 4.1, 8j, 9j]
# print(array_5)

# print(array_1, array_2, array_3, array_4, array_5)
# print(array_1+array_2+array_3+array_4+array_5)

#             0        1       2  3  4  5    6    7   8
# array_5 = ['haris', 'bilal', 1, 2, 3, 2.5, 4.1, 8j, 9j]
# print(array_5)

# print(array_5[6])

# Changing Index Item in Array

# array_5[6] = 'Haris Zuberi'
# print(array_5)
#
# array_5[0] = 'Amin Zuberi'
# print(array_5)

# length of list

# print(len(array_5))

# to add an item in  the list at last we use .append()
# array_5.append('Bilal Zuberi')
# print(array_5)

# array_5.pop()
# print(array_5)

# array_5.pop(1)
# print(array_5)

# array_5.remove(8j)
# print(array_5)

# array_6 = ['Haris', 'Bilal', 'Amin']
# array_5.extend(array_6)
# print(array_5)

# print(array_5+array_6)

# array_7 = array_6.copy()
# print(array_7)
# array_7 = array_6
# print(array_7)

# print(array_5.count('Haris'))
# print(array_5.count('Sami'))
# print(array_5.index('farhan'))

# array_6 = ['Haris', 'Bilal', 'Amin']
# array_6.insert(0, 'Haris Zuberi')
# print(array_6)

# array_6.insert(1, 'Haris Zuberi')
# print(array_6)

# array_6.reverse()
# print(array_6)

# array_6.sort()
# print(array_6)

# array_6.sort(reverse=True)
# print(array_6)

# ====================================== LISTS ============================================

# list1 = ['haris', 'amin', 'bilal', 'anas', 'ali']
# list2 = [100, 200, 300, 400, 500]
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, ]
# list4 = [1j, 2j, 3j, 4j, 5j, 6j]
# list5 = [True, False, None]

# print(list1, list2, list3, list4, list5)
# print(list1+list2+list3+list4+list5)

# ================= list to string ===================

# print('{}{}{}{}{}'.format(list1,list2,list3,list4,list5))
# print('{}'.format(list1+list2+list3+list4+list5))
#
# print('%s%s%s%s%s'%(list1,list2,list3,list4,list5))
# print('%s'%(list1+list2+list3+list4+list5))
#
# print(f'{list1}{list2}{list3}{list4}{list5}')
# print(f'{list1+list2+list3+list4+list5}')

# ================ Access items in the list =================

#           0         1       2  3  4  5
#           0        -5      -4 -3 -2 -1
# list1 = ['farhan', 'haris', 1, 2, 3, 9.99]
# print(list1[2])
# print(list1[0])
# print(list1[1])
# print(list1[-5])
# print(list1[-2])
# print(list1[-1])

# =================== Changing items in the list =============

#         0         1           2       3       4       5
# list2 = ['farhan', 'haris', 'bilal', 'amin', 'sami', 'ali']
# print(list2)
# list2[2] = 'hussain'
# print(list2)
# list2[1:4] = ['Amin', 'Sami', 'Ali']
# print(list2)
# list2[1:3] = ['Hassan']
# print(list2)

# =================== Adding items in the list =============

# there are three ways to add items in the list ( append, insert, extend)

# list3 = ['Amin', 'Sami', 'Ali', 'Haris']
# list4 = ['Farhan', 'Bilal', 'Kamran']
# list3.append('Hassan')
# print(list3)
# list3.insert(0, 'Hussain')
# print(list3)
# list3.extend(list4)
# print(list3)
# myTuple = (1, 2, 3)
# list3.extend(myTuple)
# print(list3)

# =================== Removing items from the list =============

# list5 = ['Amin', 'Sami', 'Ali', 'Haris', 'Farhan', 'Bilal', 'Kamran']

# list5.remove('Farhan')
# print(list5)

# list5.pop()
# print(list5)

# list5.pop(2)
# print(list5)

# del list5[1]
# print(list5)

# list5.clear()
# print(list5)

# del list5
# print(list5)

# # =================== Slicing List ====================

# =================== Index to Item ====================

#            0        1          2  3  4     5
#            0       -5         -4 -3 -2    -1
# myList = ['Ahmed', 'Abdullah', 4, 5, 21.0, 25.3]
# print(myList)
# print(myList[0])
# print(myList[4])
# print(myList[-1])
# print(myList[-4])
# print(myList[:])
# print(myList[1:])
# print(myList[2:5])
# print(myList[-5:-3])
#
# # =================== Item to Index ====================

# print(myList.index('Abdullah'))
# print(myList.index('Ahmed'))
# print(myList.index(5))

# =================== Changing items in the list =============

#         0         1           2       3       4       5
# list2 = ['farhan', 'haris', 'bilal', 'amin', 'sami', 'ali']
# print(list2)

# list2[2] = 'hussain'
# print(list2)

# list2[1:4] = ['Amin', 'Sami', 'Ali']
# print(list2)

# list2[1:3] = ['Hassan']
# print(list2)

# list2 = [100,200,300,400,500]
# list2[3] = 'Saami'
# print(list2)

# =================== Adding items in the list =============

#         0         1           2       3       4       5
# list3 = ['farhan', 'haris', 'bilal', 'amin', 'sami', 'ali']
# list4 = ['Audi', 'BMW', 'Mercedes']
# list3.append('BMW')
# print(list3)
# list3.insert(2,'Audi')
# print(list3)
# list3.extend(list4)
# print(list3)

# =================== removing items from the list =============

#         0         1           2       3       4       5
# list88 = ['farhan', 'haris', 'bilal', 'amin', 'sami', 'ali']
# print(list88)

# list88.remove('sami')
# print(list88)

# list88.pop()
# print(list88)

# list88.pop(1)
# print(list88)

# list88.clear()
# print(list88)

# del list88
# print(list88)

# =================== List Comprehension using Loops ==================================

# ============================= For Loop ===================================

# list99 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# for items in list99:
#     print(items)
#
# list99 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# for index in range(len(list99)):
#     print(index)

# list99 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# for haris in range(len(list99)):
#     print(haris)
#     print(list99[haris])
#     print(list99)

# ============================= While Loop ===================================

# list99 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# x = 0
# while x < len(list99):
#     print(list99[x])
#     x = x + 1

# =================================== List Comprehension ======================================

# list100 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# list101 = []
# for items in list100:
#     list101.append(items)
#     print(list101)

# list100 = ['Haris', 'Bilal', 'Amin', 'Farhan', 'Sami']
# list101 = [items for items in list100]
# print(list101)

# ========================== Tuples in Python ================================

# list1 = ['Haris', 'Amin', 'Bilal']  # mutable (it can be changed)
# tuple_1 = ('Haris', 'Amin', 'Bilal')  # immutable (it cant be changed)
# print(tuple_1)
# print(len(tuple_1))
# print(type(tuple_1))

# tuple_1 = ('Haris', 'Amin', 'Bilal')
# tuple_2 = (1, 2, 3)
# tuple_3 = (9.99, 5.5, 66.01)
# tuple_4 = (5j, 8j)
# tuple_5 = (True, False)
# tuple_6 = ('Haris', 1, 5.45, 9j, True)

# students = ['Haris', 'Amin', 'Bilal']
# classes = ('9th')
# Name = str(input('Enter Your Name: '))
# print(Name)

# ================ Tuple Formatting =================

# tuple_1 = ('Haris', 'Amin', 'Bilal')
# tuple_2 = (1, 2, 3)
# tuple_3 = (9.99, 5.5, 66.01)
# tuple_4 = (5j, 8j)
# tuple_5 = (True, False)

# print(tuple_1 + tuple_2 + tuple_3 + tuple_4 + tuple_5)  # joining tuples

# print('Tuple 1 is {}, Tuple 2 is {}, Tuple 3 is {}, Tuple 4 is {}, Tuple 5 is {},'.format(tuple_1, tuple_2, tuple_3, tuple_4, tuple_5))

# print('Tuple 1 is {},\nTuple 2 is {},\nTuple 3 is {},\nTuple 4 is {},\nTuple 5 is {},'.format(tuple_1, tuple_2, tuple_3, tuple_4, tuple_5))

# print('Tuple 1 is %s,\nTuple 2 is %s,\nTuple 3 is %s,\nTuple 4 is %s,\nTuple 5 is %s,' % (tuple_1, tuple_2, tuple_3, tuple_4, tuple_5))

# print(f'Tuple 1 is {tuple_1},\nTuple 2 is {tuple_2},\nTuple 3 is {tuple_3},\nTuple 4 is {tuple_4},\nTuple 5 is {tuple_5}')

# print('This is the main Tuple : {}'.format(tuple_1 + tuple_2 + tuple_3 + tuple_4 + tuple_5))

# ==================== Tuple Constructor ================

# myTuple = tuple(('Bilal', 'farhan', 'Haris'))
# print(myTuple)
