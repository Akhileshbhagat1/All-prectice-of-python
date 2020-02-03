# deque but it pronounced as 'deck' is an optimised list to perform insertion and deletion easily

from collections import deque


a = ['a', 'k', 'h', 'i', 'l']
d = deque(a)
d.append('bhagat')
d.appendleft('Mr.')
d.pop()    # pop() removes the last value from the list
d.popleft() # popleft() removes the value from the first
print(d)