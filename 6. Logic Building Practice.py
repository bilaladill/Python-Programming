# ============================== If, Elif, Else ==================================

# equal            ==
# unequal          !=
# greater          >
# less             <
# greater or equal >=
# less or equal    <=

# ============================= Programs ===============================

# =============== If, Elif, Else =================

import math

name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
rank = int(input('Enter your class: '))
section = str(input('Enter your section: '))
subject = str(input('Enter learning subject: '))
total_marks = int(input('Enter total marks: '))
obtained_marks = int(input('Enter obtained marks: '))
percentage = math.floor((obtained_marks/total_marks)*100)
# grade = str('A', 'A+', 'B', 'C', )


if percentage >= 80 and percentage <= 100:
    print('Grade: A+')
#
elif percentage >= 70 and percentage < 80:
    print('Grade: A')
#
elif percentage >= 60 and percentage < 70:
    print('Grade : B')
#
elif percentage >= 50 and percentage < 60:
    print('Grade: C')
#
else:
    print('Grade: Failed')

print(f'--- THE DECENCY CODIFIED MARKETING ---\nName: {name}\nAge: {age}\nClass: {rank}\nSection: {section}\nSubject: {subject}\nObtained Marks: {obtained_marks}\nTotal Marks: {total_marks}\nPercentage: {percentage}%\n--- RESULT FROM THE DECENCY CODIFIED MARKETING ---')
