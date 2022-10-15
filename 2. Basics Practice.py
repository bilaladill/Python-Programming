# ============================================== STRINGS ==================================================

# ===============Input===============
# bi
# name = str(input('Enter your name: '))
# age = int(input('Enter your age: '))
# marks = int(input('Enter your marks: '))
# percentage = float(input('Enter your percentage: '))
# print(name, age, marks, percentage)

# ha

# Name = str(input('Enter your name: '))
# Class = int(input('Enter your class: '))
# RollNo = int(input('Enter your RollNo: '))
# Marks = int(input('Enter your Marks: '))
# Percentage = int(input('Enter your Percentage: '))
# print(Name, Class, Marks, Percentage)

# ============== writing strings ======================

# bil
# a = 'bilal'
# print(a)

# har
# a = 'haris'
# print(a)

# bil
# name = 'bilal is a good boy'
# print(name)

# har
# Percentage = 'My perc is as good as my perc of matric'
# print(Percentage)

# bil
# mySent = "Python is a programming language and it's easy to use"
# print(mySent)

# har
# Whats_your_Name = 'Enter your name:Haris '
# print(Whats_your_Name)

# bil
# myPara = """haris is a good boy
# bilal is a good boy
# amin is a good boy"""
# print(myPara)

# har
# myPara = """There are Three Best python programmer
# Haris
# Amin
# Bilal
# In The Town"""
# print(myPara)

# ==================== slicing strings =================

# bil
# index =     01234567891123456789
# greeting = 'hello world im bilal'
# print(greeting)

# ================= index to item ===============

# bil
# print(greeting[8])
# print(greeting[18])
# print(greeting[15])
# print(greeting[:9])
# print(greeting[:])

# ================ item to index =================

# bil
# print(greeting.index('i'))
# print(greeting.index('bila'))

# ======================== String method ================================

# greeting = "hello beautiful beautiful people i'm bilal bilal bilal"

# ========================== counting =======================

# print(greeting.count('bilal'))
# print(greeting.count('beautiful'))
# print(greeting.count('hello'))
# print(greeting.count('l'))
# print(greeting.count('i'))

# ======================= upper() / lower() ================

# index =      01234567891
# greeting1 = 'hello world'
# greeting2 = 'HELLO WORLD'
# greeting3 = 'HEllo wOrld I aM bilAL anD i am 19 YEars olD'

# print(greeting1.upper())
# print(greeting2.lower())
# print(greeting3.upper())
# print(greeting3.lower())

# ============== capitalize ===================

# greeting = 'hello moto'
# print(greeting.capitalize())

# ============== find =====================

# index =     01234567891123456789012345678901234567890123456789
# greeting = 'hello world my name is bilal and i live in karachi'
# print(greeting.find('world'))
# print(greeting.find('karachi'))

# ================== index ====================

# greeting = 'hello world my name is bilal and i live in karachi'
# print(greeting.index('my'))

# =================== replace =====================

# print(greeting.replace('hello', 'hey'))
# print(greeting.replace('bilal', 'haris'))
# print(greeting.replace('karachi', 'lahore'))

# ================== join ==========================

# greeting = 'tomato ketchup'
# print('_'.join(greeting))
# print('-'.join(greeting))
# print(' - '.join(greeting))
# print('.'.join(greeting))
# print('+'.join(greeting))

# ==================== split ===================

# name = 'bilal'
# number = '36'
# print(name.split('l'))
# print(name.split('a'))
# print(name.split('i'))

# 'isnumeric tells whether the value we are asking for is a numeric value or not. So it answers in true or false.'

# print(number.isnumeric())
# print(name.isnumeric())

# =================== concatination ========================

# sent_1 = 'Haris and amin are brothers.'
# sent_2 = 'They both live in the same house.'
# sent_3 = 'Their grandmother also lives with them.'
# print(sent_1+' '+sent_2)
# print(sent_1+' '+sent_2+' '+sent_3)
# print(sent_1+' '+sent_3)

# ====================== formatting string ==========================

# ===== .format method =====

# import math
# name = str(input('Enter your name: '))
# age = int(input('Enter your age: '))
# id = int(input('Enter your id: '))
# total_marks = int(input('Enter your total marks: '))
# obtainedMarks = int(input('Enter your obtained marks: '))
# percentage = math.floor((obtainedMarks/total_marks)*100)
# print("Hello {} you are {} years old. Your roll no. is {}. The total marks of the test were {} and you have obtained {}. So your percentage is {}%".format(name, age, id, total_marks, obtainedMarks, percentage))

