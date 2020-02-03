# # health management system
# # 3 clients Akhil, vinit, umesh
#
# # total 6 files
# # write a function that when executed takes as input client name
# # one more function to retrive exercise or food for any client
#
# import datetime
#
#
# def getdate():
#     return datetime.datetime.now()
#
#
# def take(k):
#     if k == 1:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             value = input('type here \n')
#             with open("Akhil-ex.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#         elif c == 2:
#             value = input('type here \n')
#             with open("Akhil-food.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#     elif k == 2:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             value = input('type here \n')
#             with open("Vinit-ex.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#         elif c == 2:
#             value = input('type here \n')
#             with open("Vinit-food.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#     elif k == 3:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             value = input('type here \n')
#             with open("Umesh-ex.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#         elif c == 2:
#             value = input('type here \n')
#             with open("Umesh-food.txt", 'a') as op:
#                 op.write(str([str(getdate())]) + " : " + value + "\n")
#             print("successfully written")
#     else:
#         print("Please enter valid input (1(akhil), 2(vinit), 3(umesh))")
#
#
# def retrive(k):
#     if k == 1:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             with open('Akhil-ex.txt') as op:
#                 for i in op:
#                     print(i, end="")
#         elif c == 2:
#             with open('Akhil-food.txt') as op:
#                 for i in op:
#                     print(i, end="")
#
#     elif k == 2:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             with open('Vinit-ex.txt') as op:
#                 for i in op:
#                     print(i, end="")
#         elif c == 2:
#             with open('Vinit-food.txt') as op:
#                 for i in op:
#                     print(i, end="")
#
#     elif k == 3:
#         print("Enter 1 for exercise and 2 for food")
#         c = int(input())
#         if c == 1:
#             with open('Umesh-ex.txt') as op:
#                 for i in op:
#                     print(i, end="")
#         elif c == 2:
#             with open('Umesh-food.txt') as op:
#                 for i in op:
#                     print(i, end="")
#
#     else:
#         print('Please enter valid input (akhi, vinit, umesh)')
#
#
# print("Health Management System")
# a = int(input("press 1 for log the values and 2 for retrieve :"))
#
# if a == 1:
#     b = int(input("press 1 for akhil 2 for vinit 3 for umesh"))
#     take(b)
#
# else:
#     b = int(input("press 1 for akhil 2 for vinit 3 for umesh"))
#     retrive(b)
#



















# #                            health management system
# 3 clients Akhil, vinit, umesh

# total 6 files
# write a function that when executed takes as input client name
# one more function to retrive exercise or food for any client

import datetime


def getdate():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            value = input('type here \n')
            with open("Akhil-ex.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input('type here \n')
            with open("Akhil-food.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
    elif k == 2:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            value = input('type here \n')
            with open("Vinit-ex.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input('type here \n')
            with open("Vinit-food.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
    elif k == 3:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            value = input('type here \n')
            with open("Umesh-ex.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input('type here \n')
            with open("Umesh-food.txt", 'a') as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(akhil), 2(vinit), 3(umesh))")


def retrive(k):
    if k == 1:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            with open('Akhil-ex.txt') as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open('Akhil-food.txt') as op:
                for i in op:
                    print(i, end="")

    elif k == 2:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            with open('Vinit-ex.txt') as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open('Vinit-food.txt') as op:
                for i in op:
                    print(i, end="")

    elif k == 3:
        print("Enter 1 for exercise and 2 for food")
        c = int(input())
        if c == 1:
            with open('Umesh-ex.txt') as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open('Umesh-food.txt') as op:
                for i in op:
                    print(i, end="")

    else:
        print('Please enter valid input (akhi, vinit, umesh)')


print("Health Management System")
a = int(input("press 1 for log the values and 2 for retrieve :"))

if a == 1:
    b = int(input("press 1 for akhil 2 for vinit 3 for umesh"))
    take(b)

else:
    b = int(input("press 1 for akhil 2 for vinit 3 for umesh"))
    retrive(b)












