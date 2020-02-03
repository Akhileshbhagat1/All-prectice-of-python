num = int(input("enter a no"))
first = 0
second = 1
for i in range(num):
    print(first)
    temp = first
    first = second
    second = temp + second

# ###### alternate method

#
# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return f(n-2) + f(n-1)
#
#
# for i in range(1, 20):
#     print(f(i))