# ===== %s method =====

# print("I am %s. I am %s years old. My id is %s. My total marks were %s and I have obtained %s marks. So my percentage is %s." %(name, age, id, total_marks, obtainedMarks, percentage))

# ===== f'' method =====

# print(f'Hello {name}. \nYour age is {age} years. \nYour roll number is {id}. \nThe total marks were {total_marks}. \nYou have obtained {obtainedMarks} marks. \nYour percentage is {percentage}%')


# ========================================= INTEGERS ================================================

# str = strings (alphanumeric/alphabetical/special char/numbers as text)
#                farhan123     haris          @amin&!       '23435'
# int = integers (numeric values)
#               12 55 1000  9999
# float = numeric values with decimal points
#               99.99  9.8 17.9 78.3
# Variables = it stores or contains any value i.e str, int, float
# contants = fixed values

# ================== type ======================

# number = int(input('enter your number: '))
# print(number)
# print(type(number))

# float = float(input('enter your float: '))
# print(float)
# print(type(float))

# complex = complex(input('enter your number: '))
# print(complex)
# print(type(complex))

# ========================= arithmetic operators =====================

#  ( +, -, *, /, //, **, % )

# print(8+9)
# print(19+63)

# print(53-7)
# print(78-43)

# print(7*3)
# print(82*2)

# print(49/7)
# print(54/6)

# // means floor division

# print(36//7)
# print(81//8)

# ** means multiplying by the given power

# print(8**8)
# print(2**6)

# % means modulus

# print(9 % 3)
# print(82 % 8)
# print(30 % 7)   # 30 = 7*4 = 28 + 2 => 2

# =========================== assignment operators =========================

#  ( += , -= , *= , /= , //= , **= , %= , &= , |= , ^= , >>= , <<= )

# a = 67
# a += 3
# print(a)

# b = 39
# b -= 4
# print(b)

# c = 21
# c *= 3
# print(c)


# d = 70
# d /= 7
# print(d)

# import math
# d = 70
# d /= 7
# print(math.floor(d))

# e = 81
# e //= 8
# print(e)

# f = 2
# f **= 6
# print(f)

# g = 98
# g %= 9
# print(g)

# 0    0000
# 1    0001
# 2    0010
# 3    0011
# 4    0100
# 5    0101
# 6    0110
# 7    0111
# 8    1000
# 9    1001
# 10   1010
# 11   1011
# 12   1100
# 13   1101
# 14   1110
# 15   1111

# prodecure for the ans of &= option

# 0.0=0  f.f=f
# 0.1=0  f.t=f
# 1.0=0  t.f=f
# 1.1=1  t.t=t


# h = 14    # 1110
# h &= 5    # 0101
# print(h)  # 0100 # 'ans will be 4 because the code 0100 is the code of number 4 given above'

# i = 12     # 1100
# i &= 7     # 0111
# print(i)   # 0100 # ans 4

# |=  is called OR  # |= union

# 0+0=0  f+f=f
# 0+1=1  f+t=t
# 1+0=1  t+f=t
# 1+1=1  t+t=t

# j = 3     # 0011
# j |= 5    # 0101
# print(j)  # 0111 # ans = 7

# ^= is called XOR

# 0+0=0  f+f=f
# 0+1=1  f+t=t
# 1+0=1  t+f=t
# 1+1=1  t+t=t

# k = 9      # 1001
# k ^= 6     # 0110
# print(k)   # 1111 # ans = 15

# >>= is called shift towards right

# l = 2
# l >>= 3
# print(l)

# ____
# 0010
# ---_
# ---0010
# 0000    # ans of print(l) will be 0

# m = 9
# m >>= 1
# print(m)

# ____
# 1001
# -___
# -1001
# 0100  # ans of print(m) will be 4

# <<= is called shift towards left

# n = 5
# n <<= 3
# print(n)

# <<=  converts into 8 bit code

# 00000101
# 00101000

# o = 3
# o <<= 2
# print(o)

# 00000011
# 00001100 # ans of print(o) will be 12 b/c the last four digits from the 8 bit code is the code of num. 12

# ===================== comparision operators =====================

# Equal to                  : ==
# Not Equals to             : !=
# Greater Than              : >
# Less Than                 : <
# Greater Than or Equals to : >=
# Less than or Equals to    : <=

# a = 4
# b = 6

