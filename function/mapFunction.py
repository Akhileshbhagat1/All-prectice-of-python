# Defination = the map() executes a specified function for each item in a iterable .
#              the item is sent to the function as a parameter

# Syntax = map(function, iterable)


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'grapse'))
print(x)

