d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}


def is_key_present(i):
    if i in d:
        print(i, 'is present as a  key')
    else:
        print(i, 'is not present as a key ')


is_key_present(3)
