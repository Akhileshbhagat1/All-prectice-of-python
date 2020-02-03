class Person:
    name = "akhil"
    age = 24
    country = "india"


p = Person()
x = getattr(p, 'age')  # getattr(object, attribute, default )
print(x)


