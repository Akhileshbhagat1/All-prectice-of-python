print("Enter a no ")
num = int(input())
if num % 2 == 0:
    bul = True
else:
    bul = False

while True:
    if bul:
        for i in range(num + 1):
            for j in range(i):
                print('*', end='')
            print('\n')
        break
    elif not bul:
        for i in range(num, 0, -1):
            for j in range(0, i):
                print('*', end='')
            print('\n')
        bul = True
        break


