import re

NameAge = ''' Akhil is 24 years old and Vinit is only 27 Neha is 21 years as well as Ruchi is 22 and Vikesh  is 23 and 
                Mithlesh is 26'''

ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)

# print(dict(zip(names, ages)))       # for printing a dict
# print(ages)
# print(names)

# another way to printing a dict

ageDict = {}
x = 0
for eachNames in names:
    ageDict[eachNames] = ages[x]
# print(ageDict)
    x += 1
print(ageDict)
