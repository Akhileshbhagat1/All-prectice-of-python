catnames = []
while True:
    print("Enter the name of Cates " + str(len(catnames) + 1) + ' (Or Enter nothing to stop.):')
    names = input()
    if names == '':
        break
    catnames = catnames + [names]  # list concatinations
print("Cat names are : ")
for names in catnames:
    print(' ' + names)
    Print("success")
