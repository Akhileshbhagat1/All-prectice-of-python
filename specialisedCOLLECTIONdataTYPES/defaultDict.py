# defaultDict is a dictonary subclass which calls a factory function to supply misssing values

# d = defaultDict(int)
# d['akhilesh'] = 1
# d['python'] = 2
# print(d['java'])
#
# op = 0


from collections import defaultdict


d = defaultdict(int)
d[1] = 'akhilesh'
d[2] = 'python'
# print(d)
print(d[3])
