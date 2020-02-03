catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break

    catNames = catNames + [name]  # list concatenation
# print(catNames)
print('The cat names are:')
for name in catNames:
    print('  ' + name)

# list = []
# while True:
# 	print('enter your name'+' ' + str(len(list)+1)+'(Or enter nothing to stop)')
# 	name = input()
# 	if name == '':
# 		break
# 	list = list + [name]
# print(' total names are:')
# for i in list:
# 	print("   "+i)


myName = []
while True:
    print('enter your subject names' + ' ' + str(len(myName) + 1) + '(Or type enter to stop.)')
    name = input()
    if name == '':
        break
    myName = myName + [name]
print('total names are :')
for i in myName:
    print("  " + i)
