
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

# ===================== creating class ==========================


# class MyClass:         # class name must be written as title
#     x = 15
#     y = 16


# Object = MyClass()


# print(Object.x, Object.y)
# print(Object.y)

# ========== __init__() Function (initialization function) =============

# class Person:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade


# abc = Person('Haris', 16, 2)

# print(abc.name, abc.age, abc.grade)
# print(abc.name)
# print(abc.age)
# print(abc.grade)
# print(abc.name, abc.age*5, abc.grade*3)

# ================== __str__() Function (string function) ==================

# =========== (It Always Returns Expression) ============

# class Person:
#     def __init__(self, name, age, grade, tmarks):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.tmarks = tmarks

#     def __str__(self):
#         return f'Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nTotal Marks: {self.tmarks}'

#     def myFunc(self):
#         return f'{self.name} ko Python Seekhni Hai!'


# abc = Person('Haris', 16, 2, 100)  # abc is an object

# print(abc)
# print(abc.myFunc)
# print(abc.myFunc())

# abc.age = 50
# print(abc)

# del abc.age
# print(abc)
# abc = Person('Haris', 16, 2, 100)
# print(abc)
# del abc
# print(abc)

# ================================ Student Record System ==========================


# class Student:
#     pass


# std1 = Student()
# std2 = Student()
# std3 = Student()

# print(std1)
# print(std2)
# print(std3)

# std1.id = '1000'
# std1.fname = 'Haris'
# std1.lname = 'Zuberi'
# std1.fatherName = 'Waris Zuberi'

# std2.id = '2000'
# std2.fname = 'Bilal'
# std2.lname = 'Adil'
# std2.fatherName = 'Adil Zuberi'

# std3.id = '3000'
# std3.fname = 'Amin'
# std3.lname = 'Zuberi'
# std3.fatherName = 'Waris Zuberi'

# print(std1.id, std1.fname, std1.lname, std1.fatherName,)
# print(std2.id, std2.fname, std2.lname, std2.fatherName,)
# print(std3.id, std3.fname, std3.lname, std3.fatherName,)


# ==================

# class Student:
#     def __init__(self, id, fname, lname, fatherName):
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.fatherName = fatherName

#     def __str__(self):
#         return f'ID: {self.id}\nFull Name: {self.fname} {self.lname}\nFather Name: {self.fatherName}'


# std1 = Student('1000', 'Haris', 'Zuberi', 'Waris Zuberi')
# std2 = Student('2000', 'Bilal', 'Adil', 'Adil Zuberi')
# std3 = Student('3000', 'Amin', 'Zuberi', 'Waris Zuberi')
# print()
# print(std1)
# print()
# print(std2)
# print()
# print(std3)
# print()

# =====================================

# import math
#
#
# class Student:
#     annual_increment = 1.10  # class variable
#
#     def __init__(self, id, fname, lname,  fatherName, group, scholarship):
#
#         self.id = id
#         self.fname = fname
#         self.lname = lname
#         self.group = group
#         self.fatherName = fatherName
#         self.scholarship = scholarship
#
#     def __str__(self):
#         return f'ID: {self.id}\nFull Name: {self.fname} {self.lname}\nFather Name: {self.fatherName}\nGroup: {self.group}\nScholarship: {self.scholarship}\nNext year Your Scholarship Will Be Increased By,\nAnnual Increment: {str(math.floor((Student.annual_increment*100)-100))}%\nIncreased Scholarship: {math.floor(self.scholarship*self.annual_increment)}'
#
#
# std1 = Student('1122', 'Haris', 'Zuberi',
#                'Waris Zuberi', 'Computer Science', 25000)
#
# std2 = Student('1123', 'Amin', 'Zuberi',
#                'Waris Zuberi', 'Computer Science', 15000)
# std3 = Student('1124', 'Bilal', 'Adil',
#                'Adil Hameed', 'Computer Programming', 20000)
# print(std1)
# print()
# print(std2)
# print()
# print(std3)
# print()
# # scholarship_increment = str(math.floor((Student.annual_increment*100)-100))+'%'
# scholarship_increment = math.floor((Student.annual_increment*100)-100)
#
# print(scholarship_increment)

# =======================Class with methods======================

# class Employee:
#
#     def __init__(self, first_name, last_name, salary, middle_name=''):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.salary = salary
#     def __str__(self):
#         if self.middle_name != "":
#             return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nSalary: {self.salary}'
#         else:
#             return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}'

# emp1 = Employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
# emp2 = Employee('Azam', 'Shaheed', 120000)

# print(emp1)
# print()
# print(emp2)

# ======================= Class with class variables ======================

# import math
# class Employee:
#     number_of_employees = 0
#     salary_increment = 1.10
#
#     def __init__(self, first_name, last_name, salary, middle_name=''):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.salary = salary
#
#         Employee.number_of_employees += 1
#
#     def __str__(self):
#         return f'{self.first_name} | {self.last_name} | {self.salary} | {self.middle_name}'
#     def __str__(self):
#         '''if self.middle_name != "":
#             return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salary_increment)}'
#         else:
#             return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salary_increment)}'''
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first_name, last_name, salary, middle_name = emp_str.split('-')
#         return cls(first_name, last_name, salary, middle_name)
#
#
# emp1 = Employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
# emp2 = Employee('Azam', 'Shaheed', 120000)
# '''print(emp1)
# print()
# print(emp2)
# print()
# print(f'Total Employees: {Employee.number_of_employees}')'''
#
# emp3 = 'Yasir-Shami-1000000-Asool'
# print(emp3)
#
# emp_str1 = Employee.from_string(emp3)
# print(emp_str1)

# ====================================

# class Employee:
#
#     def __init__(self, fname, lname, salary, mname=''):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#         self.mname = mname
#
#     def __str__(self):
#         if self.mname != '':
#             return f'Name: {self.fname} {self.mname} {self.lname}\nSalary: {self.salary}'
#         else:
#             return f'Name: {self.fname} {self.lname}\nSalary: {self.salary}'


# emp1 = Employee('Haris', 'Zuberi', 150000)
# emp2 = Employee('Amin', 'Zuberi', 145000)
# emp3 = Employee('Bilal', 'Hameed', 145000)
# print(emp1)
# print()
# print(emp2)
# print()
# print(emp3)
# print()
# ===================================


class Employee:
    def __init__(self, fname, lname, salary, mname='', cell_no=''):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.mname = mname
        self.cell_no = cell_no

    '''def __str__(self):
        if self.mname != '':
            return f'Name: {self.fname} {self.mname} {self.lname}\nSalary: {self.salary}'
        else:
            return f'Name: {self.fname} {self.lname}\nSalary: {self.salary}'''

    @classmethod
    def ifno(cls, name):
        fname, lname, mname, salary, cell_no = name

        if mname != '':
            return cls(f'Name: {fname} {mname} {lname}\nPhone Number: {cell_no}\nSalary: {salary}')
        else:
            return cls(f'Name: {fname} {lname}\nPhone Number: {cell_no}\nSalary: {salary}')

    '''@classmethod
    def from_string(cls, emp_str):
        fname, lname, salary, mname = emp_str.split('_')
        return cls(fname, lname, salary, mname)'''


# emp4 = 'Farhan_Shah_555-100000_Qadir'
# print(Employee.from_string(emp4))
'''emp1 = Employee('Bilal', 'Hameed', 150000, mname='Adil', cell_no='03060272415')'''
emp1 = 'Bilal', 'Hameed', 'Adil', 150000, '03060272415'

print()
print()
print(Employee.ifno(emp1))
