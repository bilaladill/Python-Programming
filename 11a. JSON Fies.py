# =================== JSON Files ========================

# Json to python

# import json

# x = '{"name":"Bilal", "Age":30,"city":"Karachi"}'
# y = json.loads(x) # json to python
# print(y)
# print(y.keys())
# print(y.values())
# print(x)

# mydict = {
#     'name':'haris',
#     'age':16,
#     'city':'california'
#     
# }
# z = json.dumps(mydict) # python to json
# print(z)

# we can convert following python objects into JSON i.e.
# dict,list,tuple,string,int,float,True,False,None

# print(json.dumps({"name":"Bilal", "Age":30,"city":"Karachi"}))
# print(json.dumps(["Bilal", 30,"Karachi"]))
# print(json.dumps(("Bilal", 30,"Karachi")))
# print(json.dumps("Bilal"))
# print(json.dumps(55))
# print(json.dumps(55.55))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json
# 
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# 
# print(json.dumps(x))
# print(json.dumps(x, indent=4))

