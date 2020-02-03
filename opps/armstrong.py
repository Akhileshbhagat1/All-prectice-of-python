# write a python program for armstrong no
# num = int(input("enter a no"))
for i in range(101):
    num = i
    result = 0
    n = len(str(i))
    while i != 0:
        digit = i % 10
        result = result + digit ** n
        i = i//10
    if num == result:
        print(num)
