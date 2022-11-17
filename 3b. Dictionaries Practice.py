
# ===================================== Dictionaries Practice ==========================================

# Dictionaries = { keys : values }

# ==== *If u will put 2 saqme keys in a dictionary so the python will read or consider the 2nd one in the dictionary* ====

# Players = {
#     'Batsman': 'Babar',
#     'Fast Bowler': 'Shaheen',
#     'Spin Bowler': 'Shadab',
#     'All Rounder': 'Nawaz'
# }

# print(Players)

# ====================== Accessing Keys ========================

# print(Players['Batsman'])
# print(Players['Spin Bowler'])

# print(Players.keys())
# print(Players.values())

# print(len(Players))
# print(type(Players))

# print(Players.get('All Rounder'))

# ====================== Adding Items ========================

# newItem = Players.keys()
# print(newItem)
# Players['Batsman Order'] = 2
# print(Players)
# print(newItem)

# ====================== Changing/Update Items ========================

# Players['Fast Bowler'] = 'Haris Rauf'
# print(Players)

# Players['All Rounder'] = 'Iftikhar'
# print(Players)

# Players.update({'Best Batsman': 'Babar'})
# Players.update({'Best Bowler': 'Rauf'})
# Players.update({'Best All Rounder': 'Shadab'})
# print(Players)

# ====================== Removing Items ========================

# Players.popitem()
# print(Players)

# Players.pop('Fast Bowler')
# print(Players)

# Players.clear()
# print(Players)

# del Players
# print(Players)

# ============================= Loops In Dictionaries ================================

# Players = {
#     'Batsman': 'Babar',
#     'Fast Bowler': 'Shaheen',
#     'Spin Bowler': 'Shadab',
#     'All Rounder': 'Nawaz'
# }

# print(Players)

# for role in Players:
#     print(role)

# for names in Players:
#     print(Players[names])

# for keys in Players.keys():
#     print(keys)

# for values in Players.values():
#     print(values)

# for items in Players.items():
#     print(items)

# ============================= Copying A Dictionary ================================

# Players = {
#     'Batsman': 'Babar',
#     'Fast Bowler': 'Shaheen',
#     'Spin Bowler': 'Shadab',
#     'All Rounder': 'Nawaz'
# }

# newPlayers1 = Players.copy()
# print(newPlayers1)

# newPlayers2 = dict(Players)
# print(newPlayers2)

# ============================= Nested Dictionary ================================

# Students = {
#     'Student 1': {
#         'Name': 'Haris',
#         'Age': '13',
#         'Class': '7'
#     },
#     'Student 2': {
#         'Name': 'Amin',
#         'Age': '10',
#         'Class': '5'
#     },
#     'Student 3': {
#         'Name': 'Farhan',
#         'Age': '5',
#         'Class': '2'
#     },
#     'Student 4': {
#         'Name': 'Nadir',
#         'Age': '17',
#         'Class': '10'
#     }
# }

# print(Students)

# ======= Another Method =======

# Student1 = {
#     'Name': 'Haris',
#     'Age': '13',
#     'Class': '7'
# },

# Student2 = {
#     'Name': 'Amin',
#     'Age': '10',
#     'Class': '5'
# },

# Student3 = {
#     'Name': 'Farhan',
#     'Age': '5',
#     'Class': '2'
# },

# Student4 = {
#     'Name': 'Nadir',
#     'Age': '17',
#     'Class': '10'
# }

# Students_Detail = {
#     'Student 1': Student1,
#     'Student 2': Student2,
#     'Student 3': Student3,
#     'Student 4': Student4
# }

# print(Students_Detail)

# ============================= Methods In Dictionaries ================================

# Players = {
#     'Batsman': 'Babar',
#     'Fast Bowler': 'Shaheen',
#     'Spin Bowler': 'Shadab',
#     'All Rounder': 'Nawaz'
# }

# print(Players)

# =============== copy() =================

# newPlayers = Players.copy()
# print(newPlayers)

# ================ get() =================

# print(Players.get('Batsman'))
# print(Players.get('All Rounder'))

# =============== items() =================

# print(Players.items())

# =============== keys() =================

# print(Players.keys())

# =============== values() =================

# print(Players.values())

# =============== update() =================

# Players.update({'Best Player': 'Shaheen'})
# print(Players)

# =============== pop() =================

# Players.pop('Batsman')
# print(Players)

# =============== popitem() =================

# Players.popitem()
# print(Players)

# =============== fromkeys() =================

# keys = ('City', 'Stadium')
# values = ('Melbourne')
# newPlayers = dict.fromkeys(keys, values)
# print(newPlayers)

# =============== setdefault() =================

# Players.setdefault('Batsman', 'Rizwan')
# print(Players)

# Players.setdefault('Second Batsman', 'Rizwan')
# print(Players)

# =============== clear() =================

# Players.clear()
# print(Players)
