# #####################################################
# tel = {'a':20, 'b:':20, 'c':50, 'd':60, 'e':70}
# tel['a'] = 60
# tel['m'] = 112
# del(tel['d'])
# print(tel)
# print(list(tel))
# print(tuple(tel))
# print(str(tel))
# # print()
#
# print(tel)
########################################################

# fruits = ['a', 'b', 'c', 'd', 'e', 'a', 'f', 'b']
# for i in sorted(set(fruits)):
#     print(i)
#
# print(fruits.count('a'))

# #################################  Write a Python program to multiply all the items in a dictionary
# a = {'a':5, 'b':6, 'c':8}
# mul = 1
# for i in a.values():
# 	mul *= i
# print(mul)
# ######################################### Write a Python program to remove a key from a dictionary
# di = {'a': 12, 'b': 15, 'c': 30, 'm': 25}
# if 'm' in di:
#     del di['m']
# print(di)

# #################################    Write a Python program to map two lists into a dictionary
# a = ['a', 'b', 'd', 'e']
# b = [1, 2, 3, 4, 5]
# d = dict(zip(a, b))
#
# print(d)

# ################################################
# count = 0
# for i in range(1, 101):
#     count += i
# print(count)
# ##############################################
# d = {'a': 'abc', 'b': 'bbb', 'c': 'ccc'}
#
#
# def check(v):
#     for i in d.keys():
#         print(i)
#         if v == i:
#             return d[i]
#     print('not in dict')
#
#
# name = input('enter your choice')
# check(str(name))
# # print(d[name])
# ############################################## Write a Python program to get the key, value and item in a dictionary.
#
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 8: '', 9: ''}
#
# print('keys values count')
# for count, (keys, values) in enumerate(dict_num.items(), 1):
#     print(keys, '  ', values, '    ', count)

# ###########################################  Write a Python program to remove duplicates from Dictionary.
# d = {1: 2, 'a': 'akhil', 2: 2, 'b': 'boy', 1: 2, 'a': 'akhil', 1: ''}
# empt = {}
# for key, value in d.items():
#     if value not in empt:
#         empt[key] = value
# print(empt)
# ############################################  Write a Python program to combine two dictionary. # no made as i want
# d1 = {'a': 100, 'b': 500, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# a = d2.copy()
# b = d1.copy()
# a.update(b)
# print(a)

# ######################################### Write a Python program to find the highest 3 values in a dictionary.
