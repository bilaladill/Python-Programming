    # ===== 30-sep-22 =====

# import math
# name = str(input('enter your name: '))
# age = int(input('enter your age: '))
# id = int(input('enter your id: '))
# total_marks = int(input('enter your total marks: '))
# obtained_marks = int(input('enter your obtained marks: '))
# percentage = math.floor((obtained_marks/total_marks)*100)
# print(f'Your name is {name} and your age is {age} years. Your id is {id}. Your total marks were {total_mrks} and you have obtained {obtained_marks} marks. Which becomes {percentage}%.')

# ============ List =============


# my_list = ['Amin', 'Farhan', 'Haris', 'Bilal']
# print(len(my_list))

# ============= 28 - october - 2022 ================


# def StudentProfile(fname, lname, **StudentInfo):
#     StudentInfo['First Name'] = fname
#     StudentInfo['Last Name'] = lname
#     return StudentInfo

# Std_profile = StudentProfile('Haris', 'Ahmed', percentage='51%')
# print(Std_profile)
# 
# StdFatherName = str(input('Enter your Father Name: '))
# StdClass = int(input('Enter your class: '))
# print(
#     f'Student Name: {Std_profile}!\nFater Name: {StdFatherName}\nStudent Class: {StdClass}')
 

# =========================

# Make a programe using strings., function., class, Interger., input., for loop

# import math

# class Bilal:

#     obtainedMarks = input('Obtaied Marks out of 750: ')
#
#     def __init__(self, fname, lname, sports):
#         self.fname = fname
#         self.lname = lname
#         self.sports = sports

#     def __str__(self):
#         return f'First Name: {self.fname}\nLast Name: {self.lname}\nFavorite Sports: {self.sports}'

#     def myinfo():
#         percentage = math.floor((int(Bilal.obtainedMarks)/750)*100)
#         return f'You have Result is as Follow,\nResult: {percentage}%'

# myInformation = Bilal('Bilal', 'Adil', 'Cricket')
# print(myInformation)
# print(Bilal.myinfo())

# ===================== 19 - Nov - 22 ======================

# ====== Sample Programe by Sir Firhan ======

# import math

# numberofStudents, totalMarks, studentName, studentAge, studentClass, studentMarks = 5, 500, [], [], [], []
# 
# for student in range(1, numberofStudents):
#     global name, age, grade, marks
# 
#     name = input('Enter Your name: ')
#     age = input('Enter Your Age: ')
#     grade = input('Enter Your Class: ')
#     marks = int(input('Enter Your Marks: '))
# 
#     studentName.append(name)
#     studentAge.append(age)
#     studentClass.append(grade)
#     studentMarks.append(marks)
# 
# print(studentName, studentAge, studentClass, studentMarks)
# 
# 
# def result():
#     return print(f'student Name: {studentName[index]}\nstudent Age:{studentAge[index]}\nstudent Grade:{studentClass[index]} \nObtained Marks:{studentMarks[index]}\nPercentage:{math.floor((studentMarks[index]/totalMarks)*100)}%\ncomment: Congrats! You Got First Position!!')
# 
# 
# if studentMarks[0] > (studentMarks[1] and studentMarks[2] and studentMarks[3]):
#     index = 0
#     result()
# elif studentMarks[1] > (studentMarks[0] and studentMarks[2] and studentMarks[3]):
#     index = 1
#     result()
# elif studentMarks[2] > (studentMarks[1] and studentMarks[1] and studentMarks[3]):
#     index = 2
#     result()
# else:
#     index = 3
#     result()

