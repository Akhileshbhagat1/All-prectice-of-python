# orderedDict is a dict subclass which remembers the order in which the entries were done

# od = collections.OrderedDict()
# od['a'] = 2
# od['b'] = 1
# od['c'] = 3
# print(od)
#
# OrderedDict({[(a,2), (b,1), (c, 3)]})

from collections import OrderedDict


d = OrderedDict()
d[1] = 'a'
d[2] = 'k'
d[3] = 'h'
d[4] = 'i'
d[5] = 'l'
print(d)
