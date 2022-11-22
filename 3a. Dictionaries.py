
# ======================================= DICTIONARIES ============================================

# Dictionaries = { keys : values }

# ==== *If u will put 2 saqme keys in a dictionary so the python will read or consider the 2nd one in the dictionary* ====

# myDict = {
#     'Name': 'Bilal',
#     'Class': 12,
#     'Age': 19,
#     'Course': 'Programming',
#     'Total Marks': 300,
#     'Obtained Marks': 225,
#     'Percentage': (225/300)*100
# }

# print(myDict)

# ====================== Accessing Keys ========================

# print(myDict['Name'])
# print(myDict['Age'])
# print(myDict['Percentage'])

# print(myDict.keys())
# print(myDict.values())

# print(len(myDict))
# print(type(myDict))

# print(myDict.get('Name'))  # (another way of accessing a key)

# ====================== Adding Items ========================

# newItem = myDict.keys()
# print(newItem)
# myDict['School'] = 'City School'
# print(newItem)

# ====================== Changing/Update Items ========================

# myDict['Course'] = 'Web Development'
# myDict['Name'] = 'Haris'
# print(myDict)

# myDict['Total Marks'] = 600
# myDict['Obtained Marks'] = 532
# myDict['Percentage'] = (532/600)*100
# print(myDict)

# myDict.update({'College': 'Jauhar College'})
# myDict.update({'College Road': 'University Road'})
# print(myDict)

# ====================== Removing Items ========================

# myDict.popitem()  # == popitem deletes the last item of dictionary or list ==
# print(myDict)

# myDict.pop('Class')
# print(myDict)

# myDict.pop('Course')
# print(myDict)

# myDict.clear() # == .clear deletes all the keys and its values ==
# print(myDict)

# del myDict # == it will give erroe bcz before printing we have deleted the dictionary ==
# print(myDict)

# ============================= Loops In Dictionaries ================================

# myDict = {
#     'Name': 'Bilal',
#     'Class': 12,
#     'Age': 19,
#     'Course': 'Programming',
#     'Total Marks': 300,
#     'Obtained Marks': 225,
#     'Percentage': (225/300)*100
# }

# print(myDict)

# for itemKeys in myDict:   # == we can give any name by our choice at the place of itemKeys ==
#     print(itemKeys)

# for itemValues in myDict:   # == we can give any name by our choice at the place of itemValues ==
#     print(myDict[itemValues])

# for keys in myDict.keys():
#     print(keys)

# for values in myDict.values():
#     print(values)

# for items in myDict.items():  # == The ans will be in tuples and we cannot change anything in tuples ==
#     print(items)

# ============================= Copying A Dictionary ================================

# myDict = {
#     'Name': 'Bilal',
#     'Class': 12,
#     'Age': 19,
#     'Course': 'Programming',
#     'Total Marks': 300,
#     'Obtained Marks': 225,
#     'Percentage': (225/300)*100
# }

# NewDict1 = myDict.copy()
# print(NewDict1)

# newDict2 = dict(myDict)
# print(newDict2)

# ============================= Nested Dictionary ================================

# == When there are more dictionaries in a dictionary then it is called Nested Dictionary ==

# ClassSubjects1 = {
#     'Class1': {
#         'Subject1': 'Urdu',
#         'Subject2': 'English',
#         'Subject3': 'Islamiat',
#     },
#     'Class2': {
#         'Subject1': 'Physics',
#         'Subject2': 'Chemistry',
#         'Subject3': 'Math',
#     },
#     'Class3': {
#         'Subject1': 'History',
#         'Subject2': 'Geography',
#         'Subject3': 'Arts',
#     }
# }

# print(ClassSubjects1)

# ======= Another Method =======

# Class1 = {
#     'Subject1': 'Urdu',
#     'Subject2': 'English',
#     'Subject3': 'Islamiat'
# }

# Class2 = {
#     'Subject1': 'Physics',
#     'Subject2': 'Chemistry',
#     'Subject3': 'Math'
# }

# Class3 = {
#     'Subject1': 'History',
#     'Subject2': 'Geography',
#     'Subject3': 'Arts'
# }

# ClassSubjects2 = {
#     'Class1': Class1,
#     'Class2': Class2,
#     'Class3': Class3
# }
# print(ClassSubjects2)

# ============================= Methods In Dictionaries ================================

# myDict = {
#     'Name': 'Bilal',
#     'Class': 12,
#     'Age': 19,
#     'Course': 'Programming',
#     'Total Marks': 300,
#     'Obtained Marks': 225,
#     'Percentage': (225/300)*100
# }

# print(myDict)

# =============== copy() =================

# newDict = myDict.copy()
# print(newDict)

# ================ get() =================

# print(myDict.get('Course'))
# print(myDict.get('Name'))

# =============== items() =================

# print(myDict.items())

# =============== keys() =================

# print(myDict.keys())

# =============== values() =================

# print(myDict.values())

# =============== update() =================

# myDict.update({'Class Section': 'A'})
# print(myDict)

# =============== pop() =================

# myDict.pop('Age')
# print(myDict)

# =============== popitem() =================

# myDict.popitem()
# print(myDict)

# =============== fromkeys() =================

# keys = ('A', 'B', 'C')
# values = 8
# newDict = dict.fromkeys(keys, values)
# print(newDict)

# =============== setdefault() =================

# myDict.setdefault('Name', 'Haris')
# print(myDict)

# myDict.setdefault('Names', 'Haris')
# print(myDict)

# =============== clear() =================

# myDict.clear()
# print(myDict)
