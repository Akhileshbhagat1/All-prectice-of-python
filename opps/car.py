command = ""
count = False
while True:
    print(' enter your car status " START or STOP" for exit "quit"')
    command = input('> ').lower()

    if command == 'start':
        if count:
            print('car already started..!')
        else:
            count = True
            print('car  started')

    elif command == 'stop':
        if not count:
            print('car already stopped..!')
        else:
            count = False
        print('car  stopped')

    elif command == 'help':
        print('''
start = to start car
stop = to stop car
quit = to exit''')

    elif command == 'quit':
        break
    else:
        print(" i don't understand ")
