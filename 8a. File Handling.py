# =================== File Handling ======================

# f = open('haris.txt')
# print(f)
# print(f.read(5))
# h = open('G:\\bilal.txt', 'rt')
# print(h.read(10))
# print(h.read(5))

# ===========

# d = open('haris.txt')
# print(d.readline())
# print(d.readline())
# print(d.readline())

# ===========

# a = open('haris.txt')
# for x in a:
#     print(x)

# ===========

# b = open('G:\\bilal.txt')
# print(b.readline())
# b.close()

# ============ Writing to an Existing File ==============

# a = open('abc.txt','a')
# a.write('they both tease each other!')
# a.close()

# a = open('abc.txt','r')
# print(a.read())

# b = open('abc.txt','w')
# b.write('this is a file named as abc')
# b.close()

# b = open('abc.txt','r')
# print(b.read())

# creating a new file xyz ( We use x to create file )

# c = open('xyz.txt','x')
# c.close()

# d = open('xyz.txt','a')
# d.write('''haris is crying!
# uwain uwain uwain!!!
# he is also good boy''')
# d.close()

# d = open('xyz.txt','r')
# print(d.read())

# ============ Deleting files =============

# import os
# os.remove('xyz.txt')

# if os.path.exists('xyz.txt'):
#     os.remove('xyz.txt')
# else:
#     print('there is no such file!!')