# merging two list's values into a single list
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']
# list1.extend(list2)
# print(list1)

# or

# list3 = [1, 2, 3, 4]
# list4 = ['q', 'e', 'w', 't']
#
# list5 = []
# for i in list3:
#     list5.append(i)
# for j in list4:
#     list5.append(j)
# print(list5)

# or

# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']
# list3 = list1 + list2
# print(list3)

# 0r
#
from itertools import chain

print(list(chain([1, 2, 3, 4], ['a', 'b', 'c', 'd'])))
