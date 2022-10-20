
# ============================= Functions ===================================

# def myFunction():
#     pass

# myFunction()
# print(myFunction)
# print(myFunction())


# def myFunc():  # defining a function
#     print('Function has been Executed!!')


# --Calling function is very important to execute a function--
# myFunc()

# =========== arguments in Function ============


# def Function1(name, food):
#     print(name + '! your Favorite food is ' + food)

# Function1('Haris', 'French Fries')


# def add(a, b):
#     print(a*b)


# add(5, 9)

# =========== parameters in functions ============

# def addition(a=10, b=10):
#     print(a+b)


# addition()
# addition(55, 66)
# addition(55, )
# addition(66)

# ========== number of Arguments ===========

# def name(fname='amin', mname='N/A', lname='N/A', education='N/A'):
#     print(f'Welcome {fname} {mname} {lname}! you are a {education}')


# name()
# name('Amin', 'Ahmed', 'Zuberi', 'Professional of Cyber Security')
# # Arbitrary Arguments, *args (tuple)


# def ArbArg(*classmates):
#     print('The Smartest Boys are ' + classmates[0] + ' & ' + classmates[0])


# ArbArg('Haris', 'Amin', 'Bilal', 'Sami', 'Farhan')

# ========= Arbitrary kewords arguments, **kwargs (Dictionary) ==========


# def myCars(**cars):
#     print('The 1st Best Car is '+cars['car1'])
#     print('The 2nd Best Car is '+cars['car2'])
#     print('The 3rd Best Car is '+cars['car3'])


# myCars(car1='BMW', car2='Audi', car3='Tesla')

# ========= functions with list ==========

# cars = ['BMW', 'Audi', 'Tesla']


# def myCars(CARS):
#     for car in CARS:
#         print(car)


# myCars(cars)

# ========= Return ==========


# def func(arg):
#     return print(5*arg)


# func('Amin ')
# func(14)
