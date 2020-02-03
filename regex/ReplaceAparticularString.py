import re


Food = 'hat mat rat sat'
regex = re.compile('[r]at')
Food = regex.sub('food', Food)
print(Food)