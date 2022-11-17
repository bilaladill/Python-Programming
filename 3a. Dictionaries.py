
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

# print(myDict)
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

# === pop (It deletes/remove the last item or given item in argument from list or dictionary ) ===

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

myDict = {
    'Name': 'Bilal',
    'Class': 12,
    'Age': 19,
    'Course': 'Programming',
    'Total Marks': 300,
    'Obtained Marks': 225,
    'Percentage': (225/300)*100
}
