
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

# ======================= Making Programs Of Functions ============================

# def greeting(username):
#     print(f'Hello! {username.upper()}')


# greeting('bilal')

# ====================

# def greeting(username):
#     print(f'Hello! {username.title()}')


# greeting('bilal')

# ====================


# def names(fname, lname):
#     fullName = f'{fname} {lname}'
#     return fullName.title()


# while True:
#     print("Enter 'q' to quit the program.")
#     print('Please enter your name below.')
#     FName = input('Enter your first name: ')
#     if FName == 'q':
#         break
#     LName = input('Enter your last name: ')
#     if LName == 'q':
#         break
#     Name = names(FName, LName)
#     print(f'Hello {Name} how are you?')

# ========================


# def greeting(names):
#     for name in names:
#         message = f'Hello, {name}!'
#         print(message)


# usernames = ['Haris', 'Amin', 'Chaparganju']
# greeting(usernames)

# =======================

# def makingPizza(*flavours):
#     print(f'\nWe have variety of pizza flavours!\nThe flavours are:')
#     for flavour in flavours:
#         print(f'{flavour}')


# flavours = ('fajita', 'tikka', 'bbq', 'afghani feast')
# makingPizza(flavours)

# pizza = str(
#     input('Which flavour pizza do you want?\nInput here your desired flavour: '))
# if pizza == 'fajita' or pizza == 'tikka':
#     print("Okay! We'll serve you in 10 mins.")
# elif pizza == 'bbq' or pizza == 'afghani feast':
#     print("Okay! We'll serve you in 10 mins.")
# else:
#     print("Sorry! We don't have this flavour.")

# =========================

# def Profile(fname, lname, **userInfo):
#     userInfo['Frist Name'] = fname
#     userInfo['Last Name'] = lname
#     return userInfo


# userProfile = Profile('Bilal', 'Adil', Age=19, Gender='Male',
#                       Grade='Intermediate', NationalLanguage='Urdu')
# print(userProfile)
