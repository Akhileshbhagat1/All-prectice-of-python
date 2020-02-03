# birthday = {'akhilesh': '18 oct', 'vinit': '26 Aug', 'mithlesh': '11 Apr'}
#
# while True:
#     print('Enter a name ("blank to quit")')
#     name = input()
#     if name == '':
#         break
#     if name in birthday:
#         print(birthday[name] + 'is birthday of ' + name)
#     else:
#         print('I do not have birthday information of ' + name)
#         print('what is their birthday?')
#         bday = input()
#         birthday[name] = bday
#         print('birthday database is updated')

birthdays = {'akhilesh': '18 oct', 'umseh': '4 feb', 'mithlesh': '11 Apr'}

while True:
    print('Enter your name ("Blank for quit")')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print(name + ' birthday is not in database')
        print('what is his/her birthday ?')
        bday = input()
        birthdays[name] = bday
        print(name + ' is added into our database')


























