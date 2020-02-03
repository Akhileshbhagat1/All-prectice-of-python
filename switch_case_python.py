print("Enter these keywords to perform mathematical operations like....add for addition "
      "\"add for addition\" \"sub for subtraction\" \"mul for multiplication\" \"div for division\" ")


def dispatch_dict(operator, x, y):
    return {
            'add': lambda: x+y,
            'sub': lambda: x-y,
            'mul': lambda: x*y,
            'div': lambda: x/y,
        }.get(operator, lambda: None)()


key = input('Enter your keyword')
val1 = int(input('Enter first value'))
val2 = int(input('Enter second value'))

print(dispatch_dict(key, val1, val2))
