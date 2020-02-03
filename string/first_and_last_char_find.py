def string_both_end(str1):
    if len(str1) < 2:
        return 'empty string'
    return str1[0:2] + str1[-2:]


print(string_both_end('abcdef'))
print(string_both_end('ab'))
print(string_both_end('a'))
