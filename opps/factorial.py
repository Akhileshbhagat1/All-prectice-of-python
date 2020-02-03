# write a program to calculate a factorial no  like 5! = 120
def fectorial_(n):
    if n == 1:
        return 1
    else:
        return n*(fectorial_(n-1))


res = fectorial_(5)
print(res)

