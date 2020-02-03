# namedtuple() returns the tuple with named value for esch element in the tuple

# details = (name = 'akhilesh', age = '24', language = 'python')

from collections import namedtuple


a = namedtuple('courses', 'name, technology, age, address ')
s = a('akhilesh', 'python', '24', 'bhagaiya')
print(s)
                # you can use list at the place of tuple  OR iterable(list, tuple) in both case it will return tuple
# s = a._make(['akhilesh', 'python', '24', 'bhagaiya'])
# print(s)
