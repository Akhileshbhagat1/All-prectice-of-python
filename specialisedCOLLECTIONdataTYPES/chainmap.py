# chainmap is a dictonary like class for creating a single view of multiple mapping.

# example :   A = {1: 'akil', 2: 'vinit'}
#             B = {3: 'subham', 3: 'umesh'}

#              ({1: 'akil', 2: 'vinit'}, {3: 'subham', 4: 'umesh'})


from collections import ChainMap


A = {1: 'akil', 2: 'vinit'}
B = {3: 'subham', 3: 'umesh'}
C = ChainMap(A, B)
print(C)