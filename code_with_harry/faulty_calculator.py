while True:
    def calculate(op, x, y):
        if op == '+' and x == 56 and y == 9:
            return 77
        elif op == '*' and x == 45 and y == 3:
            return 555
        elif op == '/' and x == 56 and y == 6:
            return 4
        return {
            '+': lambda: x + y,
            '-': lambda: x - y,
            '*': lambda: x * y,
            '/': lambda: x / y,
        }.get(op, lambda: None)()
    op = input("Enter your operator\n + for Add \n - for Subtract\n * for multiply\n / for divide\n :- ")
    first = int(input("Enter first number "))
    second = int(input("Enter second number "))
    print(calculate(op, first, second))
    print(" do you want to continue pres y if not press enter to quit")

    name = input()
    if name == '':
        break
    elif name == 'y':
        continue

# ####################################################33
# num1=int(input("Enter your First Number: "))
# num2=int(input("Enter your First Number: "))
# opt=input("Choose you operator(+,-,*,/): ")
#
#
# if(num1==45 and num2==3 and opt=="*"):
#     print(555)
# elif(num1==56 and num2==9 and opt=="+"):
#     print(77)
# elif(num1==56 and num2==6 and opt=="/"):
#     print("4")
# elif(opt=="+"):
#     print(num1+num2)
# elif(opt=="-"):
#     print(num1-num2)
# elif(opt=="*"):
#     print(num1*num2)
# elif(opt=="/"):
#     print(num1/num2)
# ###############################################################3
# while(True):
#     x = int(input("enter your first no.: "))
#     y = input("enter the operator: ")
#     z = int(input("enter your second no.: "))
#     if x == 45 and y == "*" and z == 3:
#         print("= 555")
#     elif x == 56 and y == "+" and z == 9:
#         print("= 77")
#     elif x == 56 and y == "/" and z == 6:
#         print("= 4")
#     elif y == "+":
#         print(int(x) + int(z))
#     elif y == "-":
#         print(int(x) - int(z))
#     elif y == "*":
#         print(int(x) * int(z))
#     elif y == "/":
#         print(int(x) / int(z))
#     else:
#         print("invalid data")
#
#     inp=input("Want to use again? y for YES n for NO \n")
#     if inp=="y":
#         continue
#     elif inp == "n":
#         break