# print(a == b)  # it will be false b/c a is not equal to b
# print(a != b)  # it will be true b/c a is not equal to b
# print(a > b)   # false
# print(a < b)   # true
# print(a >= b)  # false
# print(a <= b)  # true

# ================== logical operators =================

# OR

# 0 + 0 = 0  f + f = f
# 1 + 0 = 1  t + f = t
# 0 + 1 = 1  f + t = t
# 1 + 1 = 1  t + t = t

# myNumber = 6
# print(myNumber > 5 or myNumber < 5)
# print(myNumber < 4 or myNumber == 6)
# print(myNumber == 5 or myNumber != 8)

# NOT

# a = b
# 1 = 0
# 0 = 1

# myNumber = 7
# print(not myNumber)

# ================== identity operators =================

# is
# is not

# a = 7
# b = 7
# print(a is b)
# print(a is not b)

# ================== membership operators ==================

# in
# not in

# list = [2, 5, 9]
# print(4 in list)
# print(2 in list)
# print(9 not in list)
# print(5 in list)

# ================== bitwise operators =====================

# ======= & method =========

# print(3 & 9)  # 3 = 0011
# 9 = 1001
#     0001 # ans of print(3 & 9) will be 1

# print(2 & 7)  # 2 = 0010
# 7 = 0111
#     0010 # ans of print(2 & 7) will be 2

# ======== | OR method ==========

# print(3 | 6)  # 3 = 0011
# 6 = 0110
#     0111 # ans will be 7

# print(9 | 12)  # 1001
# 1100
# 1101 # ans will be 13

# ======== ^ XOR method =========

# print(8 ^ 15)
# print(1 ^ 9)

# ======== ~ NOT method =========

# print(~4)
# print(~2)

# ====== >> right shift method =======

# print(7 >> 1)
# print(4 >> 2)

# ====== << left shift method =======

# print(15 << 2)
# print(11 << 3)

# ===================== casting =======================

# name = str(input('Enter your name: '))
# id = int(input('Enter your id: '))
# percentage = float(input('Enter your percentage: '))
# print(name)
# print(id)
# print(percentage)

# ===================== booleans ======================

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

# ================== Indexing ==================

#           0  1  2  3  4  5  6  7  8  9  10
# numbers = 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(numbers.count(4))
# print(numbers.count(44))
# print(numbers.index(9))
# print(numbers.index(3))

# ============================== arrays ================================

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

# print(f'{Array_1}\n{Array_2}\n{Array_3}\n{Array_4}\n{Array_5}')

# print('{}\n{}\n{}\n{}\n{}'.format(Array_1,Array_2,Array_3,Array_4,Array_5))

# print('%s\n%s\n%s\n%s\n%s'%(Array_1,Array_2,Array_3,Array_4,Array_5))

# print('%s%s%s%s%s'%(Array_1,Array_2,Array_3,Array_4,Array_5))

# print('%s'% (Array_1+Array_2+Array_3+Array_4+Array_5))

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

# ====================================== LISTS ===============================================

# list1 = ['bilal', 'haris', 'farhan', 'amin']
# list2 = [200, 300, 400, 500]
# list3 = [2.2, 3.3, 4.44, 5.53, 9.1]
# list4 = [2j, 3j, 4j, 9j, 1j]
# list5 = [True, False, None]

# print(list1, list2, list3, list4, list5)
# print(list1+list2+list3+list4+list5)

# =================== list to string =====================

# list1 = ['bilal', 'haris', 'farhan', 'amin']
# list2 = [200, 300, 400, 500]
# list3 = [2.2, 3.3, 4.44, 5.53, 9.1]
# list4 = [2j, 3j, 4j, 9j, 1j]
# list5 = [True, False, None]

# print('{}{}{}{}{}'.format(list1, list2, list3, list4, list5))

# print('%s%s%s%s%s' % (list1, list2, list3, list4, list5))
# print('%s' % (list1+list2+list3+list4+list5))
# print('%s' % (list1+list2+list3+list4+list5))

# print(f'{list1}{list2}{list3}{list4}{list5}')
# print(f'{list1}+{list2}+{list3}+{list4}+{list5}')
# print(f'{list1}+\n{list2}+\n{list3}+\n{list4}+\n{list5}')

# ============== access items in the list ================

# index    0        1        2    3    4    5
# index    0       -5       -4   -3   -2   -1
# list = ['bilal', 'haris',  1,   2,   6,   3.5]

# print(list[5])
# print(list[2])
# print(list[-3])
# print(list[-5])
# print(list[0])

# ============== changing items in the list ================

