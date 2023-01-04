
# ============================ OBJECT ORIENTED PROGRAMMING ===============================

# ===================== Classes and Objects =======================

# python is an object oriented programming language and it depends on classes and objects

# print(type(90))
# print(type('Amin'))
# print(type(99.99))
# print(type(5j))
# a = ['Haris', 5]
# print(type(a))
# print(type(('ali', 5)))
# print(type({'ali': 5}))


# def names():
#     pass


# print(type(names))

# ================== Creating Class =====================

# class MyClass:
#     x = 12
#     y = 15


# object = MyClass()

# print(object.x)
# print(object.y)
# print(object.y, object.x)
# print(object.y*object.x)

# ==============

# class MyClass:
#     fname = 'Bilal'
#     lname = 'Adil'


# object = MyClass()

# print(object.fname)
# print(object.lname)
# print(object.fname+' '+object.lname)

# ============= __init__() Function (initialization function) =============

# class person:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade


# abc = person('Bilal', 19, 12)
# print(abc.name, abc.age, abc.grade)
# print(abc.name)
# print(abc.age)
# print(abc.grade)

# ================== __str__() Function (string function) ===================

# =========== (It Always Returns Expression) ============

# class Person:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def __str__(self):
#         return f'Name = {self.name}\nAge = {self.age}\nGrade = {self.grade}'


# abc = Person('Bilal', 19, 12)

# print(abc)

# =======================

# class student:
#     def __init__(self, name, age, gender, birthYear):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.birthYear = birthYear
#
#     def __str__(self):
#         return f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nBirth Year: {self.birthYear}'
#
#     def myFunc(self):
#         return f'{self.name} wants to learn python and different programming languages.'
#

# std_detail = student('Bilal', 19, 'Male', 2003)
# print(std_detail)
# print(std_detail.myFunc())
# print(std_detail.myFunc)
#
# std_detail.age = 50
# print(std_detail.age)
#
# del std_detail.age
# print(std_detail)
# std_detail = student('Bilal', 19, 'Male', 2003)
# print(std_detail)
# del std_detail
# print(std_detail)

# ===================== employees record system ========================

# class employees:
#     pass


# emp1 = employees()
# emp2 = employees()
# emp3 = employees()
# emp4 = employees()
# emp5 = employees()

# print(emp1)
# print(emp2)
# print(emp3)
# print(emp4)
# print(emp5)

# emp1.fname = 'Huzaifa'
# emp1.lname = 'Nadeem'
# emp1.phnumber = '03307182973'
# emp1.level = 'Manager'

# emp2.fname = 'Moeen'
# emp2.lname = 'Ali'
# emp2.phnumber = '03307182973'
# emp2.level = 'Sales Officer'

# emp3.fname = 'Rashid'
# emp3.lname = 'Khan'
# emp3.phnumber = '03139378201'
# emp3.level = 'Security Guard'

# emp4.fname = 'Shahzeb'
# emp4.lname = 'Khanzada'
# emp4.phnumber = '03238963720'
# emp4.level = 'Host'

# emp5.fname = 'Ghazab'
# emp5.lname = 'Khan'
# emp5.phnumber = '02873637829'
# emp5.level = 'Cashier'

# print(emp1.fname, emp1.lname, emp1.phnumber, emp1.level)
# print(emp2.fname, emp2.lname, emp2.phnumber, emp2.level)
# print(emp3.fname, emp3.lname, emp3.phnumber, emp3.level)
# print(emp4.fname, emp4.lname, emp4.phnumber, emp4.level)
# print(emp5.fname, emp5.lname, emp5.phnumber, emp5.level)


# print(
#     f'Employee Details:\n \nName: {emp1.fname} {emp1.lname}\nPhone Number: {emp1.phnumber}\nPosition: {emp1.level}')
# print()
# print(
#     f'Employee Details:\n \nName: {emp2.fname} {emp2.lname}\nPhone Number: {emp2.phnumber}\nPosition: {emp2.level}')
# print()
# print(
#     f'Employee Details:\n \nName: {emp3.fname} {emp3.lname}\nPhone Number: {emp3.phnumber}\nPosition: {emp3.level}')
# print()
# print(
#     f'Employee Details:\n \nName: {emp4.fname} {emp4.lname}\nPhone Number: {emp4.phnumber}\nPosition: {emp4.level}')
# print()
# print(
#     f'Employee Details:\n \nName: {emp5.fname} {emp5.lname}\nPhone Number: {emp5.phnumber}\nPosition: {emp5.level}')
# print()

