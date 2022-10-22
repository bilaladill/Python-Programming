# ================== Object Oriented Programming ====================
# ================ Classes and Objects ===================
# python is an object oriented programming language and it depends on classes and objects
'''print(type(90))
print(type('Amin'))
print(type(99.99))
print(type(5j))
a = ['Haris', 5]
print(type(a))
print(type(('ali', 5)))
print(type({'ali': 5}))'''


'''def names():
    pass


print(type(names))'''

# ============ creating class ===================


class MyClass:  # class name must be written as title
    x = 15
    y = 16


Object = MyClass()


print(Object.x, Object.y)
print(Object.y)

# __init__() Function (initialization function)


'''class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


abc = Person('Haris', 16, 2)

print(abc.name, abc.age, abc.grade)
print(abc.name)
print(abc.age)
print(abc.grade)
print(abc.name, abc.age*5, abc.grade*3)'''

# __str__() Function (string function always returns expression)


class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}'


abc = Person('Haris', 16, 2)

print(abc)
