# ===== 30-sep-22 =====

# import math
# name = str(input('enter your name: '))
# age = int(input('enter your age: '))
# id = int(input('enter your id: '))
# total_marks = int(input('enter your total marks: '))
# obtained_marks = int(input('enter your obtained marks: '))
# percentage = math.floor((obtained_marks/total_marks)*100)
# print(f'Your name is {name} and your age is {age} years. Your id is {id}. Your total marks were {total_mrks} and you have obtained {obtained_marks} marks. Which becomes {percentage}%.')

# ============================== List ======================================


# my_list = ['Amin', 'Farhan', 'Haris', 'Bilal']
# print(len(my_list))

# ============= 28 - october - 2022 ================


'''def StudentProfile(fname, lname, **StudentInfo):
    StudentInfo['First Name'] = fname
    StudentInfo['Last Name'] = lname
    return StudentInfo


Std_profile = StudentProfile('Haris', 'Ahmed', percentage='51%')
print(Std_profile)

StdFatherName = str(input('Enter your Father Name: '))
StdClass = int(input('Enter your class: '))
print(
    f'Student Name: {Std_profile}!\nFater Name: {StdFatherName}\nStudent Class: {StdClass}')
'''


# Make a programe using strings., function., class, Interger., input., for loop
import math


class Bilal:

    obtainedMarks = input('Obtaied Marks out of 750: ')

    def __init__(self, fname, lname, sports):
        self.fname = fname
        self.lname = lname
        self.sports = sports

    def __str__(self):
        return f'First Name: {self.fname}\nLast Name: {self.lname}\nFavorite Sports: {self.sports}'

    def myinfo():
        percentage = math.floor((int(Bilal.obtainedMarks)/750)*100)
        return f'You have Result is as Follow,\nResult: {percentage}%'


myInformation = Bilal('Bilal', 'Adil', 'Cricket')
print(myInformation)
print(Bilal.myinfo())
