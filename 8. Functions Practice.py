
# ========================= Functions ===============================

# def myFunction():
#     pass


# myFunction()
# print(myFunction)
# print(myFunction())

# =====================

# def myFunc():
#     print('It is my function and you are not supposed to change it!')


# myFunc()

# ===================== Arguments In Function ========================

# def func(name, age):
#     print('Congratulations ' + name + '! You are ' + str(age) + ' years old now!')


# func('Bilal', 19)

# ===================

# def add(a, b):
#     print(a*b)


# add(3, 9)

# =================== Parameters In Function =====================

# def addition(b=20, d=30):
#     print(b+d)


# addition()
# addition(10, 50)
# addition(5, )
# addition(90)

# ==============

# def addition(b, d):
#     print(b+d)


# addition(5, 5)
# addition(5, 3)
# addition(15, 40)

# =================== Number Of Arguments =====================

# def name(fname='Bilal', lname='Adil', education='Intermediate'):
#     print(f'Hello {fname} {lname}! You are an {education} student.')


# name()

# ====================


# def name(fname='N/A', lname='N/A', education='N/A'):
#     print(f'Hello {fname} {lname}! You are an {education} student.')


# name()

# =========== Arbitrary Arguments =============

# def ArbArg(*classmates):
#     print('The handsome boys are ' + classmates[0] + ' and ' + classmates[1] + '.')


# ArbArg('farhan', 'bilal', 'amin', 'nabeel')

# ==================

# def ArbArg(*classmates):
#     print('The handsome boys are ' +
#           classmates[3] + ' and ' + classmates[2] + '.')


# ArbArg('farhan', 'bilal', 'amin', 'nabeel')

# ================= Arbitrary Keyword Arguments, **kwords (dictionary)

# def myCars(**cars):
#     print('My first car was ' + cars['fcar'])
#     print('My second car was ' + cars['scar'])
#     print('My third car was ' + cars['tcar']+'.')
#     print('My current car is ' + cars['ccar']+'.')


# myCars(fcar='Audi', scar='Ferrari', tcar='Mercedes', ccar='Tesla')

# =============== Functions With List ===============

# cars = ['audi', 'sonata', 'prado', 'mark x']


# def myCars(Cars):
#     for car in Cars:
#         print(car)


# myCars(cars)

# =============== Return ==================

# def func(arg):
#     return print(3*arg)


# func('Bilal ')

# ================

# def func(arg):
#     return print(3*arg)


# func('Bilal\n')

# ================

# def func(arg):
#     return print(3*arg)


# func(20)

# ================
