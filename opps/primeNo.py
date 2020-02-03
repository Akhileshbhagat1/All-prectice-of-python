# num = int(input("Enter a no"))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, " is not a prime no")
#             break
#         else:
#             print(num, "is a prime no")
#             break


print("Enter a no to check prime or not")
num = int(input())
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime no")
            break
        else:
            print(f'{num} is a prime no')
            break
else:
    print("please enter an integer grater than 1 ")

















