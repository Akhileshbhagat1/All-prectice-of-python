# counter is a dictonary subclass for counting hashable objects.

# A = [1,2,3,4,5,6,7,8]
# count = aounter(A)
# counter({})

from collections import Counter


a = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 1, 5, 7, 9, 23, 6, 5, 5, 8, 6]
c = Counter(a)                 # Counter() returns a dictonary and it is applicable on all iterble(list, tuple, set)
print(c)
# print(tuple(c.elements()))
# print(list(c.elements()))
# print(set(c.elements()))

print(c.most_common())
sub = {5: 1, 1: 1}
print(c.subtract(sub))
print(c.most_common())


