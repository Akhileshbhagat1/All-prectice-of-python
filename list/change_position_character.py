def change_char(str1):
    char_1 = str1[0:3]
    str1 = str1.replace(char_1, 'ram')
    str1 = char_1 + str1[3:]
    return str1


print(change_char('man is not a man with man available man'))