# ==========================

# class player:
#     def __init__(self, fullname, type, orderNum, team):
#         self.fullname = fullname
#         self.type = type
#         self.orderNum = orderNum
#         self.team = team

#     def __str__(self):
#         return f'Name: {self.fullname}\nType: {self.type}\nOrder Number: {self.orderNum}\nTeam: {self.team}'


# Player1 = player('Virat Kohli', 'Batsman', 3, 'India')
# Player2 = player('Trent Boult', 'Bowler', 11, 'Newzealand')
# Player3 = player('Shadab Khan', 'All Rounder', 6, 'Pakistan')

# print()
# print(Player1)
# print()
# print(Player2)
# print()
# print(Player3)
# print()

# ====================== class with methods =========================

# class student:
#
#     def __init__(self, fname, lname, father_name, age, group, fees, middle_name=''):
#         self.fname = fname
#         self.lname = lname
#         self.father_name = father_name
#         self.age = age
#         self.group = group
#         self.fees = fees
#         self.middle_name = middle_name

#     def __str__(self):
#         if self.middle_name != '':
#             return f'Name: {self.fname} {self.middle_name} {self.lname}\nFather Name: {self.father_name}\nAge: {self.age}\nGroup: {self.group}\nFees: {self.fees}'

#         else:
#             return f'Name: {self.fname} {self.lname}\nFather Name: {self.father_name}\nAge: {self.age}\nGroup: {self.group}\nFees: {self.fees}'


# std1 = student('Jhanzeb', 'shakir', 'Shakir Ali', 12, 4, 5000)
# std2 = student('Hadi', 'Ahmed', 'Ahmed Malik', 13, 5, 7000, 'Bin')

# print()
# print(std1)
# print()
# print(std2)
# print()

# ==================== Class with class variables =====================

# import math


# class employee:
#
#     numberOfEmployees = 0
#     salaryIncrement = 1.10
#
#     def __init__(self, fname, lname, salary, middleName=''):
#         self.fname = fname
#         self.lname = lname
#         self.middleName = middleName
#         self.salary = salary
#
#         employee.numberOfEmployees += 1
#
#     def __str__(self):
#         if self.middleName != '':
#             return f'First Name: {self.fname}\nMiddle Name: {self.middleName}\nLast Name: {self.lname}\nSalary: {self.salary}\nAnnual Increment: {math.floor((self.salaryIncrement*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salaryIncrement)}'
#
#         else:
#             return f'First Name: {self.fname}\nLast Name: {self.lname}\nSalary: {self.salary}\nAnnual Increment: {math.floor((self.salaryIncrement*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salaryIncrement)}'


# emp1 = employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
# emp2 = employee('Azam', 'Shaheed', 120000)
#
# print()
# print(emp1)
# print()
# print(emp2)
# print()
# print(f'Total Employees: {employee.numberOfEmployees}')

# =======================

# class Employee:
    
#     def __init__(self, fname, lname, age, salary, mname=''):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.salary = salary
#         self.mname = mname
        
#     def __str__(self):
#         if self.mname != '':
#             return f'Name: {self.fname} {self.mname} {self.lname}\nAge: {self.age}\nSalary: {self.salary}'
#         else:
#             return f'Name: {self.fname} {self.lname}\nAge: {self.age}\nSalary: {self.salary}'
         
# emp1 = Employee('Aqib', 'Jafri', 22, 12000)
# emp2 = Employee('Amin', 'Zuberi', 23, 13000, 'Ahmed')
# emp3 = Employee('Hassan', 'Jhangir', 24, 14000)
# emp4 = Employee('Wasim', 'Khan', 25, 15000, 'Akhtar')
 
# print(emp1)
# print()
# print(emp2)
# print()
# print(emp3)
# print()
# print(emp4)
# print()

# ========================

# from datetime import date

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @classmethod
#     def from_Employee(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)
    
#     def display(self):
#         print(f'Name: {self.name}\nAge: {self.age}')
        
#     @staticmethod
#     def isAdult():
#         age = int(input('Enter your age: '))
#         if age <= 17:
#             return print(f'You are not an adult uptill now!')
#         else:
#             return print(f'Wow you are an adult!')
        
# emp1 = Employee('Qazi', 16)
# emp2 = Employee.from_Employee('Saim', 1995)

# print(emp1.age)
# print(emp2.age)
# Employee.isAdult()