# index  0        1       2        3         4        5      6
# list = ['haris', 'amin', 'bilal', 'farhan', 'qadir', 'ali', 'saim']

# print(list)

# list[2] = 'moin '
# print(list)

# list[6] = 112
# print(list)

# list[0] = 'saud'
# print(list)

# list[2:6] = ['hamza', 'zain', 'hadi', 'anas']
# print(list)

# list[2:7] = ['hamza', 'zain', 'hadi', 'anas', 'ahmed']
# print(list)

# ============== adding items in the list ================

# there are three ways to add items in the list ( append, insert, extend )

# list1 = ['farhan', 'zakir', 'zohaib', 'zafar']
# list2 = ['faizan', 'sohaib', 'zulekha']

# list1.append('zainab')
# print(list)

# list1.insert(3, 'zulfiqar')
# print(list)

# list1.extend(list2)
# print(list1)

# myTuple = (1, 4, 8)
# list1.extend(myTuple)
# print(list1)

# myTuple = ('jiju', 'joja', 'jaji')
# list1.extend(myTuple)
# print(list1)

# =============== removing items from the list ================

# list = ['Amin', 'Sami', 'Ali', 'Haris', 'Farhan', 'Bilal', 'Kamran']

# list.remove('Haris')
# print(list)

# pop always removes the last item of the list if we donot mention anything in the brackets.

# list.pop()
# print(list)

# list.pop(3)
# print(list)

# del list[3]
# print(list)

# del list
# print(list)

# list.clear()
# print(list)

# ====================== slicing list ======================

# ================= index to item ===================

#        0        1     2   3   4    5
#        0       -5    -4  -3  -2   -1
# list = ['ahmed', 'ali', 98, 32, 4.5, 8.9]

# print(list)
# print(list[-1])
# print(list[0])
# print(list[3])
# print(list[-3])
# print(list[-5])
# print(list[5])
# print(list[:])
# print(list[2:5])
# print(list[1:])
# print(list[-5:-1])
# print(list[:-4])

# ============ item to index =============

# list = ['ahmed', 'ali', 98, 32, 4.5, 8.9]

# print(list.index(4.5))
# print(list.index(32))
# print(list.index('ali'))

# =========== changing items in the list =============

#        0        1        2        3      4         5
# list = ['ahmed', 'zafar', 'zakir', 'ali', 'farhan', 'haris']

# print(list)

# list[3] = 'haris'
# print(list)

# list[0] = 'bilal'
# print(list)

# list[1:4] = 'zain', 'amin', 'shoaib'
# print(list)

# list[2:5] = 'amin'
# print(list)

# list = [200, 300, 400, 500, 600, 700]
# list[2] = 'amin'
# print(list)

# =========== adding items in the list ============

# listA = ['haris', 'amin', 'bilal', 'farhan']
# listB = ['hamza', 'talha', 'saud', 'huzaifa']

# listA.append('taha')
# print(listA)

# listA.insert(1, 'saad')
# print(listA)

# listA.extend(listB)
# print(listA)

# ========== removing items from the list =============

#        0         1        2       3        4
# list = ['farhan', 'bilal', 'hadi', 'haris', 'amin']

# print(list)

# list.remove('haris')
# print(list)

# list.pop()
# print(list)

# list.pop(2)
# print(list)

# list.clear()
# print(list)

# del list
# print(list)

# ===================== list comprehension using loops ========================

# ================== for loop ===================

# list = ['haris', 'amin', 'farhan']
# for items in list:
#     print(items)

# list = ['haris', 'amin', 'farhan']
# for index in range(len(list)):
#     print(index)

# list = ['haris', 'amin', 'farhan']
# for haris in range(len(list)):
#     print(haris)
#     print(list[haris])
#     print(list)

# ================== while loop =================

# list = ['zahid', 'zubair', 'basim', 'sohail']
# x = 1
# while x < len(list):
#     print(list[x])
#     x = x + 1

# ======================== list comprehension ===========================

# listA = ['ashar', 'ali', 'sami', 'furqan', 'saim', 'asharib']
# listB = []
# for items in listA:
#     listB.append(items)
#     print(listB)

# listC = ['ali', 'basit', 'talha']
# listD = [items for items in listC]
# print(listD)

# ==================================== tuples in python ============================================

# list = ['haris', 'amin', ' jhanzaib']  # muthable (bcz they are changeable)
# tuple = ('bilal', 'farhan', 'shoaib')  # immutable (bcz they cannot be changed)

# print(tuple)
# print(len(tuple))
# print(type(tuple))

