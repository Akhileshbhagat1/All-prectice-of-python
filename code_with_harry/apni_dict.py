# here create a dict and take input from user and return the meaning fo the word from that dictionary
while True:
    d = {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog', 'e': 'elephant', 'h': 'hen', 'i': 'ice-cream',
         'j': 'jackfruit'}
    print("Enter your word : ")
    key = input()
    if key in d.keys():
        print(d[key])
    print("Press y for continue and Enter for 'quit'")
    name = input()
    if name == 'y':
        continue
    elif name == '':
        break



