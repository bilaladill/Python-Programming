# ============================== If, Elif, Else ==================================

# equal            ==
# unequal          !=
# greater          >
# less             <
# greater or equal >=
# less or equal    <=


# Made By Amin
# d = int(input('enter number d: '))
# y = int(input('enter number y: '))
#
# if d > y:
#     print('d is grater than y')
#
# elif d < y:
#     print('y is grater than d')
#
# else:
#     print('both are equal')

# Made By Bilal

# yourFood = str(input('Enter the food you want to know in menu card: '))
# PakistaniMenu = ['nihari', 'biryani', 'qarhai', 'kunna']
# ChineseMenu = ['momos', 'shashlic', 'platter', 'cockroach']

# if yourFood in PakistaniMenu:
#     print('Yeah sure, we do have this Pakistani food and we can serve it to you!')

# elif yourFood in ChineseMenu:
#     print('Yeah sure, we do have this Chinese item and we can serve it to you!')

# else:
#     print('Sorry! We Don\'t Have This Item')

# Made By AMIN

# YourName = str(input('Enter your Name: '))
# Yourclass = int(input('Enter your class: '))
# YourBestFriend = str(input('Enter your Best friend: '))

# if YourName == 'Farhan' or YourBestFriend == 'Amin':
#     print('You are Right!')

# elif YourName == 'Amin' or YourBestFriend == 'Farhan':
#     print('You are Also Right!')

# else:
#     print('Please make good friends!!')

# =================================== Programs ==========================================

# ===================== If, Elif, Else ==========================

# person = str(input('Your Nationality? '))
# if person == 'Pakistani' or person == 'pakistani':
#     print('To kesy hain ap Log!!')
# else:
#     print('Hum Ap ko nahi Janty!!!')


# person = str(input('Your Nationality? '))
# if person == 'Arabic' or person == 'arabic':
#     print('Marhaba Ya Habibi!!')
# if person == 'Pakistani' or person == 'pakistani':
#     print('Assalam Alaikum!!')


# person = str(input('Your Nationality? '))
# if person == 'Arabic' or person == 'arabic':
#     print('Marhaba Ya Habibi!!')

# elif person == 'Pakistani' or person == 'pakistani':
#     print('Assalam Alaikum!!')

# elif person == 'Indian' or person == 'indian':
#     print('India will be defeated by Pakistan Soon, In Sha Allah')

# else:
#     print('we are not available in your country')


# name = str(input('Enter Your Name: '))
# age = int(input('Enter your Age: '))
# if age < 0:
#     print('This is not true, don\'t try to be Over Smart')
# elif age <= 10:
#     print('You are too small to be a programmer')
# elif age == 13:
#     print('You are cute %s' % (name))
# elif age == 17:
#     print('Yeah Boy, This is {}'.format(name))
# elif age == 19:
#     print(f'Masoom {name}')
# elif age > 30:
#     print(f'Budhy {name}')
# else:
#     print(f'Ab to {name} hi bacha hai')


# a = float(input('Enter number a: '))
# b = float(input('Enter number b: '))
# c = float(input('Enter number c: '))
# maximum = max((a, b, c))
# print('The Maximum value is: ' + str(maximum))

# if a > b and a > c:
#     maximum = a
# elif b > a and b > c:
#     maximum = b
# else:
#     maximum = c
# print('The Maximum value is: ' + str(maximum))


# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'corolla':
#         print(car.lower())
#     else:
#         print(car.title())


# banned_users = ['sami', 'sani', 'ali']
# user = input('entr name: ')
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")
# else:
#     print(f"{user.title()}, you are not allowed to post any response.")