# tuple1 = ('bilal', 'amin', 'farhan')
# tuple2 = (22, 33, 44, 55, 66, 77)
# tuple3 = (1.2, 7.8, 9.3, 5.5)
# tuple4 = (5j, 9j, 10j, 3j)
# tuple5 = (True, False)
# tuple6 = ('bilal', 22, 33, 5j, 8j, 2.2, True)

# students = ('farhan', 'talha', 'khalid')
# classes = ('9th')
# name = str(input('enter your name: '))
# print(name)

# ==================== Tuple Formatting =======================

# tuple1 = ('bilal', 'amin', 'farhan')
# tuple2 = (22, 33, 44, 55, 66, 77)
# tuple3 = (1.2, 7.8, 9.3, 5.5)
# tuple4 = (5j, 9j, 10j, 3j)
# tuple5 = (True, False)

# print(tuple1+tuple2+tuple3+tuple4+tuple5)  # joining tuples

# print(f'this is tuple number 1: {tuple1}this is tuple number 2: {tuple2}this is tuple number 3: {tuple3}this is tuple number 4: {tuple4}this is tuple number 5: {tuple5}')

# print(f'this is tuple number 1: {tuple1}\nthis is tuple number 2: {tuple2}\nthis is tuple number 3: {tuple3}\nthis is tuple number 4: {tuple4}\nthis is tuple number 5: {tuple5}')

# print('this is tuple number 1: %s, this is tuple number 2: %s, this is tuple number 3: %s, this is tuple number 4: %s, this is tuple number 5: %s' %(tuple1, tuple2, tuple3, tuple4, tuple5))

# print('this is tuple 1: {}, this is tuple 2: {}, this is tuple 3: {}, this is tuple 4: {}, this is tuple 5: {}'.format(tuple1, tuple2, tuple3, tuple4, tuple5))

# print('the main tupple is: {}'.format(tuple1+tuple2+tuple3+tuple4+tuple5))

# ======================= Tuple Constructor ======================

# tuple = tuple(('syed', 'mohammad', 'farhan', 'qadir', 'shah', 'bukhari'))
# print(tuple)

# ======================= Accessing Tuples ========================

#           0        1       2       3   4   5
#           0       -5      -4      -3  -2  -1
# myTuple = ('haris', 'amin', 'bilal', 29, 88, 5j)

# print(myTuple)
# print(myTuple[2])
# print(myTuple[0])
# print(myTuple[-5])
# print(myTuple[-1])
# print(myTuple[:])
# print(myTuple[4:])
# print(myTuple[:3])
# print(myTuple[2:4])
# print(myTuple[-4:-1])
# print(myTuple[-5:])
# print(myTuple[:-1])
# print(myTuple[0:0])

# myTuple = ('haris', 'amin', 'bilal', 29, 88, 5j)

# myInput = input('what do you want to find in myTuple? ')
# if myInput in myTuple:
#     print('Yahoo! This item exist in myTuple')

# else:
#     print('Sorry! This item doesnot exist in myTuple')

# print(myTuple.index('amin'), myTuple[-4])

# ================= Update Tuples ==================

# myTuple = ('haris', 'amin', 'bilal', 29, 88, 5j)
# print(myTuple)

# updatedTuple = list(myTuple)
# updatedTuple.append('rizwan')
# print(updatedTuple)
# myTuple = tuple(updatedTuple)
# print(myTuple)

# ================= Unpack Tuples ==================

# tuple1 = (22, 11, 44, 99)  # packing tuples
# (a, b, c, d) = tuple1   # unpacking tuples

# print(c)
# print(a)
# print(d)
# print(b)

# tuple2 = (81, 90, 48, 87, 32, 29)  # packing tuple
# (a, b, c, *d) = tuple2  # unpacking tuple

# print(a)
# print(d)
# print(c)

# =============== Joining Tuples ================

# tuple1 = (22, 11, 44, 99)  # packing tuples
# tuple2 = (81, 90, 48, 87, 32, 29)  # packing tuple

# print(tuple1+tuple2)

# ============== Loops in tuples ================

# tuple1 = (1, 2, 3, 4, 5, 6)

# print(tuple1)

# for items in tuple1:
#     print(items)

# for x in range(len(tuple1)):
#     print(x)

# index = 0
# while index < len(tuple1):
#     print(index)
#     index = index + 1

# b = 0
# while b < len(tuple1):
#     print(tuple1[b])
#     b = b + 1

# ========================= sets in python ===============================
