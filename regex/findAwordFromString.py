import re


# allinform = re.findall('inform', 'we need to inform him for latest information')  # findall() returns list of matches
# for i in allinform:
#     print(i)

if re.search('inform', 'we need to inform him for latest information'):
    print("match found")