# ========================
'''
total_employees, employee_name, employee_age, employee_rank, employee_salary = 5, [], [], [], []

for employee in range(1, total_employees):
    global name,age,rank,salary
    
    name = (input('Name: '))
    age = (input('Age: '))
    rank = (input('Rank: '))
    salary = (input('Salary: '))
    
    employee_name.append(name)
    employee_age.append(age)
    employee_rank.append(rank)
    employee_salary.append(salary)
    
print(employee_name, employee_age, employee_rank, employee_salary)

def employee_details():
    return print(f'Employee Name: {employee_name[index]}\nEmployee Age: {employee_age[index]}\nEmployee Rank: {employee_rank[index]}\nEmployee Salary: {employee_salary[index]}\n{employee_name[index]} Has The Best Rank In The Office!')

if employee_rank[0] > (employee_rank[1] and employee_rank[2] and employee_rank[3]):
    index = 0
    employee_details()
elif employee_rank[1] > (employee_rank[0] and employee_rank[2] and employee_rank[3]):
    index = 1
    employee_details()
elif employee_rank[2] > (employee_rank[0] and employee_rank[2] and employee_rank[3]):
    index = 2
    employee_details()
else:
    index = 3
    employee_details()
'''
   
# ============== 23 Nov 22 ================

# ========= Logic Building ===========

# import math
# 
# school = 'Early Learning School'
# name = input('Name: ') 
# age = int(input('Age: ')) 
# grade = int(input('Class: ')) 
# section = input('Section: ') 
# obtained_marks = int(input('Obtained Marks: ')) 
# total_marks = 500 
# percentage = math.floor((obtained_marks/total_marks)*100) 
# 
# print(f'\n \n------- {school} -------\n---------- Report Card ----------\nName: {name}\nAge: {age}\nClass: {grade}{section}\nObtained Marks: {obtained_marks}\nTotal Marks: {total_marks}\nPercentage: {percentage}')
# 
# if percentage >=80 and percentage <= 100:
#     print('Grade: A+\n-------- Congratulations --------')
#     
# elif percentage >=70 and percentage <= 79:
#     print('Grade: A\n-------- Congratulations --------')
#     
# elif percentage >= 60 and percentage <= 69:
#     print('Grade: B\n-------- Congratulations --------')
#     
# elif percentage >= 50 and percentage <= 59:
#     print('Grade: C\n-------- Congratulations --------')
#     
# else:
#     print('Grade: Fail\n---------- Work Hard ----------')    
    
# ===============================

'''
import math

total_students, stdName, stdAge, stdGrade, stdSec, stdOM, stdTM, stdPerc, stdPos = 4, [], [], [], [], [], [], [], [] 

for students in range(1, total_students):
    global name, age, grade, section, obtained_marks, total_marks, percentage 

    name = input('Name: ') 
    age = int(input('Age: ')) 
    grade = int(input('Class: ')) 
    section = input('Section: ') 
    obtained_marks = int(input('Obtained Marks: ')) 
    total_marks = 500 
    percentage = math.floor((obtained_marks/total_marks)*100) 
    
    stdName.append(name)
    stdAge.append(age)
    stdGrade.append(grade)
    stdSec.append(section)
    stdOM.append(obtained_marks)
    stdTM.append(total_marks)
    stdPerc.append(percentage)
    stdPos.append()

print(stdName, stdAge, stdGrade, stdSec, stdOM, stdTM, stdPerc)
    
def std_result():
    print(f'\n \n------- Early Learning School -------\n---------- Report Card ----------\nName: {name[index]}\nAge: {age[index]}\nClass: {grade[index]}{section[index]}\nObtained Marks: {obtained_marks[index]}\nTotal Marks: {total_marks[index]}\nPercentage: {percentage[index]}\nPositon: {}')

if percentage >=80 and percentage <= 100:
    print('Grade: A+\n-------- Congratulations --------')
    
elif percentage >=70 and percentage <= 79:
    print('Grade: A\n-------- Congratulations --------')
    
elif percentage >= 60 and percentage <= 69:
    print('Grade: B\n-------- Congratulations --------')
    
elif percentage >= 50 and percentage <= 59:
    print('Grade: C\n-------- Congratulations --------')
    
else:
    print('Grade: Fail\n---------- Work Hard ----------')
'''

