import re


str = "sat, hat, mat, pat"
allStr = re.findall("[shmp]at", str)
# print(allStr)
for i in allStr:
    print(i)