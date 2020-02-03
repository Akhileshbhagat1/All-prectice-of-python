import re


str = "sat, hat, mat, iat, jat, lat, pat"
somestr = re.findall("[h-m]at", str)
# print(somestr)
for i in somestr:
    print(i)