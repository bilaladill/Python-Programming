
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
#
#     def __str__(self):
#         return f'Name = {self.name}\nAge = {self.age}\nGrade = {self.grade}'


# abc = Person('Bilal', 19, 12)

# print(abc)
